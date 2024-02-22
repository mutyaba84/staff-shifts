
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from user_profiles.models import UserProfile, Address
from employers.models import Employer
from notifications.models import Notification


class Shift(models.Model):
    CANCELLED = 'cancelled'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]


    max_users = models.PositiveIntegerField(default=1)
    shift_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    reminder_enabled = models.BooleanField(default=False)
    reminder_days_before = models.PositiveIntegerField(default=3)

    # Add address details for the employer
    employer_address_line1 = models.CharField(max_length=255, blank=True, null=True)
    employer_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    employer_city = models.CharField(max_length=255, blank=True, null=True)
    employer_state = models.CharField(max_length=255, blank=True, null=True)
    employer_postal_code = models.CharField(max_length=20, blank=True, null=True)

    def send_reminder(self):
        if self.reminder_enabled:
            reminder_date = self.start_time - timezone.timedelta(days=self.reminder_days_before)
            if timezone.now() <= reminder_date:
                notification_content = f'Reminder: Your shift "{self.shift_name}" is scheduled for {self.start_time}.\n' \
                                       f'Employer Address: {self.get_employer_full_address()}\n' \
                                       f'Map: {self.get_employer_map_url()}'
                for offer in self.shiftoffer_set.all():
                    Notification.objects.create(user=offer.user.user, content=notification_content)

    def get_employer_full_address(self):
        address_parts = [self.employer_address_line1, self.employer_address_line2, self.employer_city,
                         self.employer_state, self.employer_postal_code]
        return ', '.join(filter(None, address_parts))

    def get_employer_map_url(self):
        if self.employer_address_line1 and self.employer_city and self.employer_state:
            address_for_map = f'{self.employer_address_line1}, {self.employer_city}, {self.employer_state}'
            # You can replace the API_KEY with your actual Google Maps API key
            api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
            return f'https://www.google.com/maps/embed/v1/place?key={api_key}&q={address_for_map}'
        else:
            return 'Map not available'

    def cancel_shift(self):
        if self.status != self.CANCELLED:
            self.status = self.CANCELLED
            self.save()

            notification_content = f'The shift "{self.shift_name}" has been canceled.'
            for offer in self.shiftoffer_set.all():
                Notification.objects.create(user=offer.user.user, content=notification_content)
                Notification.objects.create(user=offer.employer.user, content=notification_content)



class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shift_availability')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='shift_availability')
    date_time_selected = models.DateTimeField()
    is_available = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'date_time_selected']

    def clean(self):
        if self.shift.start_time and self.shift.end_time and self.date_time_selected:
            if self.shift.start_time <= self.date_time_selected < self.shift.end_time:
                raise ValidationError("User cannot work overlapping shifts.")


class ShiftOffer(models.Model):
    user = models.ForeignKey(User, related_name='shift_offers_received', on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, related_name='offers_sent', on_delete=models.CASCADE)
    shift = models.ForeignKey('Shift', on_delete=models.CASCADE)
    offer_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    offer_message = models.TextField(blank=True, null=True)