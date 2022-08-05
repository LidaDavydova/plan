# Generated by Django 3.2.4 on 2021-07-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0016_remove_excel_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel/clients')),
                ('client', models.CharField(max_length=50)),
                ('duploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Fileexel',
        ),
        migrations.RemoveField(
            model_name='brief',
            name='name_client',
        ),
    ]
