# Generated by Django 3.2.4 on 2021-08-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0103_delete_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pattern')),
            ],
        ),
        migrations.CreateModel(
            name='Report_common',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pattern')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
