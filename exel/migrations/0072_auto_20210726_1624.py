# Generated by Django 3.2.4 on 2021-07-26 13:24

from django.db import migrations, models
import exel.models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0071_auto_20210723_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_file',
            name='comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_file',
            name='presentation',
            field=models.FileField(null=True, upload_to=exel.models.content_file_name),
        ),
    ]
