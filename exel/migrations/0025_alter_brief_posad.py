# Generated by Django 3.2.4 on 2021-07-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0024_auto_20210706_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='posad',
            field=models.CharField(max_length=300),
        ),
    ]
