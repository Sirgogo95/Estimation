# Generated by Django 4.1.7 on 2023-04-29 19:43

import django.core.files.storage
from django.db import migrations, models
import presup.models


class Migration(migrations.Migration):

    dependencies = [
        ('presup', '0012_alter_proyecto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/presup/media//', location='C:\\Users\\Junior\\Desktop\\GitHub\\Estimation\\test\\presup/media/'), upload_to=presup.models.image_directory_path),
        ),
    ]
