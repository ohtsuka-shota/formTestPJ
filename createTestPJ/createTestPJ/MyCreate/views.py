from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import MyCreate
from .models import MyCreateTable
 
class HogeCreateView(CreateView):
    template_name = "MyCreate.html"
    model = MyCreateTable
    form_class = MyCreate
    success_url = reverse_lazy('MyCreate:MyCreatePage')