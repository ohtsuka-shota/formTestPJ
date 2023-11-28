from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import MyFormView

app_name = "MyForm"

urlpatterns = [
    path('', MyFormView.as_view(), name="MyFormPage"),
]