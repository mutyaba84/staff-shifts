from django.contrib import admin
from .models import UserProfile, Address, Shift, Availability, ShiftOffer

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_employer', 'subscription_valid_until', 'subscription_enabled')
    search_fields = ('user__username', 'user__email')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line1', 'city', 'state', 'postal_code')
    search_fields = ('address_line1', 'city', 'state', 'postal_code')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shift_name', 'start_time', 'end_time', 'max_users')

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('user', 'shift', 'address', 'date_time_selected', 'is_available')
    search_fields = ('user__username', 'shift__shift_name', 'address__address_line1')

@admin.register(ShiftOffer)
class ShiftOfferAdmin(admin.ModelAdmin):
    list_display = ('user', 'employer', 'shift', 'offer_status', 'offer_message')
    search_fields = ('user__username', 'employer__username', 'shift__shift_name')
