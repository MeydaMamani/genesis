from django.db import models

# Create your models here.
class dit001_ac_n(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    participante = models.IntegerField(blank=True, null=True)
    taller = models.CharField(max_length=500, blank=True, null=True)
    subproduct = models.CharField(max_length=500, blank=True, null=True)
    reg = models.CharField(max_length=10, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)

    # def natural_key(self):
    #     return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
    #            self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.eess, \
    #            self.ult_eess, self.documento, self.programa,\
    #            self.programa, self.den, self.num

    # def __str__(self):
    #     return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class mat002_vg_n(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    fec_atencion = models.DateField(blank=True, null=True)
    lab = models.CharField(max_length=10, blank=True, null=True)
    reg = models.CharField(max_length=10, blank=True, null=True)
    trimestre = models.CharField(max_length=50, blank=True, null=True)
    trazador = models.IntegerField(blank=True, null=True)
    subproduct = models.CharField(max_length=500, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class mat002_vg_c(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class mat002_vg_cr(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    primer_trim = models.DateField(blank=True, null=True)
    segundo_trim = models.DateField(blank=True, null=True)
    tercer_trim = models.DateField(blank=True, null=True)
    trazador = models.IntegerField(blank=True, null=True)
    fur = models.DateField(blank=True, null=True)
    fpp = models.DateField(blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class mat002_dc_n(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    eje = models.CharField(max_length=100, blank=True, null=True)
    taller = models.CharField(max_length=400, blank=True, null=True)
    subproduct = models.CharField(max_length=500, blank=True, null=True)
    reg = models.CharField(max_length=10, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class dit001_fng_n(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_atencion = models.DateField(blank=True, null=True)
    edad_reg = models.IntegerField(blank=True, null=True)
    tedad = models.CharField(max_length=5, blank=True, null=True)
    subproduct = models.CharField(max_length=500, blank=True, null=True)
    reg = models.CharField(max_length=10, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class mat002_vp_n(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    fec_atencion = models.DateField(blank=True, null=True)
    visita = models.IntegerField(blank=True, null=True)
    trazador = models.CharField(max_length=100, blank=True, null=True)
    reg = models.CharField(max_length=15, blank=True, null=True)
    subproduct = models.CharField(max_length=500, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class mat002_vp_cr(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    visita1 = models.DateField(blank=True, null=True)
    visita2 = models.DateField(blank=True, null=True)
    visita3 = models.DateField(blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


