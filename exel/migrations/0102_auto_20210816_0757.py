# Generated by Django 3.2.2 on 2021-08-16 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0101_auto_20210816_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedfile',
            name='file',
            field=models.FileField(upload_to='clients/materials/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
