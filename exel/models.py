from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
import pandas as pd
import numpy as np
import math
from django.db.models.signals import pre_delete
from django.core.files.base import ContentFile
import openpyxl
from openpyxl.styles import Alignment, Border, Side, PatternFill
from openpyxl import load_workbook


def materials(instance, file):
    return '/'.join(['clients', 'materials', instance.username, instance.client, file])

def content_file_name(instance, filename):
    return '/'.join(['clients', instance.username, instance.client, filename])


class Feed(models.Model):
    name_rk = models.CharField(max_length = 200)
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 50)

class FeedFile(models.Model):
    file = models.FileField(upload_to="clients/materials/%Y/%m/%d")
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)

class Complete(models.Model):
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 50)
    name_rk = models.CharField(max_length = 200)
    budget = models.CharField(max_length = 30)
    period_c = models.CharField(max_length = 10)
    period_p = models.CharField(max_length = 10)

class Cleared(models.Model):
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 50)
    name_rk = models.CharField(max_length = 200)
    mp = models.FileField(upload_to = content_file_name, null=True)
    comments = models.TextField(null=True)
    access = models.TextField(null=True)
    landing = models.CharField(max_length = 60, null=True)
    utm = models.FileField(upload_to = content_file_name, null=True)

class All_file(models.Model):
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 50)
    name_rk = models.CharField(max_length = 200)
    dmp = models.FileField(upload_to = content_file_name, null=True)
    brief = models.FileField(upload_to = content_file_name, null=True)
    report = models.FileField(upload_to = content_file_name, null=True)
    presentation = models.FileField(upload_to = content_file_name, null=True)
    comments = models.TextField(null=True)
    mp = models.FileField(upload_to = content_file_name, null=True)
    
    def create_mp(self):
        dmp = f"media\clients\{self.username}\{self.client}\DMP_{self.name_rk}.xlsx"
        p = pd.read_excel(dmp, header=0)
        w = openpyxl.load_workbook(filename=dmp, data_only=True)
        max_row = w.get_highest_row()
        max_col = w.get_highest_column()

class Client(models.Model):
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 50)
    calculation = models.FileField('Файл расчета', upload_to = content_file_name, null=True)
    name_rk = models.CharField(max_length = 200)
    duploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    comments = models.TextField(null=True)
    
    def __str__(self):
        return self.file.name
    

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
        
    def save_excel(self, dataframe):
        if self.file.name.lower().endswith(('.xlsx', '.xls')):
            excelWriter = pd.ExcelWriter(self.file.path)
            dataframe.to_excel(excelWriter, index=False)
            excelWriter.save()
        else:
            dataframe.to_csv(self.file.path, index=False)

