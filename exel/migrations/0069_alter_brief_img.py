# Generated by Django 3.2.4 on 2021-07-22 11:00

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0068_alter_brief_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=exel.models.content),
        ),
    ]
