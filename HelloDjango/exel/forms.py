from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.views.generic.edit import FormView
from django.forms import ClearableFileInput


class FileModelForm(forms.ModelForm):
    class Meta:
        model = FeedFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }

class UtmForm(forms.ModelForm):
    class Meta:
        model = Cleared
        fields = ['utm',]

class ReportForm(forms.ModelForm):
    report = forms.FileField(label='Отчет')
    class Meta:
        model = All_file
        fields = ['report',]
class ClearForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
    access = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
    mp = forms.FileField(required=False)
    name_rk = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
    landing = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
    class Meta:
        model = Cleared
        fields = ['comments', 'access', 'landing', 'mp', 'name_rk',]

class CommentForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
    presentation = forms.FileField(required=False)
    mp = forms.FileField(required=False)
    name_rk = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
    class Meta:
        model = All_file
        fields = ['comments', 'name_rk', 'presentation', 'mp',]

class BriefForm(forms.ModelForm):
    img = forms.ImageField(label='Логотип', required=False)
    class Meta:
        model = Brief
        fields = ['img',]
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['calculation',]
        
class DmpForm(forms.ModelForm):
    class Meta:
        model = Dmp
        fields = ['file',]

class RegisterUserForm(UserCreationForm):
    
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             'style': 'width:180px;height:18px'
                                                             }))
    email = forms.EmailField(label='Email', 
                               widget=forms.EmailInput(attrs={'class': 'form-input',
                                                              'style': 'width:180px;height:18px'
                                                              }))
    password1 = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'style': 'width:180px;height:18px'
                                                                 }))
    password2 = forms.CharField(label='Повтор пароля', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'style': 'width:180px;height:18px'
                                                                 }))
    
    class Meta:
        model = User
        fields = {'email', 'username', 'password2','password1'}
       

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
