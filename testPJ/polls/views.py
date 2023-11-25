# This is polls app views.py

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import Question

# Create your views here.
class pollsHome(TemplateView):
    template_name = "polls/polls_home.html"

class QuestionList(LoginRequiredMixin, ListView):
    model = Question
    template_name = "polls/QuestionList.html"
