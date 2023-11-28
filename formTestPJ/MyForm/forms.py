from django import forms
from .models import MyFormTable

class MyForm(forms.ModelForm):
    class Meta:
        model = MyFormTable
        fields = ['username', 'password', 'email', 'memo']
        widgets = {
            'password': forms.PasswordInput(),
        }