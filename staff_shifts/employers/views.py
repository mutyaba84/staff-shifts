# employers/views.py
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import EmployerProfile
from .forms import EmployerProfileForm
from shifts.models import Shift

class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'employers/create_employer_profile.html'
    success_url = '/employers/'

class EmployerProfileUpdateView(UpdateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'employers/update_employer_profile.html'
    success_url = '/employers/'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Set reminders for shifts
        shifts = Shift.objects.filter(user=self.request.user)
        for shift in shifts:
            shift.send_reminder()

        return response

