# Generated by Django 3.2.4 on 2021-07-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0058_remove_brief_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='brief',
            name='username',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
