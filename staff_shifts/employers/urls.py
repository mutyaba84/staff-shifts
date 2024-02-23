# employers/urls.py
from django.urls import path
from .views import EmployerProfileCreateView, EmployerProfileUpdateView

app_name = 'employers'

urlpatterns = [
    path('create/', EmployerProfileCreateView.as_view(), name='create_profile'),
    path('update/', EmployerProfileUpdateView.as_view(), name='update_profile'),
]
