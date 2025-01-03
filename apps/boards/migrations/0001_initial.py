# Generated by Django 4.2.13 on 2024-12-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fedgestante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_dep', models.CharField(blank=True, max_length=5, null=True)),
                ('departamento', models.CharField(blank=True, max_length=30, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=5, null=True)),
                ('provincia', models.CharField(blank=True, max_length=40, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=8, null=True)),
                ('distrito', models.CharField(blank=True, max_length=80, null=True)),
                ('anio', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('nombremes', models.CharField(blank=True, max_length=10, null=True)),
                ('si04', models.CharField(blank=True, max_length=5, null=True)),
                ('si01', models.CharField(blank=True, max_length=5, null=True)),
                ('vi0101', models.CharField(blank=True, max_length=5, null=True)),
                ('vi0102', models.CharField(blank=True, max_length=5, null=True)),
                ('vii01', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fedninio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_dep', models.CharField(blank=True, max_length=5, null=True)),
                ('departamento', models.CharField(blank=True, max_length=30, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=5, null=True)),
                ('provincia', models.CharField(blank=True, max_length=40, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=8, null=True)),
                ('distrito', models.CharField(blank=True, max_length=80, null=True)),
                ('anio', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('nombremes', models.CharField(blank=True, max_length=10, null=True)),
                ('pqtrn', models.CharField(blank=True, max_length=5, null=True)),
                ('si0201', models.CharField(blank=True, max_length=5, null=True)),
                ('si0202', models.CharField(blank=True, max_length=5, null=True)),
                ('si0203', models.CharField(blank=True, max_length=5, null=True)),
                ('si03', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
