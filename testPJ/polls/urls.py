# This is polls app urls.py

from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views
from .views import QuestionList, pollsHome

app_name = 'polls'
QuestionList_view = TemplateView.as_view()

urlpatterns = [
    path("questionlist/",  login_required(QuestionList.as_view()), name="QuestionList"),
    path("", pollsHome.as_view(), name="polls"),
]
