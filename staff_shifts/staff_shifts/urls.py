"""
URL configuration for staff_shifts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employers/', include('employers.urls', namespace='employers')),
    

    # Include user_profiles app URLs
    path('user_profiles/', include('user_profiles.urls')),
    
    # Include shifts app URLs
    path('shifts/', include('shifts.urls')),
    
    # Include notifications app URLs
    path('notifications/', include('notifications.urls')),
    
    # Add more app-specific URLs as needed
    
    # Include authentication URLs (assuming you're using Django's built-in authentication)
    path('accounts/', include('django.contrib.auth.urls')),
    # Add your home or landing page URL here
    # path('', include('your_app.urls')),
]

