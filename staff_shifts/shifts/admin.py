from django.contrib import admin
from .models import Shift, Availability, ShiftOffer


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['shift_name', 'start_time', 'end_time', 'status']
    search_fields = ['shift_name', 'status']
    list_filter = ['status', 'reminder_enabled']
    date_hierarchy = 'start_time'
    actions = ['cancel_selected_shifts']

    def cancel_selected_shifts(self, request, queryset):
        for shift in queryset:
            shift.cancel_shift()
        self.message_user(request, f'Selected shifts have been canceled.')

    cancel_selected_shifts.short_description = 'Cancel selected shifts'


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['user', 'shift', 'date_time_selected', 'is_available']
    search_fields = ['user__username', 'shift__shift_name', 'date_time_selected']
    list_filter = ['is_available', 'shift__shift_name', 'user__username']
    date_hierarchy = 'date_time_selected'




@admin.register(ShiftOffer)
class ShiftOfferAdmin(admin.ModelAdmin):
    list_display = ['user', 'employer', 'shift', 'offer_status']
    search_fields = ['user__username', 'employer__user__username', 'shift__shift_name', 'offer_status']
    list_filter = ['offer_status', 'shift__shift_name', 'user__username', 'employer__user__username']
