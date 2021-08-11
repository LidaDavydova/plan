from django.shortcuts import render, redirect
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic.base import *
from django.views.generic import *
from django.conf import settings
from django.contrib import messages
import pandas as pd
import openpyxl
import os
import io
from django.http import FileResponse
from os.path import join
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font
from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils.dataframe import dataframe_to_rows


def main(request, super_us = False):
    if request.user.is_authenticated:
        username = request.user.username
        data = {
            'files': Client.objects.filter(username=username)[::-1],
            'cleared': Cleared.objects.filter(username=username)[::-1],
            'complete': Complete.objects.filter(username=username)[::-1]
                }
        #if not auth_user.objects.get()
        if request.user.is_superuser == 1:
            data['body'] = 'on'
            return render(request, 'base.html', data)
        data['body'] = 'off'
    else:
        return redirect('exel:login')
    return render(request, 'base.html', data)


class RegisterView(CreateView):
    form_class  = RegisterUserForm
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse('exel:main')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    
class Login(LoginView):
    form_class  = AuthenticationForm
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        return reverse('exel:main')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return redirect('exel:login')

class Prepare_calc(TemplateView):
    template_name = "prepare_calculation/prepare.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            data = {
                'client': Brief.objects.filter(username=username)[::-1],
                'form': BriefForm,
                #'now' : Brief.objects.filter(username=username),
                }
            if request.method == 'POST':
                username = username
                discount = request.POST.get('discount')
                AK = request.POST.get('AK')
                DCM = request.POST.get('DCM')
                client = request.POST.get('client')
                product = request.POST.get('product')
                name_rk = request.POST.get('name_rk')
                posad = request.POST.get('posad')
                type_act = request.POST.get('type_act')
                country = request.POST.get('country')
                region = request.POST.get('region')
                gender = request.POST.get('gender')
                age = request.POST.get('age')
                interes = request.POST.get('interes')
                income = request.POST.get('income')
                rek = request.POST.get('rek')
                materials = request.POST.get('materials')
                duration1 = request.POST.get('duration1')
                duration2 = request.POST.get('duration2')
                duration3 = request.POST.get('duration3')
                period_c = request.POST.get('period_c')
                period_p = request.POST.get('period_p')
                budget = request.POST.get('budget')
                KPI = request.POST.get('KPI')
                plan = request.POST.get('plan')
                description = request.POST.get('description')
                competitors = request.POST.get('competitors')
                who_prep_materials = request.POST.get('who_prep_materials')
            
                form = BriefForm(request.POST, request.FILES)
 
                if form.is_valid():
                    ex = request.FILES.get('img')
                    try:
                        if ex.name.lower().endswith(('.jpg', '.jepg', '.png', '.svg')):
                            Brief.objects.create(username=username, client=client, product=product,
                                         name_rk=name_rk, posad=posad, 
                                         type_act=type_act, country=country, 
                                         region=region, gender=gender, 
                                         age=age, interes=interes, income=income, 
                                         rek=rek, materials=materials,
                                         duration1=duration1, duration2=duration2,
                                         duration3=duration3,
                                         period_c=period_c, period_p=period_p,
                                         KPI=KPI, plan=plan, budget=budget,
                                         description=description, 
                                         competitors=competitors,
                                         who_prep_materials=who_prep_materials, img=ex,
                                         discount=discount, AK=AK, DCM=DCM)
                    except (NameError, AttributeError):
                        s = Brief.objects.filter(username=username, client=client)[::-1][0]
                        k = s.img.name
                        ak = s.AK
                        disc = s.discount
                        dcm = s.DCM
                        Brief.objects.create(username=username, client=client, product=product,
                                         name_rk=name_rk, posad=posad, 
                                         type_act=type_act, country=country, 
                                         region=region, gender=gender, 
                                         age=age, interes=interes, income=income, 
                                         rek=rek, materials=materials,
                                         duration1=duration1, duration2=duration2,
                                         duration3=duration3,
                                         period_c=period_c, period_p=period_p,
                                         KPI=KPI, plan=plan, budget=budget,
                                         description=description, 
                                         competitors=competitors,
                                         who_prep_materials=who_prep_materials, img=k,
                                         discount=disc, AK=ak, DCM=dcm)
                    except Location.MultipleObjectsReturned:
                        pass
                
                # In the down def to create a file DMP.xlsx
                for i in Dmp.objects.all():
                    n = i.file.url[1:]
                hol = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                p = pd.read_excel(os.path.join(hol, n),
                                     header=5)
                e = openpyxl.load_workbook(filename=os.path.join(hol, n), data_only=True)
                a = p["Категория Клиента"].tolist()
                b = p["KPI"].tolist()
                season = p["Сезонники"].tolist()
                season_discont = p["Сезонный коэф."].tolist()
                
                u = p["коэф. скидки от 1 (min стоимость плана) до  3 (max стоимость плана) "].tolist() 
                k = []
                for i in range(1, len(a)+1):
                    if (a[i-1] == 'Все' or a[i-1] == type_act) and b[i-1] == KPI and (u[i-1]=='1-3' or u[i-1] == str(Brief.objects.filter(username=username, client=client).first().discount)):
                        k.append(6+i)
                data = dict.fromkeys([i for i in p.columns.ravel()])
                d = []
                for j in k:
                    line = []
                    if season[j-7]=='проверить' or season[j-7]=='нет':
                        for i in range(1, len(p.columns.ravel())+1):
                            line.append(e['Лист1'].cell(row=j, column=i).value)
                        d.append(line)
                    else:
                        try:
                            for n in list(season[j-7].split()):
                                line1 = []
                                sd = list(season_discont[j-7].split())
                                for v in range(1, len(p.columns.ravel())+1):
                                    line1.append(e['Лист1'].cell(row=j, column=v).value)
                                line1[20] = sd[sd.index(n)+1]
                                line1[7] = n
                                d.append(line1)
                        except ValueError:
                            for i in range(1, len(p.columns.ravel())+1):
                                line.append(e['Лист1'].cell(row=j, column=i).value)
                                line[20] = list(season_discont[j-7].split())[list(season_discont[j-7].split()).index(season[j-1])+1]
                            d.append(line)
                        except AttributeError:
                            for i in range(1, len(p.columns.ravel())+1):
                                line.append(e['Лист1'].cell(row=j, column=i).value)
                            d.append(line)
                        
                for i in range(len(d[0])):
                    m = []
                    for j in range(len(d)):
                        m.append(d[j][i])
                    data[(p.columns.ravel())[i]] = m
                s = pd.DataFrame(data)
                
                if not os.path.exists(os.path.join(hol, f"media/clients/{username}")):
                    os.mkdir(os.path.join(hol, f"media/clients/{username}"))
                if not os.path.exists(os.path.join(hol, f"media/clients/{username}/{client}")):
                    os.mkdir(os.path.join(hol, f"media/clients/{username}/{client}"))
                s.to_excel(os.path.join(hol, f"media/clients/{username}/{client}/DMP_{name_rk}.xlsx"), startrow=1, index=False)
                
                ''' This is create brief file for clients'''
                for i in Brief_pattern.objects.all():
                    n = f'media/{i.file.name}'
                wb = openpyxl.load_workbook(filename=os.path.join(hol, n), data_only=True)
                ws = wb.worksheets[0]
                sheet = wb.active
                bd = Brief.objects.filter(username=username, client=client, 
                                       product=product, name_rk=name_rk)[::-1][0]
                sheet['C3'] = bd.client
                sheet['C4'] = bd.product
                sheet['C5'] = bd.name_rk
                sheet['C6'] = bd.posad
                sheet['C7'] = bd.description
                sheet['C8'] = bd.competitors
                sheet['C9'] = bd.type_act
                sheet['C11'] = bd.country
                sheet['C12'] = bd.region
                sheet['C14'] = bd.gender
                sheet['C15'] = bd.age
                sheet['C16'] = bd.interes
                sheet['C17'] = bd.income
                sheet['C18'] = bd.rek
                sheet['C20'] = bd.materials + bd.duration1 + bd.duration2 + bd.duration3
                sheet['C21'] = str(bd.period_c) + " - " + str(bd.period_p)
                sheet['C22'] = bd.budget
                sheet['C23'] = bd.KPI
                sheet['C24'] = bd.plan
                sheet['C25'] = bd.who_prep_materials
                sheet['H3'] = bd.discount
                sheet['H4'] = bd.AK
                sheet['H5'] = bd.DCM
                im = openpyxl.drawing.image.Image(bd.img)
                im.height = 250
                im.width = 250
                ws.add_image(im, 'H6')
                
                for row in sheet.iter_rows():
                    for cell in row:
                        cell.alignment = Alignment(wrap_text=True,vertical='top') 
                wb.save(os.path.join(hol, f"media/clients/{username}/{client}/brief_{name_rk}.xlsx"))
                path2 = join('clients', username, client, f'brief_{name_rk}.xlsx')
                
                '''This is correction DMP'''
                wb=load_workbook(os.path.join(hol, f"media/clients/{username}/{client}/DMP_{name_rk}.xlsx"))
                sheet = wb.active
                
                p = pd.read_excel(os.path.join(hol, f"media/clients/{username}/{client}/DMP_{name_rk}.xlsx"),
                                     header=1)
                season = p['Сезонники'].tolist()
                for row in sheet[f'H3':f'H{len(season)+1}']:
                    for cell in row:
                        if cell == 'проверить':
                            cell.fill = PatternFill(start_color='ff3333', end_color='ff3333', fill_type='solid')
                sheet.column_dimensions['B'].width = 10
                sheet.column_dimensions['C'].width = 8
                sheet.column_dimensions['D'].width = 17
                sheet.column_dimensions['E'].width = 11
                sheet.column_dimensions['F'].width = 145
                sheet.column_dimensions['G'].width = 11
                sheet.column_dimensions['H'].width = 14
                sheet.column_dimensions['I'].width = 65
                sheet.column_dimensions['J'].width = 13
                sheet.column_dimensions['K'].width = 13
                sheet.column_dimensions['L'].width = 13
                sheet.column_dimensions['M'].width = 15
                sheet.column_dimensions['N'].width = 15
                sheet.column_dimensions['O'].width = 19
                sheet.column_dimensions['P'].width = 45
                sheet.column_dimensions['Q'].width = 15
                sheet.column_dimensions['R'].width = 15
                sheet.column_dimensions['S'].width = 25
                sheet.column_dimensions['T'].width = 15
                sheet.column_dimensions['U'].width = 25
                sheet.column_dimensions['V'].width = 19
                sheet.column_dimensions['W'].width = 35
                sheet.column_dimensions['X'].width = 12
                sheet.column_dimensions['Y'].width = 12
                sheet.column_dimensions['Z'].width = 12
                sheet.column_dimensions['AA'].width = 12
                sheet.column_dimensions['AB'].width = 12
                sheet.column_dimensions['AC'].width = 8
                sheet.column_dimensions['AD'].width = 17
                sheet.column_dimensions['AE'].width = 11
                sheet.column_dimensions['AF'].width = 9
                sheet.column_dimensions['AG'].width = 12
                sheet.column_dimensions['AH'].width = 14
                sheet.column_dimensions['AI'].width = 14
                sheet.column_dimensions['AJ'].width = 15
                sheet.column_dimensions['AK'].width = 13
                sheet.column_dimensions['AL'].width = 13
                sheet.column_dimensions['AM'].width = 12
                sheet.column_dimensions['AN'].width = 12
                sheet.column_dimensions['AO'].width = 12
                sheet.column_dimensions['AP'].width = 12
                sheet.column_dimensions['AQ'].width = 12
                sheet.column_dimensions['AR'].width = 12
                sheet.column_dimensions['AS'].width = 12
                sheet.column_dimensions['AT'].width = 12
                sheet.column_dimensions['AU'].width = 12
                sheet.column_dimensions['AV'].width = 12
                sheet.column_dimensions['AW'].width = 12
                sheet.column_dimensions['AX'].width = 12
                sheet.column_dimensions['AY'].width = 20
                sheet.column_dimensions['AZ'].width = 12
                for row in sheet.iter_rows():
                    for cell in row:
                        cell.alignment = Alignment(wrap_text=True,vertical='top',
                                                   horizontal='center')
                        cell.border = Border(top = Side(border_style='thin', color='FF000000'),
                            right = Side(border_style='thin', color='FF000000'),
                            bottom = Side(border_style='thin', color='FF000000'),
                            left = Side(border_style='thin', color='FF000000')) 
                wb.save(os.path.join(hol, f"media/clients/{username}/{client}/DMP_{name_rk}.xlsx"))
                
                '''This is create mp'''
                p = pd.read_excel(os.path.join(hol, f"media/clients/{username}/{client}/DMP_{name_rk}.xlsx"), 
                                  header=None, skiprows=2, usecols = [1, 2, 3, 4, 5, 6, 7,
                                                                    8, 9, 10, 12, 13,
                                                                    14, 15, 16, 17,
                                                                    18, 19, 20, 21, 22,
                                                                    23, 24, 29, 30, 31])
                frequency = pd.read_excel(os.path.join(hol, f"media/clients/{username}/{client}/DMP_{name_rk}.xlsx"),
                                          header=None, skiprows=2, usecols = [37])
                fr = frequency.to_dict(orient='list')
                b = p.to_dict(orient='list')
                height = len(b[4])
                b[35] = b.pop(10)
                b[20] = [i for i in range(1, height+1)]
                
                for i in list(b.keys())[::-1]:
                    if i>=21:
                        b[i+1] = b.pop(i)
                
                b[33] = b.pop(31)
                b[34] = b.pop(32)
                b[32] = b.pop(30)
                b[26] = b.pop(25)
                b[29] = [f'=COUNT(BF{i}:CK{i})' for i in range(13, height+13)]
                b[30] = ['месяц']*len(b[4])
                b[31] = [f'=AB{i}/Y{i}' for i in range(13, height+13)]
                b[21] = [f'=S{i}' for i in range(13, height+13)]
                b[25] = ['бриф 7ю1']*height
                b[28] = ['1000 показов']*height
                
                b = dict(sorted(b.items(), key=lambda x: x[0]))
                
                b[37] = [f'=IF(OR(X{i}="1000 показов",X{i}="клики",X{i}="engagement",X{i}="вовлечение",X{i}="просмотры"),IF(X{i}="клики",AG{i}*1000/AI{i},IF(OR(X{i}="engagement",X{i}="просмотры",X{i}="вовлечение"),AG{i}*1000/AI{i},AC{i}*AD{i}*(1-AE{i}))),IF(ISERR(AC{i}*AD{i}/AI{i}*1000*(1-AE{i})),0,AC{i}*AD{i}*AB{i}*(1-AE{i})/AI{i}*1000))' for i in range(13, height+13)]
                b[38] = [f'=IF(X{i}="клики",AC{i}*AD{i}*(1-AE{i})*AO{i},IF(OR(X{i}="просмотры",X{i}="engagement",X{i}="вовлечение"),AB{i}*AC{i}*AD{i}*(1-AE{i}),IF(OR(X{i}="пакет",X{i}="неделя",X{i}="день",X{i}="месяц",X{i}="единица",X{i}="единиц"),AC{i}*AD{i}*(1-AE{i})*AB{i},AB{i}*AF{i})))' for i in range(13, height+13)]
                b[39] = [f'=AG{i}*1.2' for i in range(13, height+13)]
                b[40] = [f'=AM{i}/AL{i}' for i in range(13, height+13)]
                b[41] = fr[37]
                b[42] = [f'=AI{i}/AJ{i}' for i in range(13, height+13)]
                b[43] = [f'ОТЧЕТ VTR' for i in range(13, height+13)]
                b[44] = [f'=AB{i}' for i in range(13, height+13)]
                b[45] = [f'CTR' for i in range(13, height+13)]
                b[46] = [f'=AI{i}*AN{i}' for i in range(13, height+13)]
                b[47] = [f'=AG{i}/AI{i}*1000' for i in range(13, height+13)]
                b[48] = [f'=AG{i}/AK{i}*1000' for i in range(13, height+13)]
                b[49] = [f'=AG{i}/AM{i}' for i in range(13, height+13)]
                b[50] = [f'=AG{i}/AO{i}' for i in range(13, height+13)]
                b[51] = [f'отчеты кол лид' for i in range(13, height+13)]
                b[52] = [f'=AG{i}/AT{i}' for i in range(13, height+13)]
                
                u=pd.DataFrame(b)
                
                wb = openpyxl.load_workbook(filename=os.path.join(hol, "media/pattern/медиаплан.xlsx"))
                w = wb.worksheets[0]
                sheet = wb.active
                
                for r in dataframe_to_rows(u, index=None, header=None):
                    w.append(r)
                
                formula = '1000 показов, клики, пакет, просмотры, engagement, вовлечение, неделя, месяц, единица, единиц, день'
                dv = DataValidation(type='list', formula1='"{}"'.format(formula), allow_blank=True)
                sheet.add_data_validation(dv)
                dv.add(f'X13:X{height+12}')
                
                formula1 = 'день, дней, дня, неделя, недели, недель, месяц, месяца, месяцев, единица, единиц, единицы'
                dv = DataValidation(type='list', formula1='"{}"'.format(formula1), allow_blank=True)
                sheet.add_data_validation(dv)
                dv.add(f'Z13:Z{height+12}')
                
                sheet['T2'] = bd.client
                sheet['T3'] = bd.product
                sheet['T4'] = bd.posad
                sheet['T5'] = bd.gender + ", " + bd.age + ", " + bd.interes
                sheet['T6'] = bd.country + ", " + bd.region
                sheet['T7'] = bd.KPI
                
                for row in list(sheet)[12:]:
                    for cell in row:
                        cell.border = Border(top = Side(border_style='thin', color='FF000000'),
                            right = Side(border_style='thin', color='FF000000'),
                            bottom = Side(border_style='thin', color='FF000000'),
                            left = Side(border_style='thin', color='FF000000')) 
                sheet[f'AE{height+13}'] = 'Итого:'
                sheet[f'AF{height+13}'] = f'=SUMIF(AI13:AI{height+12},">0",AG13:AG{height+12})/AI{height+13}*1000'
                sheet[f'AG{height+13}'] = f'=SUM(AG13:AG{height+12})'
                sheet[f'AH{height+13}'] = f'=SUM(AH13:AH{height+12})'
                sheet[f'AI{height+13}'] = f'=SUM(AI13:AI{height+12})'
                sheet[f'AJ{height+13}'] = f'=SUMIF(AK13:AK{height+12},">0",AI13:AI{height+12})/AK{height+13}'
                sheet[f'AK{height+13}'] = f'=SUM(AK13:AK{height+12})*0.8'
                sheet[f'AL{height+13}'] = f'=SUMIF(AI13:AI{height+12},">0",AM13:AM{height+12})/AI{height+13}'
                sheet[f'AM{height+13}'] = f'=SUM(AM13:AM{height+12})'
                sheet[f'AN{height+13}'] = f'=SUMIF(AI13:AI{height+12},">0",AO13:AO{height+12})/AI{height+13}'
                sheet[f'AO{height+13}'] = f'=SUM(AO13:AO{height+12})'
                sheet[f'AP{height+13}'] = f'=SUMIF(AI13:AI{height+12},">0",AG13:AG{height+12})/AI{height+13}*1000'
                sheet[f'AQ{height+13}'] = f'=SUMIF(AK13:AK{height+12},">0",AG13:AG{height+12})/AK{height+13}*1000'
                sheet[f'AR{height+13}'] = f'=SUMIF(AM13:AM{height+12},">0",AG13:AG{height+12})/AM{height+13}'
                sheet[f'AS{height+13}'] = f'=SUMIF(AO13:AO{height+12},">0",AG13:AG{height+12})/AO{height+13}'
                sheet[f'AT{height+13}'] = f'=SUM(AT13:AM{height+12})'
                sheet[f'AU{height+13}'] = f'=SUMIF(AT13:AT{height+12},">0",AG13:AG{height+12})/AT{height+13}'
                sheet[f'AV{height+13}'] = f'=SUMIF(AU13:AU{height+12},">0",AG13:AG{height+12})/AU{height+13}'
                sheet[f'AC{height+14}'] = 'Сервис DCM'
                sheet[f'AC{height+15}'] = 'Итого медиа бюджет'
                sheet[f'AC{height+16}'] = 'АК'
                sheet[f'AC{height+17}'] = 'НДС'
                sheet[f'AC{height+18}'] = 'Производство ролика, с НДС'
                sheet[f'AC{height+19}'] = 'Итого (с учётом НДС и АК)'
                sheet[f'AF{height+16}'] = bd.AK
                sheet[f'AF{height+17}'] = '20%'
                
                sheet[f'AG{height+14}'] = f'=(AI{height+13}*2.5)*1.5/1000'
                sheet[f'AG{height+15}'] = f'=SUM(AG{height+13}:AG{height+14})'
                sheet[f'AG{height+16}'] = f'=AG{height+15}*AF{height+16}'
                sheet[f'AG{height+17}'] = f'=((AG{height+15})+AG{height+16})*AF{height+17}'
                sheet[f'AG{height+18}'] = '0.00р'
                sheet[f'AG{height+19}'] = f'=SUM(AG{height+15}:AG{height+18})'
                
                font = Font(color="FFFFFFFF")
                HeaderFill = PatternFill(start_color='00b050', end_color='00b050', fill_type='solid')
                for row in sheet[f'Q{height+13}':f'AV{height+13}']:
                    for cell in row:
                        cell.fill = HeaderFill
                        cell.font = font
                for row in sheet[f'AC{height+19}':f'AF{height+19}']:
                    for cell in row:
                        cell.border = Border(
                            bottom = Side(border_style='thin', color='FF000000'))
                for row in sheet[f'AC{height+14}':f'AC{height+19}']:
                    for cell in row:
                        cell.border = Border(
                            left = Side(border_style='thin', color='FF000000'))
    
                for row in sheet[f'AG{height+14}':f'AG{height+19}']:
                    for cell in row:
                        cell.border = Border(top = Side(border_style='thin', color='FF000000'),
                            right = Side(border_style='thin', color='FF000000'),
                            bottom = Side(border_style='thin', color='FF000000'),
                            left = Side(border_style='thin', color='FF000000')) 
                for row in list(sheet[f'AG13':f'AG{height+19}']+sheet[f'AC13':f'AC{height+13}']
                                +sheet[f'AH13':f'AH{height+13}']+sheet[f'AP13':f'AP{height+13}']
                                +sheet[f'AQ13':f'AQ{height+13}']+sheet[f'AR13':f'AR{height+13}']
                                +sheet[f'AS13':f'AS{height+13}']+sheet[f'AU13':f'AU{height+13}']):
                    for cell in row:
                        cell.number_format = '###0,00"р."'
                ''' Сезонники и баинг
                season2 = {}
                for i in range(48, 103):
                    if sheet.cell(row=10, column=i).value!=None:
                        season2[sheet.cell(row=10, column=i).value] = i
                for i in range(13, len(season)+13):
                    if season[i-13]=='проверить' or season[i-13]=='нет':
                        pass
                    else:
                        f = season2[season[i-13]]
                        for k in range(5):
                            sheet.cell(row=i, column=f+k).fill = PatternFill(start_color='00b050', end_color='00b050', fill_type='solid')
                ''' 
                
                wb.save(os.path.join(hol, f"media/clients/{username}/{client}/mp_{name_rk}.xlsx"))
                
                

                path = join('clients', username, client, f'DMP_{name_rk}.xlsx')
                path3 = join('clients', username, client, f'mp_{name_rk}.xlsx')
                
                count = All_file.objects.create(username=username, client=client,
                                      name_rk=name_rk, dmp=path, brief=path2,
                                      mp=path3)
                return calculate(request, pk=count.id)
                

        return render(request, self.template_name, data)
    

