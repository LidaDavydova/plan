# Generated by Django 3.2.4 on 2021-07-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0022_auto_20210706_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='brief',
            name='KPI',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
