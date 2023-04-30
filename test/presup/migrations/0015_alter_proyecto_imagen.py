# Generated by Django 4.1.7 on 2023-04-29 23:42

import django.core.files.storage
from django.db import migrations, models
import presup.models


class Migration(migrations.Migration):

    dependencies = [
        ('presup', '0014_alter_proyecto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to=presup.models.image_directory_path),
        ),
    ]
