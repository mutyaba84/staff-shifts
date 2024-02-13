# notifications/forms.py
from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['user', 'content', 'is_read']
