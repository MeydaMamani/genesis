# Generated by Django 4.2.13 on 2024-11-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0005_plano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='fmodific',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='plano',
            name='fregistro',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
