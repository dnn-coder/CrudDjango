from django.db import models

class TablaEmpleado(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre+""+self.edad+""+self.genero+""+self.profesion+""+self.ciudad

class TablaNomina(models.Model):
    profesion = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)
    jornada = models.CharField(max_length=100)

    def __str__(self):
        return self.profesion+""+self.salario+""+self.jornada
