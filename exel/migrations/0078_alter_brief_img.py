# Generated by Django 3.2.4 on 2021-07-27 06:12

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0077_alter_brief_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='img',
            field=models.ImageField(upload_to=exel.models.content, verbose_name='Логотип'),
        ),
    ]
