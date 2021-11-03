# Generated by Django 3.2.4 on 2021-10-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0111_auto_20211030_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dmp_priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=100, null=True)),
                ('sell', models.CharField(max_length=100, null=True)),
                ('site', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dmp',
            name='corrected',
        ),
        migrations.RemoveField(
            model_name='dmp',
            name='file_content',
        ),
    ]
