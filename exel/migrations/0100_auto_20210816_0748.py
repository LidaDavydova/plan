# Generated by Django 3.2.2 on 2021-08-16 04:48

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0099_rename_user_feed_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='text',
        ),
        migrations.AlterField(
            model_name='feedfile',
            name='file',
            field=models.FileField(upload_to=exel.models.materials),
        ),
    ]
