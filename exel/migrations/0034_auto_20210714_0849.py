# Generated by Django 3.2.4 on 2021-07-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0033_alter_client_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brief',
            name='title',
        ),
        migrations.AlterField(
            model_name='client',
            name='client',
            field=models.CharField(max_length=50),
        ),
    ]
