from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import todoTable

class todoListView(ListView):
    template_name = "todoList.html"
    model = todoTable

class todoDetailView(DetailView):
    template_name = "todoDetail,html"
    model = todoTable