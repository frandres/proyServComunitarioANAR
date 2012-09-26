#coding: latin-1

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Yacimiento(models.Model):
    OPCIONES_DATUM = (
        (1, 'WGS 84'),
        (2, 'La Canoa - Provisional Suramérica 1956'),
    )
    nombre = models.CharField(max_length=100)
    longitud = models.FloatField()
    latitud = models.FloatField()
    longitud_grados = models.IntegerField( validators=[MinValueValidator(-180), MaxValueValidator(180)], null=True) 
    longitud_minutos = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(59)], null=True)
    longitud_segundos = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(59)], null=True)
    latitud_grados = models.IntegerField( validators=[MinValueValidator(-90), MaxValueValidator(90)], null=True)
    latitud_minutos = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(59)], null=True)
    latitud_segundos = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(59)], null=True)
    datum = models.IntegerField(choices = OPCIONES_DATUM)

    def _unicode_(self):
        return self.nombre

#    def transformacion_a_horas_minutos_segundos(self):
#        return 
