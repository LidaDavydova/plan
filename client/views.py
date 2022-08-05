from doctest import Example
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from sqlalchemy import false
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
    if request.user.is_authenticated:
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        if not os.path.isdir(os.path.join(path, 'sites', request.user.username)):
            os.mkdir(os.path.join(path, 'sites', request.user.username))
        fs = FileSystemStorage(location=os.path.join(path, 'sites', request.user.username), base_url=path)
        try:
            wb = pd.read_excel(os.path.join(path, 'sites', request.user.username, 'second_part.xlsx'), header=None)

            '''turn dict'''
            wb2 = [i for i in wb.values]
            wb = {}
            for i in range(len(wb2)):
                wb[i] = wb2[i]
        except:
            wb = pd.DataFrame({})
            wb.to_excel(os.path.join(path, 'sites', request.user.username, 'second_part.xlsx'), header=None, index=None)
    else:
        wb={}

    if request.method == 'POST' and 'form_login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    if request.method == 'POST' and 'form_add' in request.POST:
        mediakit = request.FILES.get('mediakit', False)
        price = request.FILES.get('price', False)
        example = request.FILES.get('example', False)
        TT = request.FILES.get('TT', False)

        AdRiver1 = request.POST.get('checkbox1', False)
        AdRiver2 = request.POST.get('checkbox2', False)
        AdRiver3 = request.POST.get('checkbox3', False)
        AdRiver4 = request.POST.get('checkbox4', False)
        contacts = request.POST.get('contacts', False)
        advantages = request.POST.get('advantages', False)
        minuses = request.POST.get('minuses', False)
        budget = request.POST.get('budget', False)
        prepayment = request.POST.get('prepayment', False)
        dop_comments = request.POST.get('dop_comments', False)
        seasons = request.POST.get('seasons', False)
        launch = request.POST.get('launch', False)

        profile = Profile.objects.get(user_id=request.user.id)
        if mediakit:
            try:
                os.remove(os.path.join(path, 'sites', request.user.username, profile.mediakit))
            except:
                pass
            profile.mediakit = mediakit.name
            fs.url(fs.save(mediakit.name, mediakit)) #url
        if price:
            try:
                os.remove(os.path.join(path, 'sites', request.user.username, profile.price))
            except:
                pass
            profile.price = price.name
            fs.url(fs.save(price.name, price))
        if example:
            try:
                os.remove(os.path.join(path, 'sites', request.user.username, profile.example))
            except:
                pass
            profile.example = example.name
            fs.url(fs.save(example.name, example))
        if TT:
            try:
                os.remove(os.path.join(path, 'sites', request.user.username, profile.TT))
            except:
                pass
            profile.TT = TT.name
            fs.url(fs.save(TT.name, TT))
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
        if seasons!='':
            profile.seasons = seasons
        if launch!='':
            profile.launch = launch
        profile.save()
        
        return render(request, 'profile.html', {
            'profile': Profile.objects.get(user_id=request.user.id),
            'data': wb
        })
        '''
        profile = Profile.objects.get(user=request.user.id)
        profile.mediakit = mediakit
        profile.save()
        '''
    if request.method=='POST' and 'form' in request.POST:
        result = {}
        for key, val in wb.items():
            row = []
            for i in range(1, len(val)+1):
                row.append(request.POST.get(f'{key}_{i}'))
            result[key] = row
        number = len(result)
        

        new_input = request.POST.getlist('new_input')
        k = 0
        for i in range(17, len(new_input)+1, 17):
            result[number] = new_input[k:i]
            k+=17
            number+=1
        data = {'data': result}
        result2 = [i for i in result.values()]
        result = {}
        for i in range(len(result2[0])):
            k = []
            for j in range(len(result2)):
                k.append(result2[j][i])
            result[i] = k
        pd.DataFrame(result).to_excel(os.path.join(path, 'sites', request.user.username, 'second_part.xlsx'), header=None, index=None)
    else:
        data = {'data': wb}
    try:
        data['profile'] = Profile.objects.get(user_id=request.user.id)
    except:
        pass
    return render(request, 'profile.html', data)