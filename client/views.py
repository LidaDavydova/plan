from doctest import Example
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from tablib import Dataset
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import *
from django.urls import reverse, reverse_lazy
from django.views.generic.base import *
from django.views.generic import *
from django.conf import settings
from django.contrib import messages
from .forms import *
from django.core.files.storage import FileSystemStorage
import pandas as pd 
from django.utils.datastructures import MultiValueDictKeyError
import os
from transliterate.decorators import transliterate_function

@transliterate_function(language_code='ru', reversed=True)
def translit(text):
    return text
# Create your views here.

class RegisterView(CreateView):
    form_class  = RegisterUserForm
    template_name = 'registration.html'

    success_url = reverse_lazy('client:profile')

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterView, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

def Logout(request):
    logout(request)
    return redirect('client:profile')

def profile(request):
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    headers = ['kpi', 'Название аудитории', 'Описание аудитории', 'Сезонники', 'Сайт', 'Место размещения на сайте и таргетинги', 'Размер (в пикселях) / Формат',
        'Тип размещения', 'Единица покупки', 'Цена (за единицу покупки), руб.', 'Наценки / Доп. Скидки', 'Скидка, %', 'Частота', 'VTR,%', 'CTR,%',
        'Ёмкость в месяц', 'Комментарии']
    if request.user.is_authenticated:
        print(request.user.username)
        if not os.path.isdir(os.path.join(path, 'sites', translit(request.user.username))):
            os.mkdir(os.path.join(path, 'sites', translit(request.user.username)))
        fs = FileSystemStorage(location=os.path.join(path, 'sites', translit(request.user.username)), base_url=path)
        try:
            wb = pd.read_excel(os.path.join(path, 'sites', translit(request.user.username), 'second_part.xlsx'), engine='openpyxl', header=0)

            '''turn dict'''
            wb2 = [i for i in wb.values]
            wb = {}
            for i in range(len(wb2)):
                wb[i] = wb2[i]
        except:
            wb = pd.DataFrame({})
            wb.to_excel(os.path.join(path, 'sites', translit(request.user.username), 'second_part.xlsx'), header=headers, index=None)
    else:
        wb={}

    # LogIn
    if request.method == 'POST' and 'form_login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

    # Inputs
    if request.method == 'POST' and 'form_add' in request.POST:
        mediakit = request.FILES.get('mediakit', None)
        price = request.FILES.get('price', None)
        example = request.FILES.get('example', None)
        TT = request.FILES.get('TT', None)

        mediakit_text = request.POST.get('mediakit_text', None)
        price_text = request.POST.get('price_text', None)
        example_text = request.POST.get('example_text', None)
        TT_text = request.POST.get('TT_text', None)

        AdRiver1 = request.POST.get('checkbox1', None)
        AdRiver2 = request.POST.get('checkbox2', None)
        AdRiver3 = request.POST.get('checkbox3', None)
        AdRiver4 = request.POST.get('checkbox4', None)
        contacts = request.POST.get('contacts', None)
        advantages = request.POST.get('advantages', None)
        minuses = request.POST.get('minuses', None)
        budget = request.POST.get('budget', None)
        prepayment = request.POST.get('prepayment', None)
        dop_comments = request.POST.get('dop_comments', None)
        launch = request.POST.get('launch', None)
        try:
            profile = Profile.objects.get(user_id=request.user.id)
        except ObjectDoesNotExist:
            return redirect('client:registr')
        if mediakit:
            name = translit(mediakit.name)
            try:
                os.remove(os.path.join(path, 'sites', translit(request.user.username), translit(profile.mediakit)))
            except:
                pass
            profile.mediakit = name
            fs.url(fs.save(name, mediakit)) #url
        if price:
            name = translit(price.name)
            try:
                os.remove(os.path.join(path, 'sites', translit(request.user.username), translit(profile.price)))
            except:
                pass
            profile.price = name
            fs.url(fs.save(name, price))
        if example:
            name = translit(example.name)
            try:
                os.remove(os.path.join(path, 'sites', translit(request.user.username), translit(profile.example)))
            except:
                pass
            profile.example = name
            fs.url(fs.save(name, example))
        if TT:
            name = translit(TT.name)
            try:
                os.remove(os.path.join(path, 'sites', translit(request.user.username), translit(profile.TT)))
            except:
                pass
            profile.TT = name
            fs.url(fs.save(name, TT))
        if mediakit_text!='':
            profile.mediakit_text = translit(mediakit_text)
        if price_text!='':
            profile.price_text = translit(price_text)
        if example_text!='':
            profile.example_text = translit(example_text)
        if TT_text!='':
            profile.TT_text = translit(TT_text)
        
        AdRiver = []
        for i in [AdRiver1, AdRiver2, AdRiver3, AdRiver4]:
            if i:
                AdRiver.append(i)
        profile.AdRiver = ', '.join(AdRiver)
        if contacts!='':
            profile.contacts = contacts
        if advantages!='':
            profile.advantages = advantages
        if minuses!='':
            profile.minuses = minuses
        if budget!='':
            profile.budget = budget
        if prepayment!='':
            profile.prepayment = prepayment
        if dop_comments!='':
            profile.dop_comments = dop_comments
        if launch!='':
            profile.launch = launch
        profile.save()
        
        return render(request, 'profile.html', {
            'profile': Profile.objects.get(user_id=request.user.id),
            'data': wb
        })
        
    # Green table
    if request.method=='POST' and 'form' in request.POST:
        result = {}
        for key, val in wb.items():
            row = []
            for i in range(1, len(val)+1):
                row.append(request.POST.get(f'{key}_{i}', '-'))
            result[key] = row
        number = len(result)
        
        # New rows
        new_input = request.POST.getlist('new_input')
        k = 0
        for i in range(17, len(new_input)+1, 17):
            result[number] = new_input[k:i]
            k+=17
            number+=1
        data = {'data': result}

        # rotate massive for DataFrame
        result2 = [i for i in result.values()]
        result = {}
        for i in range(len(result2[0])):
            k = []
            for j in range(len(result2)):
                k.append(result2[j][i])
            result[i] = k
        
        pd.DataFrame(result).to_excel(os.path.join(path, 'sites', translit(request.user.username), 'second_part.xlsx'), header=headers, index=None)
    else:
        data = {'data': wb}
    try:
        data['profile'] = Profile.objects.get(user_id=request.user.id)
    except:
        pass
    return render(request, 'profile.html', data)