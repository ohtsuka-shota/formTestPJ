from django.urls import path
from .views import MyCreateView

app_name = "MyCreate"

urlpatterns = [
    path("", MyCreateView.as_view(), name="MyCreatePage"),
]
