from django.db import models

# Create your models here.
class padron_nom(models.Model):
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    cod_padron = models.CharField(max_length=15, blank=True, null=True)
    eess = models.CharField(max_length=300, blank=True, null=True)
    ccpp = models.CharField(max_length=300, blank=True, null=True)
    est_tramite = models.CharField(max_length=30, blank=True, null=True)
    fec_tramite = models.DateField(blank=True, null=True)
    tipo_doc = models.CharField(max_length=15, blank=True, null=True)
    cnv_dni = models.CharField(max_length=20, blank=True, null=True)
    nombres_ninio = models.CharField(max_length=100, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    menor_visit = models.CharField(max_length=50, blank=True, null=True)
    menor_encont = models.CharField(max_length=10, blank=True, null=True)
    tseguro = models.CharField(max_length=10, blank=True, null=True)
    tprog_social = models.CharField(max_length=20, blank=True, null=True)
    eje_vial = models.CharField(max_length=300, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    fec_visita = models.DateField(blank=True, null=True)
    fuente = models.CharField(max_length=200, blank=True, null=True)
    eess_nacido = models.CharField(max_length=200, blank=True, null=True)
    eess_adscrip = models.CharField(max_length=200, blank=True, null=True)
    institucion = models.CharField(max_length=100, blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    dni_madre = models.CharField(max_length=20, blank=True, null=True)
    nombres_madre = models.CharField(max_length=100, blank=True, null=True)
    celular_madre = models.CharField(max_length=30, blank=True, null=True)
    grado_inst = models.CharField(max_length=80, blank=True, null=True)
    dni_jefe = models.CharField(max_length=20, blank=True, null=True)
    nombres_jefe = models.CharField(max_length=100, blank=True, null=True)
    entidad = models.CharField(max_length=100, blank=True, null=True)
    tregistro = models.CharField(max_length=50, blank=True, null=True)
    est_regist = models.CharField(max_length=50, blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.cod_dep, self.departamento, self.cod_prov, self.provincia, self.cod_dist, self.distrito,\
               self.cod_padron, self.eess, self.ccpp, self.est_tramite, self.fec_tramite, self.tipo_doc, self.cnv_dni,\
               self.nombres_ninio, self.fec_nac, self.menor_visit, self.menor_encont, self.tseguro, self.tprog_social,\
               self.eje_vial, self.descripcion, self.fec_visita, self.fuente, self.eess_nacido, self.eess_adscrip, self.institucion,\
               self.seguro, self.dni_madre, self.nombres_madre, self.celular_madre, self.grado_inst, self.dni_jefe,self.nombres_jefe,\
               self.entidad, self.tregistro, self.est_regist, self.seguro, self.mes

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito)


class actas_homol(models.Model):
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    ene = models.IntegerField(blank=True, null=True)
    feb = models.IntegerField(blank=True, null=True)
    mar = models.IntegerField(blank=True, null=True)
    abr = models.IntegerField(blank=True, null=True)
    may = models.IntegerField(blank=True, null=True)
    jun = models.IntegerField(blank=True, null=True)
    jul = models.IntegerField(blank=True, null=True)
    ago = models.IntegerField(blank=True, null=True)
    set = models.IntegerField(blank=True, null=True)
    oct = models.IntegerField(blank=True, null=True)
    nov = models.IntegerField(blank=True, null=True)
    dic = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.cod_dep, self.departamento, self.cod_prov, self.provincia, self.cod_dist, self.distrito,\
               self.ene, self.fed, self.mar, self.abr, self.may, self.jun, self.jul, self.ago, self.set, self.oct, self.nov, self.dic

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito)


class sello(models.Model):
    cod_dep = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=70, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    numdni = models.CharField(max_length=15, blank=True, null=True)
    numcnv = models.CharField(max_length=15, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    menor_encont = models.CharField(max_length=30, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    area_ccpp = models.CharField(max_length=100, blank=True, null=True)
    eje_vial = models.CharField(max_length=300, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    ref_direc = models.CharField(max_length=300, blank=True, null=True)
    tseguro = models.CharField(max_length=10, blank=True, null=True)
    seguro = models.CharField(max_length=30, blank=True, null=True)
    tprog_social = models.CharField(max_length=20, blank=True, null=True)
    est_regist = models.IntegerField(blank=True, null=True)
    meses = models.IntegerField(blank=True, null=True)
    mide = models.IntegerField(blank=True, null=True)
    var_dni = models.IntegerField(blank=True, null=True)
    var_direc = models.IntegerField(blank=True, null=True)
    medicion = models.IntegerField(blank=True, null=True)
    den = models.IntegerField(blank=True, null=True)

    def natural_key(self):
        return self.pk, self.cod_dep, self.departamento, self.cod_prov, self.provincia, self.cod_dist, self.distrito,\
               self.numdni, self.numcnv, self.documento, self.menor_encont, self.fec_nac, self.area_ccpp, self.eje_vial,\
               self.descripcion, self.ref_direc, self.tseguro, self.seguro, self.tprog_social, self.est_regist,\
               self.meses, self.mide, self.var_dni, self.var_direc, self.medicion, self.den

    # def __str__(self):
    #     return '%s %s, %s' % (self.provincia, self.distrito)


    def __lt__(self, other):
        return self.__str__() < other.__str__()
