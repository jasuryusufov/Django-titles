from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
    {
        "class": 'form-control',
        'placeholder': "Foydalanuvchi ismi"
    }
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Parol"
    }
    ))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        "class": "form-control",
        "placeholder": "Parol"
    }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        "class": "form-control",
        "placeholder": "Parol Tasdiqlash"
    }
    ))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Foydalanuvchi ismi'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Email"
            })
        }
