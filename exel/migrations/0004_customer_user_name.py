# Generated by Django 3.2.3 on 2021-05-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0003_remove_customer_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
