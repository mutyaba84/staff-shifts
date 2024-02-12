from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    subscription_valid_until = models.DateField(null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=50, null=True, blank=True)
    is_group_subscription = models.BooleanField(default=False)
    group_subscription_id = models.CharField(max_length=50, null=True, blank=True)
    subscription_enabled = models.BooleanField(default=True)

@receiver(pre_save, sender=UserProfile)
def check_subscription_status(sender, instance, **kwargs):
    if instance.is_employer and instance.subscription_valid_until and instance.subscription_enabled:
        months_before_notification = 3
        notification_date = instance.subscription_valid_until - timezone.timedelta(days=30 * months_before_notification)

        if timezone.now().date() >= notification_date:
            send_subscription_notification(instance.user, notification_date)

class Address(models.Model):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

class Shift(models.Model):
    max_users = models.PositiveIntegerField(default=1)
    shift_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_time_selected = models.DateTimeField()
    is_available = models.BooleanField(default=False)

class ShiftOffer(models.Model):
    user = models.ForeignKey(User, related_name='offers_received', on_delete=models.CASCADE)
    employer = models.ForeignKey(User, related_name='offers_sent', on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    offer_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    offer_message = models.TextField(blank=True, null=True)
