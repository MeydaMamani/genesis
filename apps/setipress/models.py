from django.db import models

# Create your models here.
class b1(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    periodo = models.CharField(max_length=7, blank=True, null=True)
    cod_dep = models.IntegerField(blank=True, null=True)
    cod_prov = models.CharField(max_length=5, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    cod_ipress = models.CharField(max_length=10, blank=True, null=True)
    cod_ugipress = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    gedad = models.IntegerField(blank=True, null=True)
    aten_med = models.CharField(max_length=10, blank=True, null=True)
    aten_nomed = models.CharField(max_length=10, blank=True, null=True)
    aten_mes = models.CharField(max_length=10, blank=True, null=True)
    cod_dist2 = models.CharField(max_length=10, blank=True, null=True)


class b2(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    periodo = models.CharField(max_length=7, blank=True, null=True)
    cod_dep = models.IntegerField(blank=True, null=True)
    cod_prov = models.CharField(max_length=5, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    cod_ipress = models.CharField(max_length=10, blank=True, null=True)
    cod_ugipress = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    gedad = models.IntegerField(blank=True, null=True)
    dx_def = models.CharField(max_length=10, blank=True, null=True)
    aten = models.CharField(max_length=10, blank=True, null=True)
    cod_dist2 = models.CharField(max_length=10, blank=True, null=True)
