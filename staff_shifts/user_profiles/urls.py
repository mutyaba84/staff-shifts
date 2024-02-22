# user_profiles/urls.py
from django.urls import path
from .views import profile, UserRegistrationView, UserProfileUpdateView, UserProfileDetailView, UserProfileEditView, UserProfileListView

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('profile/detail/<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/<int:pk>/', UserProfileEditView.as_view(), name='profile_edit'),
    path('profile/list/', UserProfileListView.as_view(), name='profile_list'),
    # Add more URL patterns as needed
]
