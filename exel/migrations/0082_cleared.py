# Generated by Django 3.2.4 on 2021-07-30 13:46

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0081_client_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('client', models.CharField(max_length=50)),
                ('name_rk', models.CharField(max_length=100)),
                ('mp', models.FileField(null=True, upload_to=exel.models.content_file_name)),
            ],
        ),
    ]
