# Generated by Django 3.2.4 on 2021-06-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0013_brief_name_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileexel',
            name='date',
        ),
        migrations.AddField(
            model_name='fileexel',
            name='duploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
