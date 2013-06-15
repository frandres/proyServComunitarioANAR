#coding: latin-1
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from anarapp.models import Yacimiento, Piedra,CaraTrabajada,ConjFiguraPorTipo, TratFotografia,FotografiaPiedra, ReproGrafEscalaNaturalPiedra, ReproGrafEscalaRedPied,BibPiedra

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

class TratFotografiaInline(NestedTabularInline):
    extra = 1
    maximun = 1
    model =  TratFotografia

class SeccionTrabajadaInline(NestedTabularInline):
    extra = 1
    model =  ConjFiguraPorTipo

class CaraTrabajadaInline(NestedStackedInline):
    model = CaraTrabajada
    display_at_top = True
    extra = 1
    inlines = [SeccionTrabajadaInline]

class PiedraAdmin (NestedModelAdmin):
    model = Piedra
    inlines = [CaraTrabajadaInline, TratFotografiaInline,FotografiaInline,ReproduccionGraficaEscalaReducidaInlinePiedra,ReproduccionGraficaEscalaNaturalInlinePiedra,BibPiedraInline]
    # fields = ('inlines','codigo')

admin.site.register(Yacimiento, YacimientoAdmin)
admin.site.register(Piedra,PiedraAdmin)
# admin.site.register(CaraTrabajada,CaraTrabajadaInline)