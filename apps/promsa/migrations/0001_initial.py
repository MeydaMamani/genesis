# Generated by Django 4.2.13 on 2024-10-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dit001_ac_n',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('cod_dep', models.CharField(blank=True, max_length=10, null=True)),
                ('departamento', models.CharField(blank=True, max_length=70, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=10, null=True)),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=10, null=True)),
                ('distrito', models.CharField(blank=True, max_length=150, null=True)),
                ('cod_eess', models.CharField(blank=True, max_length=10, null=True)),
                ('eess', models.CharField(blank=True, max_length=300, null=True)),
                ('participante', models.IntegerField(blank=True, null=True)),
                ('taller', models.CharField(blank=True, max_length=500, null=True)),
                ('subproduct', models.CharField(blank=True, max_length=500, null=True)),
                ('reg', models.IntegerField(blank=True, null=True)),
                ('den', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]