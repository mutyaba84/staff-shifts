from django import forms
from .models import Shift, Availability, ShiftOffer

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['shift_name', 'start_time', 'end_time', 'max_users']

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['user', 'shift', 'address', 'date_time_selected', 'is_available']

class ShiftOfferForm(forms.ModelForm):
    class Meta:
        model = ShiftOffer
        fields = ['user', 'employer', 'shift', 'offer_status', 'offer_message']
