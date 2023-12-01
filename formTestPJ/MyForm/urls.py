from django.contrib import admin
from django.urls import path
from .views import MyFormView

app_name = "MyForm"

urlpatterns = [
    path('', MyFormView.as_view(), name="MyFormPage"),
]
