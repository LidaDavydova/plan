# Generated by Django 3.2.4 on 2021-07-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0017_auto_20210702_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='file',
            field=models.FileField(upload_to='client'),
        ),
    ]
