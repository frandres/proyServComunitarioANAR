#coding: latin-1
from django import forms
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from anarapp.models import Yacimiento, Piedra,CaraTrabajada, FigurasPorTipo, TratFoto, \
    InfoFoto, FotoDigital, BibPiedra, FotoBibPiedra, \
    DimensionPiedra, Manifestaciones, FichaPiedra, UbicacionCaras, EsquemaPorCara, \
    EscalaNatPiedra, EscalaRedPiedra, MatAudioVisual
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


###############################################
#### Admin de piedras - Inlines 
##############################################
        
class DimensionPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1    
    model =  DimensionPiedra

class ManifestacionesInline(NestedStackedInline):
    extra = 1
    max_num = 1
    display_at_top = False
    model =  Manifestaciones

class FigurasPorTipoInline(NestedTabularInline):
    extra = 1
    max_num = 60  
    model =  FigurasPorTipo

class EsquemaPorCaraInline(NestedTabularInline):
    extra = 1
    max_num = 6
    model =  EsquemaPorCara

class CaraTrabajadaInline(NestedTabularInline):
    display_at_top = True
    extra = 1
    max_num = 6
    model = CaraTrabajada

class UbicacionCarasInline(NestedStackedInline):
    extra = 1
    max_num = 1
    model = UbicacionCaras

class TratFotoInline(NestedStackedInline):
    extra = 1
    max_num = 1  
    model =  TratFoto

class InfoFotoInline(NestedStackedInline):
    extra = 1
    max_num = 1  
    model =  InfoFoto

class FotoDigitalInline(NestedTabularInline):
    extra = 1
    model =  FotoDigital

class EscalaNatPiedraInline(NestedTabularInline):
    extra = 1
    model =  EscalaNatPiedra

class EscalaRedPiedraInline(NestedTabularInline):
    extra = 1
    model =  EscalaRedPiedra

class BibPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1
    model =  BibPiedra

class FotoBibPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1
    model =  FotoBibPiedra

class FichaPiedraInline(NestedStackedInline):
    extra = 1
    max_num = 1    
    model =  FichaPiedra

class MatAudioVisualInline(NestedStackedInline):
    extra = 1
    max_num = 1    
    model =  MatAudioVisual
    
class PiedraAdmin (NestedModelAdmin):
    model = Piedra
    inlines = [CaraTrabajadaInline, DimensionPiedraInline,
               UbicacionCarasInline, FigurasPorTipoInline,
               EsquemaPorCaraInline,
               ManifestacionesInline,
               TratFotoInline, InfoFotoInline, FotoDigitalInline,
               EscalaNatPiedraInline, EscalaRedPiedraInline,
               BibPiedraInline, FotoBibPiedraInline,
               MatAudioVisualInline,
               FichaPiedraInline]

###############################################
#### Fin admin de piedras
##############################################
    
    
admin.site.register(Yacimiento, YacimientoAdmin)
admin.site.register(Piedra,PiedraAdmin)
