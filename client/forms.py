from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.views.generic.edit import FormView
from django.forms import ClearableFileInput

class RegisterUserForm(UserCreationForm):
    
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'id': 'username',
                                                            'class': "validate"
                                                             }))
    password1 = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'id': 'password1',
                                                            'class': "validate"
                                                                 }))
    password2 = forms.CharField(label='Повтор пароля', 
                               widget=forms.PasswordInput(attrs={'id': 'password2',
                                                            'class': "validate"
                                                                 }))
    
    class Meta:
        model = User
        fields = {'username', 'password2','password1'}
       
