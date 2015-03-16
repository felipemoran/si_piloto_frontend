from sistema.models import *
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields =[
            'password',
            'email',
            'first_name',
            'last_name',
        ]

