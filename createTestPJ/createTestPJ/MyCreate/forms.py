from django import forms
from .models import MyCreateTable

class MyCreate(forms.ModelForm):
    class Meta:
        model = MyCreateTable
        fields = ['username', 'password', 'email', 'memo']
        widgets = {
            'password': forms.PasswordInput(),
        }