class Report_common(models.Model):
    file = models.FileField(upload_to ='pattern')

    def __str__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Report_common.objects.get(pk=self.pk)
            if old_self.file and self.file != old_self.file:
                old_self.file.delete(False)
        return super(Report_common, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

class Media_plan(models.Model):
    file = models.FileField(upload_to ='pattern')

    def __str__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Media_plan.objects.get(pk=self.pk)
            if old_self.file and self.file != old_self.file:
                old_self.file.delete(False)
        return super(Media_plan, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

class Report(models.Model):
    file = models.FileField(upload_to ='pattern')

    def __str__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Report.objects.get(pk=self.pk)
            if old_self.file and self.file != old_self.file:
                old_self.file.delete(False)
        return super(Report, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
        
class Brief_pattern(models.Model):
    file = models.FileField(upload_to ='pattern')

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Brief_pattern.objects.get(pk=self.pk)
            if old_self.file and self.file != old_self.file:
                old_self.file.delete(False)
        return super(Brief_pattern, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
        

class Dmp(models.Model):
    file = models.FileField(upload_to ='pattern')
    corrected = models.BooleanField(default=False) # pandas correction status
    file_content = models.BooleanField(default=False) # df required columns checker

    def __str__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Dmp.objects.get(pk=self.pk)
            if old_self.file and self.file != old_self.file:
                old_self.file.delete(False)
        return super(Dmp, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def save_excel(self, dataframe):
        if self.file.name.lower().endswith(('.xlsx', '.xls')):
            excelWriter = pd.ExcelWriter(self.file.path)
            dataframe.to_excel(excelWriter, index=False)
            excelWriter.save()
        else:
            dataframe.to_csv(self.file.path, index=False)
        

    def odo(self):
        if self.file.name.lower().endswith(('.xlsx', '.xls')):
            df = pd.read_excel(self.file.path)
        else:
            df = pd.read_csv(self.file.path)

        df.loc[:,"ODOMETER_FW"] = df.loc[:,"ODOMETER_FW"].fillna(0).astype('int')
        df.dropna(inplace = True)
        df.sort_values(by=['VEHICLE_ID_FW','TRANSACTION_DATE_FW','TRANSACTION_TIME_FW'], ascending=[True,False,False],inplace=True)
        df['ODOMETER_FW'] = df['ODOMETER_FW'].apply(lambda x: 0 if x <1000 else x)
        df.set_index(['VEHICLE_ID_FW'], inplace=True)
        ids = df.index.unique().tolist() #create of unique Vehicle IDs list
        df_corrected = pd.DataFrame() #create new df to store corrected data from dawnloaded df
        
        for i in ids: #odo correction and storing data in df_corrected
            temp_df = df.loc[i]
            odo = df.loc[i,"ODOMETER_FW"].tolist()
            if type(odo) == list:
                odo.sort(reverse=True)   
                for j in range(len(odo)-1):
                    if abs(odo[j] - odo[j+1]) > 9999 or odo[j] - odo[j+1] < 0:
                        odo[j+1] = 0    
                temp_df.loc[:,"ODOMETER_FW"] = odo #temp_df["ODOMETER_FW"] = odo
                df_corrected = df_corrected.append(temp_df)
            else:
                df_corrected = df_corrected.append(temp_df)
                
        df_corrected.reset_index(inplace=True)
        df_corrected.rename(columns = {'index':'VEHICLE_ID_FW'}, inplace = True)
        return df_corrected


    def columns_check(self): # columns check
        if self.file.name.lower().endswith(('.xlsx', '.xls')):
            df = pd.read_excel(self.file.path)
        else:
            df = pd.read_csv(self.file.path)

        cols_in_files = [col for col in df.columns]
        mandatory_cols = ['TRANSACTION_DATE_FW','TRANSACTION_TIME_FW','VEHICLE_ID_FW','ODOMETER_FW']
        for col in mandatory_cols:
            if col in cols_in_files:
                pass
            else:
                return self.file_content        
        self.file_content = True
        return self.file_content
    

def content(instance, img):
    return '/'.join(['clients', 'img', instance.username, img])
    
class Brief(models.Model):
    duploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 100)
    product = models.CharField(max_length = 100)
    name_rk = models.CharField(max_length = 200)
    posad = models.CharField(max_length = 300)
    description = models.CharField(max_length = 500)
    competitors = models.CharField(max_length = 500)
    type_act = models.CharField(max_length = 60)
    country = models.CharField(max_length = 60)
    region = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 20)
    age = models.CharField(max_length = 10)
    interes = models.TextField()
    income = models.CharField(max_length = 30)
    rek = models.TextField()
    materials = models.CharField(max_length = 60)
    duration1 = models.CharField(max_length = 30, null=True)
    duration2 = models.CharField(max_length = 30, null=True)
    duration3 = models.CharField(max_length = 30, null=True)
    period_c = models.CharField(max_length = 10)
    period_p = models.CharField(max_length = 10)
    KPI = models.CharField(max_length = 60)
    plan = models.TextField()
    budget = models.CharField(max_length = 30)
    who_prep_materials = models.CharField(max_length = 300)
    discount = models.CharField(max_length = 10, null=True)
    AK = models.CharField(max_length = 20, null=True)
    DCM = models.CharField(max_length = 20, null=True)
    img = models.ImageField('Логотип', upload_to=content)
    

    
class Bying(models.Model):
    sell = models.CharField(max_length = 100, null=True)
    site = models.CharField(max_length = 100, null=True)
    plan = models.CharField(max_length = 100, null=True)
    phact = models.CharField(max_length = 100, null=True)
    procent = models.CharField(max_length = 10, null=True)
    