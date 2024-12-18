# Generated by Django 4.2.13 on 2024-10-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promsa', '0011_met017_met_cr_met017_met_n'),
    ]

    operations = [
        migrations.CreateModel(
            name='cc',
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
                ('documento', models.CharField(blank=True, max_length=15, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('fec_atencion', models.DateField(blank=True, null=True)),
                ('reg_manual', models.CharField(blank=True, max_length=150, null=True)),
                ('subproduct', models.CharField(blank=True, max_length=500, null=True)),
                ('observacion', models.CharField(blank=True, max_length=500, null=True)),
                ('den', models.IntegerField(blank=True, null=True)),
                ('num', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
