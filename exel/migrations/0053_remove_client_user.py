# Generated by Django 3.2.4 on 2021-07-18 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0052_alter_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]
