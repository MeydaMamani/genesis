from django.db import models
# Create your models here.

class mc_03(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    eess_nacido = models.CharField(max_length=150, blank=True, null=True)
    ult_eess = models.CharField(max_length=250, blank=True, null=True)
    tipo_doc = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=200, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    tmz = models.DateField(blank=True, null=True)
    bcg = models.DateField(blank=True, null=True)
    hvb = models.DateField(blank=True, null=True)
    ctrl1 = models.DateField(blank=True, null=True)
    ctrl2 = models.DateField(blank=True, null=True)
    ctrl3 = models.DateField(blank=True, null=True)
    ctrl4 = models.DateField(blank=True, null=True)
    visit7d_prom = models.CharField(max_length=70, blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_dep, self.departamento, self.cod_prov, self.provincia,\
               self.cod_dist, self.distrito, self.ult_eess, self.tipo_doc, self.documento, self.ape_nombres,\
               self.fec_nac, self.seguro, self.tmz, self.bcg, self.hvb, self.ctrl1, self.ctrl2, self.ctrl3, self.ctrl4,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.ult_eess)


class si_01(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=150, blank=True, null=True)
    cat_eess = models.CharField(max_length=10, blank=True, null=True)
    ult_eess = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fecha_dx = models.DateField(blank=True, null=True)
    suple1 = models.DateField(blank=True, null=True)
    dosaje = models.DateField(blank=True, null=True)
    suple2 = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.eess, self.cat_eess,\
               self.ult_eess, self.documento, self.fecha_dx, self.suple1, self.dosaje, self.suple2, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class si_0202(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=150, blank=True, null=True)
    ult_eess = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    ape_nombres= models.CharField(max_length=200, blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    dsje6m = models.DateField(blank=True, null=True)
    dx_anemia = models.DateField(blank=True, null=True)
    suple1 = models.DateField(blank=True, null=True)
    suple2 = models.DateField(blank=True, null=True)
    suple2_1 = models.DateField(blank=True, null=True)
    dsje_ctrl1 = models.DateField(blank=True, null=True)
    suple3 = models.DateField(blank=True, null=True)
    suple3_1 = models.DateField(blank=True, null=True)
    dsje3 = models.DateField(blank=True, null=True)
    dsje4 = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    suple6 = models.DateField(blank=True, null=True)
    ta = models.DateField(blank=True, null=True)
    ta_1 = models.DateField(blank=True, null=True)
    dsje_ctrl = models.DateField(blank=True, null=True)
    visista6 = models.DateField(blank=True, null=True)
    visista8 = models.DateField(blank=True, null=True)
    visista9 = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.eess, \
               self.ult_eess, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class si_0203(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=150, blank=True, null=True)
    ult_eess = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=200, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    dsje6m = models.DateField(blank=True, null=True)
    suple1 = models.DateField(blank=True, null=True)
    suple2 = models.DateField(blank=True, null=True)
    dsje2 = models.DateField(blank=True, null=True)
    suple3 = models.DateField(blank=True, null=True)
    dsje3_1 = models.DateField(blank=True, null=True)
    dsje3 = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    suple6 = models.DateField(blank=True, null=True)
    ta = models.DateField(blank=True, null=True)
    dsje12m = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.eess, \
               self.ult_eess, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class si_0401(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_eess = models.CharField(max_length=10, blank=True, null=True)
    eess = models.CharField(max_length=150, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    atendida = models.DateField(blank=True, null=True)
    fec_hb = models.DateField(blank=True, null=True)
    suple = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.cod_eess, self.eess, \
               self.categoria, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class vii_0101(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    eess_apn= models.CharField(max_length=150, blank=True, null=True)
    eess_dx= models.CharField(max_length=150, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    diagnostico = models.DateField(blank=True, null=True)
    dx_3m = models.DateField(blank=True, null=True)
    dx_6m = models.DateField(blank=True, null=True)
    csm1 = models.DateField(blank=True, null=True)
    csm2 = models.DateField(blank=True, null=True)
    psicologia1 = models.DateField(blank=True, null=True)
    psicologia2 = models.DateField(blank=True, null=True)
    psicologia3 = models.DateField(blank=True, null=True)
    psicologia4 = models.DateField(blank=True, null=True)
    psicologia5 = models.DateField(blank=True, null=True)
    psicologia6 = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, \
               self.categoria, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class vi_0101(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    eess= models.CharField(max_length=150, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    trimestre= models.CharField(max_length=20, blank=True, null=True)
    fecha_apn = models.DateField(blank=True, null=True)
    tmz = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.categoria, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class vi_0102(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    eess= models.CharField(max_length=150, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    gest_tmz = models.DateField(blank=True, null=True)
    trimestre = models.CharField(max_length=10, blank=True, null=True)
    tmz = models.DateField(blank=True, null=True)
    sospecha = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.categoria, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)


class si_0201_pr(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    ult_eess = models.CharField(max_length=200, blank=True, null=True)
    tipo_doc= models.CharField(max_length=10, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    prematuro = models.IntegerField(blank=True, null=True)
    visit7d = models.CharField(max_length=150, blank=True, null=True)
    hb30d = models.DateField(blank=True, null=True)
    suple1 = models.DateField(blank=True, null=True)
    suple2 = models.DateField(blank=True, null=True)
    suple3 = models.DateField(blank=True, null=True)
    dsje3m = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    visita4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    visita5 = models.DateField(blank=True, null=True)
    dsje6m = models.DateField(blank=True, null=True)
    ta6m = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.categoria, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.ult_eess)


class si_0201_sn(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    ult_eess = models.CharField(max_length=200, blank=True, null=True)
    tipo_doc= models.CharField(max_length=10, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    visita4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    visita5 = models.DateField(blank=True, null=True)
    dsje6m = models.DateField(blank=True, null=True)
    ta6m = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.categoria, self.documento, self.programa,\
               self.programa, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.ult_eess)


class si_0201_cont(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_sector = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=70, blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.anio, self.mes, self.cod_sector, self.sector, self.cod_dep, self.departamento,\
               self.cod_prov, self.provincia, self.cod_dist, self.distrito, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito)


class si_03(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    ult_eess = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    edias = models.IntegerField(blank=True, null=True)
    emes = models.IntegerField(blank=True, null=True)
    cred1 = models.DateField(blank=True, null=True)
    cred2 = models.DateField(blank=True, null=True)
    cred3 = models.DateField(blank=True, null=True)
    cred4 = models.DateField(blank=True, null=True)
    cred5 = models.DateField(blank=True, null=True)
    cred6 = models.DateField(blank=True, null=True)
    cred7 = models.DateField(blank=True, null=True)
    cred8 = models.DateField(blank=True, null=True)
    cred9 = models.DateField(blank=True, null=True)
    cred10 = models.DateField(blank=True, null=True)
    cred11 = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

