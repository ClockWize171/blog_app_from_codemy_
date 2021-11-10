from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm as ucf
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = ucf
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

