#coding: latin-1

from anarapp.models import Yacimiento
from django.contrib import admin

class YacimientoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identificación', {'fields': ['nombre']}),
        ('Geolocalización', {'fields': ['datum', 'latitud', 'longitud']}),
        #('Grados, minutos y segundos', {'fields': ['latitud_grados','latitud_minutos', 'latitud_segundos', 
        #                                           'longitud_grados', 'longitud_minutos', 'longitud_segundos'], 'classes':['collapse']}),
    ]
   
    list_display = ('nombre','latitud','longitud')

admin.site.register(Yacimiento, YacimientoAdmin)
