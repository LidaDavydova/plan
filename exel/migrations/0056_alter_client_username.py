# Generated by Django 3.2.4 on 2021-07-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0055_alter_client_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=60),
        ),
    ]
