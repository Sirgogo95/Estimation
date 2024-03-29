# Generated by Django 4.1.7 on 2023-03-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='id',
        ),
        migrations.AddField(
            model_name='material',
            name='tasa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='material',
            name='alias',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='codigo',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='material',
            name='familias',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
