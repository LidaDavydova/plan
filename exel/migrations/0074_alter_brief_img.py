# Generated by Django 3.2.4 on 2021-07-27 06:05

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0073_alter_all_file_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='img',
            field=models.FileField(upload_to=exel.models.content, verbose_name='Изображение'),
        ),
    ]
