# Generated by Django 3.2.4 on 2021-07-15 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exel', '0035_rename_materils_brief_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
