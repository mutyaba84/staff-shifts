# user_profiles/admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_employer', 'subscription_valid_until', 'stripe_customer_id', 'is_group_subscription', 'group_subscription_id', 'subscription_enabled')
