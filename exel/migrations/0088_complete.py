# Generated by Django 3.2.4 on 2021-08-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0087_auto_20210805_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('client', models.CharField(max_length=50)),
                ('name_rk', models.CharField(max_length=200)),
            ],
        ),
    ]