def calculate(request, pk):
    if request.user.is_authenticated:
       username = request.user.username
       data = {
           'file': All_file.objects.get(pk=pk)
           }
       return render(request, 'prepare_calculation/calculate.html', data)
    


class Download_calc(TemplateView):
    template_name = 'download_calc.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            data = {
                'files': Client.objects.filter(username=username)[::-1],
                'name_client': Brief.objects.filter(username=username)[::-1],
                'list_RK': Brief.objects.filter(username=username)[::-1],
                'form': ClientForm,
                }
            if request.method == 'POST':
                client = request.POST.get('name_client')
                title_rk = request.POST.get('title_rk')
                form = ClientForm(request.POST, request.FILES)
                if form.is_valid():
                    ex = request.FILES.get('calculation')
                    Client.objects.create(username=username, calculation=ex,
                                              client=client, name_rk=title_rk)
                    return render(request, self.template_name, data)  
                else:
                    messages.error(request, f'ERROR: Format of uploaded file: {ex.name} is NOT supported !')
            else:
                form = ClientForm
            data['form'] = form
        return render(request, self.template_name, data)


    
def not_cleared(request, name_rk):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            m = All_file.objects.filter(name_rk=name_rk)[::-1][0]
            data = {
                'client': m.client,
                'mp': m.mp,
                'brief': m.brief,
                'form': CommentForm(initial={
                    'name_rk': name_rk,
                    'comments': m.comments,
                        }),
                }
            if request.method == 'POST':
                form = CommentForm(request.POST or None)
                if form.is_valid():
                    ex = request.FILES.get('presentation')
                    mp = request.FILES.get('mp')
                    comment = request.POST.get('comments')
                    rk = request.POST.get('name_rk')
                    if name_rk!=rk:
                        try:
                            d = Cleared.objects.get(username=username, mp=m.mp,
                                                  client=m.client)
                            d.name_rk = rk
                            d.save()
                        except:
                            m.name_rk = rk
                            m.save()
                            h = Client.objects.filter(username=username, mp=m.mp)[0]
                            h.name_rk = rk
                            h.save()
                    if ex==None and mp!=None:
                        try:
                            d = Cleared.objects.get(username=username, name_rk=name_rk,
                                              client=m.client)
                            m.name_rk = rk
                            m.mp = mp
                            m.comments = comment
                            m.save()
                            d.mp = mp
                            d.save()
                        except:
                            data['error'] = 'Заполните все поля'
                            return render(request, 'but_not_cleared.html', data)
                   
                    elif mp==None and ex==None:
                        try:
                            d = Cleared.objects.get(username=username, name_rk=name_rk,
                                                  client=m.client)
                            m.name_rk = rk
                            m.comments = comment
                            m.save()
                        except:
                            data['error'] = 'Заполните все поля'
                            return render(request, 'but_not_cleared.html', data)
                    else:
                        m.name_rk = rk
                        m.presentation = ex
                        m.comments = comment
                        m.save()
                        b = Brief.objects.filter(name_rk=name_rk)[::-1][0]
                        try:
                            d = Cleared.objects.get(username=username, mp=m.mp,
                                                  client=m.client)
                            d.name_rk = rk
                            d.mp = mp
                            d.save()
                        except ObjectDoesNotExist:
                            Cleared.objects.create(username=username, name_rk=name_rk,
                                          client=m.client, mp=m.mp, landing=b.posad)

                    h = Client.objects.filter(username=username, name_rk=name_rk)[0]
                    h.comments = comment
                    h.save()
                return main(request)
            return render(request, 'but_not_cleared.html', data)
        except IndexError:
            pass
        
   
    
