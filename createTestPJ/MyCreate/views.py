from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import MyCreateTable
 
class MyCreateView(CreateView):
    template_name = "MyCreate.html"
    model = MyCreateTable
    fields = ('username', 'password', 'email', 'memo')
    success_url = reverse_lazy('MyCreate:MyCreatePage')