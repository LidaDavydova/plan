# Generated by Django 4.0.3 on 2022-08-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_profile_tt_profile_advantages_profile_budget_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='margins',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
