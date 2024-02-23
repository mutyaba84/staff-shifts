from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
        # If you want to customize the appearance of the content field, you can do it here

    def save(self, user, commit=True):
        instance = super(NotificationForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance
