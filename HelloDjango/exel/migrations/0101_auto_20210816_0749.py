# Generated by Django 3.2.2 on 2021-08-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0100_auto_20210816_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='client',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='name_rk',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]