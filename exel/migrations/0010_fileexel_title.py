# Generated by Django 3.2.3 on 2021-05-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0009_fileexel'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileexel',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]