# Generated by Django 3.2.5 on 2024-03-30 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed2324', '0003_auto_20240320_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kids12M2Dosages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('anio', models.CharField(blank=True, max_length=5, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_microred', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=10, null=True)),
                ('provincia', models.CharField(blank=True, max_length=150, null=True)),
                ('distrito', models.CharField(blank=True, max_length=150, null=True)),
                ('establecimiento', models.CharField(blank=True, max_length=250, null=True)),
                ('documento', models.CharField(blank=True, max_length=15, null=True)),
                ('ape_nombres', models.CharField(blank=True, max_length=25, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('seguro', models.CharField(blank=True, max_length=5, null=True)),
                ('fec_hb', models.DateField(blank=True, null=True)),
                ('fec_anemia', models.DateField(blank=True, null=True)),
                ('fec_iniTto', models.DateField(blank=True, null=True)),
                ('suple6', models.DateField(blank=True, null=True)),
                ('suple7', models.DateField(blank=True, null=True)),
                ('suple8', models.DateField(blank=True, null=True)),
                ('suple9', models.DateField(blank=True, null=True)),
                ('suple10', models.DateField(blank=True, null=True)),
                ('suple11', models.DateField(blank=True, null=True)),
                ('fec_ta', models.DateField(blank=True, null=True)),
                ('fec_ttoTa', models.DateField(blank=True, null=True)),
                ('fec_hb2', models.DateField(blank=True, null=True)),
                ('den', models.CharField(blank=True, max_length=10, null=True)),
                ('num', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PackChildRn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('anio', models.CharField(blank=True, max_length=5, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_microred', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=10, null=True)),
                ('provincia', models.CharField(blank=True, max_length=150, null=True)),
                ('distrito', models.CharField(blank=True, max_length=150, null=True)),
                ('establecimiento', models.CharField(blank=True, max_length=250, null=True)),
                ('ultAten', models.CharField(blank=True, max_length=400, null=True)),
                ('documento', models.CharField(blank=True, max_length=15, null=True)),
                ('ape_nombres', models.CharField(blank=True, max_length=25, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('fec_hvb', models.DateField(blank=True, null=True)),
                ('fec_bcg', models.DateField(blank=True, null=True)),
                ('fec_tmz', models.DateField(blank=True, null=True)),
                ('fec_cred1', models.DateField(blank=True, null=True)),
                ('fec_cred2', models.DateField(blank=True, null=True)),
                ('fec_cred3', models.DateField(blank=True, null=True)),
                ('fec_cred4', models.DateField(blank=True, null=True)),
                ('den', models.CharField(blank=True, max_length=10, null=True)),
                ('num', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Premature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('anio', models.CharField(blank=True, max_length=5, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_microred', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=10, null=True)),
                ('provincia', models.CharField(blank=True, max_length=150, null=True)),
                ('distrito', models.CharField(blank=True, max_length=150, null=True)),
                ('establecimiento', models.CharField(blank=True, max_length=250, null=True)),
                ('documento', models.CharField(blank=True, max_length=15, null=True)),
                ('ape_nombres', models.CharField(blank=True, max_length=25, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('seguro', models.CharField(blank=True, max_length=5, null=True)),
                ('suple1', models.DateField(blank=True, null=True)),
                ('suple2', models.DateField(blank=True, null=True)),
                ('suple3', models.DateField(blank=True, null=True)),
                ('suple4', models.DateField(blank=True, null=True)),
                ('suple5', models.DateField(blank=True, null=True)),
                ('ta', models.DateField(blank=True, null=True)),
                ('den', models.CharField(blank=True, max_length=10, null=True)),
                ('num', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suple4M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('anio', models.CharField(blank=True, max_length=5, null=True)),
                ('mes', models.CharField(blank=True, max_length=3, null=True)),
                ('cod_prov', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_microred', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_dist', models.CharField(blank=True, max_length=10, null=True)),
                ('provincia', models.CharField(blank=True, max_length=150, null=True)),
                ('distrito', models.CharField(blank=True, max_length=150, null=True)),
                ('establecimiento', models.CharField(blank=True, max_length=250, null=True)),
                ('documento', models.CharField(blank=True, max_length=15, null=True)),
                ('ape_nombres', models.CharField(blank=True, max_length=25, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('seguro', models.CharField(blank=True, max_length=5, null=True)),
                ('suple4', models.DateField(blank=True, null=True)),
                ('suple5', models.DateField(blank=True, null=True)),
                ('ta', models.DateField(blank=True, null=True)),
                ('den', models.CharField(blank=True, max_length=10, null=True)),
                ('num', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='packchild',
            name='cod_dist',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='packchild',
            name='cod_microred',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='packchild',
            name='cod_prov',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teen',
            name='cod_dist',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teen',
            name='cod_microred',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teen',
            name='cod_prov',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
