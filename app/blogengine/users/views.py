from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationModelForm

class UserRegistrationView(CreateView):
    form_class = UserCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'users/registration.html'

# Create your views here.
