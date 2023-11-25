# This is Project views.py

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class homeView(TemplateView):
    template_name = "home.html"

class UserCreateView(CreateView):
    template_name = 'userCreate.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')