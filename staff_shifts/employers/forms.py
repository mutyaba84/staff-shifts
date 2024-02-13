# employers/forms.py
from django import forms
from .models import EmployerProfile

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['description']  # Add other fields as needed
