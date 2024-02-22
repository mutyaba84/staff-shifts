# user_profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm, UserRegistrationForm

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profiles/profile.html', {'user_profile': user_profile})

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user_profiles/registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_profile_form = UserProfileForm(self.request.POST, instance=self.object.profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
        return response

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profiles/profile_update.html'
    success_url = reverse_lazy('profile')

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'user_profiles/profile_detail.html'

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profiles/profile_edit.html'
    success_url = reverse_lazy('profile')

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'user_profiles/profile_list.html'
    context_object_name = 'user_profiles'
# user_profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm, UserRegistrationForm

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profiles/profile.html', {'user_profile': user_profile})

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user_profiles/registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_profile_form = UserProfileForm(self.request.POST, instance=self.object.profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
        return response

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profiles/profile_update.html'
    success_url = reverse_lazy('profile')

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'user_profiles/profile_detail.html'

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profiles/profile_edit.html'
    success_url = reverse_lazy('profile')

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'user_profiles/profile_list.html'
    context_object_name = 'user_profiles'
