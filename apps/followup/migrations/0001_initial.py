# Generated by Django 4.2.13 on 2024-10-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='padron_nom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_dep', models.CharField(blank=True, max_length=10, null=True)),
                ('departamento', models.CharField(blank=True, max_length=70, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=10, null=True)),
                ('provincia', models.CharField(blank=True, max_length=150, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=10, null=True)),
                ('distrito', models.CharField(blank=True, max_length=150, null=True)),
                ('cod_padron', models.CharField(blank=True, max_length=15, null=True)),
                ('eess', models.CharField(blank=True, max_length=300, null=True)),
                ('ccpp', models.CharField(blank=True, max_length=300, null=True)),
                ('est_tramite', models.CharField(blank=True, max_length=30, null=True)),
                ('fec_tramite', models.DateField(blank=True, null=True)),
                ('tipo_doc', models.CharField(blank=True, max_length=15, null=True)),
                ('cnv_dni', models.CharField(blank=True, max_length=20, null=True)),
                ('nombres_ninio', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('menor_visit', models.CharField(blank=True, max_length=50, null=True)),
                ('menor_encont', models.CharField(blank=True, max_length=10, null=True)),
                ('tseguro', models.CharField(blank=True, max_length=10, null=True)),
                ('tprog_social', models.CharField(blank=True, max_length=20, null=True)),
                ('eje_vial', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True)),
                ('fec_visita', models.DateField(blank=True, null=True)),
                ('fuente', models.CharField(blank=True, max_length=200, null=True)),
                ('eess_nacido', models.CharField(blank=True, max_length=200, null=True)),
                ('eess_adscrip', models.CharField(blank=True, max_length=200, null=True)),
                ('institucion', models.CharField(blank=True, max_length=100, null=True)),
                ('dni_madre', models.CharField(blank=True, max_length=20, null=True)),
                ('nombres_madre', models.CharField(blank=True, max_length=100, null=True)),
                ('celular_madre', models.CharField(blank=True, max_length=30, null=True)),
                ('grado_inst', models.CharField(blank=True, max_length=80, null=True)),
                ('dni_jefe', models.CharField(blank=True, max_length=20, null=True)),
                ('nombres_jefe', models.CharField(blank=True, max_length=100, null=True)),
                ('entidad', models.CharField(blank=True, max_length=100, null=True)),
                ('tregistro', models.CharField(blank=True, max_length=50, null=True)),
                ('est_regist', models.CharField(blank=True, max_length=50, null=True)),
                ('seguro', models.CharField(blank=True, max_length=30, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
