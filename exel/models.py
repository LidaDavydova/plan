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

def content_file(instance, filename):
    return '/'.join(['clients', instance.bying_username, filename])

class Profile(models.Model):
    agency = models.CharField(max_length = 60)
    bying_username = models.CharField(max_length = 60)
    manager_username = models.CharField(max_length = 60)
    report_common = models.FileField(upload_to = content_file, null=True)

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

class Client(models.Model):
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 50)
    calculation = models.FileField('???????? ??????????????', upload_to = content_file_name, null=True)
    name_rk = models.CharField(max_length = 200)
    duploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    comments = models.TextField(null=True)

class Report_common(models.Model):
    agency = models.CharField(max_length = 100, null=True)
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
    agency = models.CharField(max_length = 100, null=True)
    file = models.FileField(upload_to ='pattern')

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




def content(instance, img):
    return '/'.join(['clients', 'img', instance.username, img])

class Brief(models.Model):
    agency = models.CharField(max_length = 100, null=True)
    duploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length = 60)
    client = models.CharField(max_length = 100)
    product = models.CharField(max_length = 100, null=True)
    name_rk = models.CharField(max_length = 200, null=True)
    posad = models.CharField(max_length = 300, null=True)
    description = models.CharField(max_length = 500, null=True)
    competitors = models.CharField(max_length = 500, null=True)
    type_act = models.CharField(max_length = 60, null=True)
    country = models.CharField(max_length = 60, null=True)
    region = models.CharField(max_length = 100, null=True)
    ca = models.CharField(max_length = 150, null=True)
    gender = models.CharField(max_length = 20, null=True)
    age = models.CharField(max_length = 10, null=True)
    interes = models.TextField(null=True)
    income = models.CharField(max_length = 30, null=True)
    rek = models.TextField(null=True)
    materials = models.CharField(max_length = 60, null=True)
    duration1 = models.CharField(max_length = 30, null=True)
    duration2 = models.CharField(max_length = 30, null=True)
    duration3 = models.CharField(max_length = 30, null=True)
    period_c = models.CharField(max_length = 10)
    period_p = models.CharField(max_length = 10)
    KPI = models.CharField(max_length = 60, null=True)
    plan = models.TextField(null=True)
    budget = models.CharField(max_length = 30, null=True)
    who_prep_materials = models.CharField(max_length = 300, null=True)
    discount = models.CharField(max_length = 10, null=True)
    AK = models.CharField(max_length = 20, null=True)
    DCM = models.CharField(max_length = 20, null=True)
    img = models.ImageField('??????????????', upload_to=content)


class Bying(models.Model):
    agency = models.CharField(max_length = 100, null=True)
    sell = models.CharField(max_length = 100, null=True)
    site = models.CharField(max_length = 100, null=True)
    plan = models.CharField(max_length = 100, null=True)
    phact = models.CharField(max_length = 100, null=True)
    procent = models.CharField(max_length = 10, null=True)


class Dmp_priority(models.Model):
    agency = models.CharField(max_length = 100, null=True)
    sell = models.CharField(max_length = 100, null=True)
    site = models.CharField(max_length = 100, null=True)
