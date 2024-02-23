# notifications/urls.py
from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
    # Add other notifications-related URLs as needed
]