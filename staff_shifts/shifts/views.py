# shifts/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Shift, ShiftOffer
from .forms import ShiftForm, ShiftOfferForm
from user_profiles.models import UserProfile
from employers.models import Employer
from notifications.models import Notification

class ShiftListView(ListView):
    model = Shift
    template_name = 'shifts/shift_list.html'
    context_object_name = 'shifts'

class ShiftCreateView(CreateView):
    model = Shift
    form_class = ShiftForm
    template_name = 'shifts/create_shift.html'
    success_url = '/shifts/'

    def form_valid(self, form):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile.is_employer:
            form.instance.user = user_profile
            return super().form_valid(form)
        else:
            messages.error(self.request, "Only employers can create shifts.")
            return redirect('/shifts/')

class ShiftUpdateView(UpdateView):
    model = Shift
    form_class = ShiftForm
    template_name = 'shifts/update_shift.html'
    success_url = '/shifts/'

class MakeOfferView(CreateView):
    model = ShiftOffer
    form_class = ShiftOfferForm
    template_name = 'shifts/make_offer.html'
    success_url = '/shifts/'

    def form_valid(self, form):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile.is_employer:
            form.instance.user = user_profile
            return super().form_valid(form)
        else:
            messages.error(self.request, "Only employers can offer shifts.")
            return redirect('/shifts/')

    def get_success_url(self):
        shift_id = self.object.shift.id
        return f'/shifts/{shift_id}/'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Notify the user about the offer
        notification_content = f'You received a new offer for the shift "{self.object.shift}".'
        Notification.objects.create(user=self.object.user.user, content=notification_content)
        return response

class CancelShiftView(UpdateView):
    model = Shift
    template_name = 'shifts/cancel_shift.html'  # Create a template for shift cancellation if needed

    def form_valid(self, form):
        # Cancel the shift
        shift = form.save(commit=False)
        shift.cancel_shift()

        # Redirect to a success page or home
        return redirect('home')  # Change 'home' to the appropriate URL

class SetReminderView(UpdateView):
    model = Shift
    template_name = 'shifts/set_reminder.html'  # Create a template for setting reminders if needed

    def form_valid(self, form):
        # Update reminder settings
        shift = form.save(commit=False)
        shift.save()

        # Redirect to a success page or home
        return redirect('home')  # Change 'home' to the appropriate URL
