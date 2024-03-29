# Generated by Django 4.1.7 on 2023-04-01 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presup', '0004_suplidor_alter_material_alias_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_Analisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(default=0)),
                ('fecha', models.DateField(blank=True, default='', null=True)),
                ('marca', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presup.material')),
                ('suplidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presup.suplidor')),
            ],
        ),
    ]
