# Generated by Django 3.2.4 on 2021-07-21 05:19

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0061_auto_20210721_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_file_cl',
            name='dmp',
            field=models.FileField(upload_to=exel.models.content_file_name),
        ),
    ]
