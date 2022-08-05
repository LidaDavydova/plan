# Generated by Django 3.2.10 on 2022-04-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0114_brief_ca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='KPI',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='budget',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='ca',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='competitors',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='country',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='income',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='interes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='materials',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='name_rk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='plan',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='posad',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='product',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='rek',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='type_act',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='brief',
            name='who_prep_materials',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
