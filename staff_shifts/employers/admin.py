from django.contrib import admin
from .models import EmployerProfile, Employer

@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'description']
    search_fields = ['user__username', 'description']
    # Add other configurations as needed

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    search_fields = ['user__username', 'name']
    # Add other configurations as needed
