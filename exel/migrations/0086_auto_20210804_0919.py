# Generated by Django 3.2.4 on 2021-08-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0085_auto_20210803_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brief',
            old_name='duration',
            new_name='duration1',
        ),
        migrations.AddField(
            model_name='brief',
            name='duration2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='duration3',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
