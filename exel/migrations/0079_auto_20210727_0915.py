# Generated by Django 3.2.4 on 2021-07-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0078_alter_brief_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='AK',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='DCM',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='discount',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
