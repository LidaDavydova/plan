# Generated by Django 3.2.4 on 2021-07-18 08:47

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0050_client_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='client',
            name='file',
            field=models.FileField(upload_to=exel.models.content_file_name),
        ),
    ]
