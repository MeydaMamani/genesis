# Generated by Django 3.2.5 on 2024-02-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redes',
            name='level',
            field=models.CharField(choices=[('1', 'REGION'), ('2', 'PROVINCIA'), ('3', 'DISTRITO')], max_length=1),
        ),
        migrations.AlterField(
            model_name='redes',
            name='state',
            field=models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], max_length=2),
        ),
    ]