def cleared(request, name_rk):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            f = Cleared.objects.get(username=username,
                                                 name_rk=name_rk)
            data = {
               'file': f,
               'report': Report.objects.all(),
               'form2': CommentForm,
               'form1': ClearForm(initial={
                   'name_rk': name_rk,
                   'comments': f.comments,
                   'landing': f.landing,
                   'access': f.access
                       }),
               }
            if request.method=='POST' and 'form1' in request.POST:
                form1 = ClearForm(request.POST or None)
                if form1.is_valid():
                    mp = request.FILES.get('mp')
                    comments = request.POST.get('comments')
                    rk = request.POST.get('name_rk')
                    landing = request.POST.get('landing')
                    access = request.POST.get('access')
                    if mp==None:
                        f.name_rk = rk
                        f.comments = comments
                        f.landing = landing
                        f.access = access
                        f.save()
                    else:
                        f.name_rk = rk
                        f.mp = mp
                        f.comments = comments
                        f.save()
            if request.method=='POST' and 'form2' in request.FILES:
                form2 = CommentForm(request.FILES)
                if form2.is_valid():
                    report = request.FILES.get('report')
                    a = All_file.objects.get(username=username,
                                                     name_rk=name_rk)
                    a.report = report
                    a.save()
                
            return render(request, 'but_cleared.html', data)
        except ObjectDoesNotExist:
            return main(request)
    
def utm(request, name_rk):
    if request.user.is_authenticated:
        username = request.user.username
        data = {
           'file': name_rk,
           }
        return render(request, 'utm.html', data)
   
def materials(request, name_rk):
    if request.user.is_authenticated:
        username = request.user.username
        data = {
           'file': name_rk,
           }
        return render(request, 'materials.html', data)
   
def complete(request, name_rk):
    if request.user.is_authenticated:
        username = request.user.username
        f = Brief.objects.filter(username=username,
                               name_rk=name_rk)[::-1][0]
        try:
            Complete.objects.get(username=username, name_rk=name_rk,
                                 client=f.client)
        except ObjectDoesNotExist:
            Complete.objects.create(username=username, name_rk=name_rk,
                                      client=f.client, budget=f.budget,
                                      period_c=f.period_c, period_p=f.period_p)
        except MultipleObjectsReturned:
            pass
        
           
        return main(request)