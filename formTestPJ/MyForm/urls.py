from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import MyForm

app_name = "MyForm"

urlpatterns = [
    path('', MyForm.as_view(), name="MyForm"),
]