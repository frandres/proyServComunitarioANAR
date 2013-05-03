#coding: latin-1
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from anarapp.models import Yacimiento, Piedra,CaraTrabajada,ConjuntoFiguraPorTipo, TratamientoFotografia,FotografiaPiedra, ReproduccionGraficaEscalaNaturalPiedra, ReproduccionGraficaEscalaReducidaPiedra,BibliografiaPiedra

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

class BibliografiaPiedraInline(NestedTabularInline):
    extra = 1
    model =  BibliografiaPiedra

class ReproduccionGraficaEscalaReducidaInlinePiedra(NestedTabularInline):
    extra = 1
    model =  ReproduccionGraficaEscalaReducidaPiedra

class ReproduccionGraficaEscalaNaturalInlinePiedra(NestedTabularInline):
    extra = 1
    model =  ReproduccionGraficaEscalaNaturalPiedra
        
class FotografiaInline(NestedTabularInline):
    extra = 1
    model =  FotografiaPiedra

class TratamientoFotografiaInline(NestedTabularInline):
    extra = 1
    maximun = 1
    model =  TratamientoFotografia

class SeccionTrabajadaInline(NestedTabularInline):
    extra = 1
    model =  ConjuntoFiguraPorTipo

class CaraTrabajadaInline(NestedStackedInline):
    model = CaraTrabajada
    display_at_top = True
    extra = 1
    inlines = [SeccionTrabajadaInline]

class PiedraAdmin (NestedModelAdmin):
    model = Piedra
    inlines = [CaraTrabajadaInline, TratamientoFotografiaInline,FotografiaInline,ReproduccionGraficaEscalaReducidaInlinePiedra,ReproduccionGraficaEscalaNaturalInlinePiedra,BibliografiaPiedraInline]
    # fields = ('inlines','codigo')

admin.site.register(Yacimiento, YacimientoAdmin)
admin.site.register(Piedra,PiedraAdmin)
# admin.site.register(CaraTrabajada,CaraTrabajadaInline)