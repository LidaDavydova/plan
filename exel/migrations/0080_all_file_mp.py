# Generated by Django 3.2.4 on 2021-07-28 05:58

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0079_auto_20210727_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_file',
            name='mp',
            field=models.FileField(null=True, upload_to=exel.models.content_file_name),
        ),
    ]