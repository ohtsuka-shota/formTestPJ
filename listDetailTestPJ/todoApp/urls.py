from django.urls import path
from .views import todoListView, todoDetailView

app_name = "todoApp"

urlpatterns = [
    path("list/", todoListView.as_view(), name="todoListPage"),
    path("detail/<int:pk>", todoDetailView.as_view(), name="todoDetailPage"),
]