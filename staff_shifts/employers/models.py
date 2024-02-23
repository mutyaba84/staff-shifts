# employers/models.py
from django.db import models
from django.contrib.auth.models import User

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='employer_logos/', blank=True, null=True)
    # Add other fields for employer profile details as needed

    def __str__(self):
        return f'{self.user.username} Profile'

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(User, related_name='employers', blank=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    # Add other fields for employer details as needed

    def __str__(self):
        return self.name
