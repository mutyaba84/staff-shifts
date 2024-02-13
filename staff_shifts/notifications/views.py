# notifications/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'notifications/notifications.html', {'notifications': user_notifications})
