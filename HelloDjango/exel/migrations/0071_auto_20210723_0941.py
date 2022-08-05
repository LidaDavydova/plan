# Generated by Django 3.2.4 on 2021-07-23 06:41

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0070_alter_brief_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('client', models.CharField(max_length=50)),
                ('name_rk', models.CharField(max_length=100)),
                ('dmp', models.FileField(null=True, upload_to=exel.models.content_file_name)),
                ('brief', models.FileField(null=True, upload_to=exel.models.content_file_name)),
                ('report', models.FileField(null=True, upload_to=exel.models.content_file_name)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='brief',
        ),
        migrations.RemoveField(
            model_name='client',
            name='dmp',
        ),
        migrations.RemoveField(
            model_name='client',
            name='report',
        ),
    ]
