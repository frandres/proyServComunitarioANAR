#coding: latin-1

from anarapp.models import Yacimiento,Piedra   
from django.contrib import admin
from forms import YacimientoForm
class YacimientoAdmin(admin.ModelAdmin):
    form = YacimientoForm

# class YacimientoAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Identificación', {'fields': ['nombre']}),
#         ('Geolocalización', {'fields': ['datum', 'latitud', 'longitud']}),
#         #('Grados, minutos y segundos', {'fields': ['latitud_grados','latitud_minutos', 'latitud_segundos', 
#         #                                           'longitud_grados', 'longitud_minutos', 'longitud_segundos'], 'classes':['collapse']}),
#     ]
   
#     list_display = ('nombre','latitud','longitud')

admin.site.register(Yacimiento, YacimientoAdmin)
admin.site.register(Piedra)
