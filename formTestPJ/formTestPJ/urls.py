from django.contrib import admin
from django.urls import path
from .views import MyForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyForm.as_view(), name="UserCreate"),
]