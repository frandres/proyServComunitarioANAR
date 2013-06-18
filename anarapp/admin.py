#coding: latin-1
from django import forms
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from anarapp.models import Yacimiento, Piedra,CaraTrabajada,ConjFiguraPorTipo, TratFotografia, \
    FotografiaPiedra, ReproGrafEscalaNaturalPiedra, ReproGrafEscalaRedPied,BibPiedra, \
    DimensionPiedra, ManifestacionesPiedra, FichaPiedra, UbicacionCarasTrabajadas, EsquemaPorCara
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

class BibPiedraInline(NestedTabularInline):
    extra = 1
    model =  BibPiedra

class ReproduccionGraficaEscalaReducidaInlinePiedra(NestedTabularInline):
    extra = 1
    model =  ReproGrafEscalaRedPied

class ReproduccionGraficaEscalaNaturalInlinePiedra(NestedTabularInline):
    extra = 1
    model =  ReproGrafEscalaNaturalPiedra
        
class FotografiaInline(NestedTabularInline):
    extra = 1
    model =  FotografiaPiedra

class DimensionPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1    
    model =  DimensionPiedra

class ManifestacionesPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1
    display_at_top = False
    model =  ManifestacionesPiedra

class FichaPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1    
    model =  FichaPiedra

class ConjFiguraPorTipoInline(NestedTabularInline):
    extra = 1
    max_num = 60  
    model =  ConjFiguraPorTipo

class EsquemaPorCaraInline(NestedTabularInline):
    extra = 1
    max_num = 6
    model =  EsquemaPorCara

class CaraTrabajadaInline(NestedTabularInline):
    display_at_top = True
    extra = 1
    max_num = 6
    model = CaraTrabajada

class UbicacionCarasTrabajadasInline(NestedStackedInline):
    model = UbicacionCarasTrabajadas
    extra = 1
    max_num = 1   

class TratFotografiaInline(NestedStackedInline):
    extra = 1
    max_num = 1  
    model =  TratFotografia
    
class PiedraAdmin (NestedModelAdmin):
    model = Piedra
    inlines = [DimensionPiedraInline,  CaraTrabajadaInline,
               UbicacionCarasTrabajadasInline, ConjFiguraPorTipoInline,
               EsquemaPorCaraInline, 
               ManifestacionesPiedraInline,
               TratFotografiaInline,FotografiaInline,
               ReproduccionGraficaEscalaReducidaInlinePiedra,
               ReproduccionGraficaEscalaNaturalInlinePiedra,
               BibPiedraInline, FichaPiedraInline]
    
admin.site.register(Yacimiento, YacimientoAdmin)
admin.site.register(Piedra,PiedraAdmin)
