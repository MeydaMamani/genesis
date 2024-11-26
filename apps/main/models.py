from django.db import models

# Create your models here.
class Sector(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=50)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s' % (self.codigo, self.nombre)


class Departamento(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s' % (self.codigo, self.nombre)


class Red(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=60)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)


class Provincia(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=60)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)


class MicroRed(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=60)
    red= models.ForeignKey(Red, on_delete=models.CASCADE, null=True, blank=True)
    prov= models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)


class Distrito(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=50)
    red= models.ForeignKey(Red, on_delete=models.CASCADE, null=True, blank=True)
    prov= models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    mred= models.ForeignKey(MicroRed, on_delete=models.CASCADE, null=True, blank=True)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)


class Establecimiento(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=150)
    dist= models.ForeignKey(Distrito, on_delete=models.CASCADE, null=True, blank=True)
    distrito = models.CharField(max_length=150, null=True, blank=True)
    mred= models.ForeignKey(MicroRed, on_delete=models.CASCADE, null=True, blank=True)
    microred = models.CharField(max_length=150, null=True, blank=True)
    red= models.ForeignKey(Red, on_delete=models.CASCADE, null=True, blank=True)
    nred = models.CharField(max_length=150, null=True, blank=True)
    prov= models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    provincia = models.CharField(max_length=150, null=True, blank=True)
    dep= models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    departamento = models.CharField(max_length=150, null=True, blank=True)
    sector= models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=True)
    nsector = models.CharField(max_length=150, null=True, blank=True)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)


class UPS(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=200)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)


class Profesion(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=100)

    def natural_key(self):
        return self.codigo, self.nombre

    def __str__(self):
        return '%s %s %s' % (self.codigo, self.nombre)
