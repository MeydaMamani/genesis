# Generated by Django 4.2.13 on 2024-11-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0009_cnv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnv',
            name='institucion',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]