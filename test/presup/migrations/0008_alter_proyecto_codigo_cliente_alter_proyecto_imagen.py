# Generated by Django 4.1.7 on 2023-04-28 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presup', '0007_proyecto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='codigo_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='presup.cliente'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='presup/media/images/'),
        ),
    ]
