# -*- coding: utf-8 -*-

from django import forms
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from anarapp.models import Yacimiento, Piedra,CaraTrabajada,ConjFiguraPorTipo, TratFotografia,FotografiaPiedra, ReproGrafEscalaNaturalPiedra, \
    ReproGrafEscalaRedPied,BibPiedra, DimensionPiedra, LocalidadYacimiento,UsoActSuelo, TenenciaDeTierra,\
    Indicaciones, Croquis,Plano,FotografiaYac,Coordenadas, Datum, Altitud,TipoYacimiento,\
    ManifestUbicacionYacimiento,OrientacionYacimiento,FloraYacimiento,FaunaYacimiento,HidrologiaYacimiento,TexturaSuelo,\
    TipoExposicionYac,ConstitucionYacimiento, MaterialYacimiento,TecnicaParaGeoglifo,TecnicaParaPintura,\
    TecnicaParaPetroglifo, TecnicaParaMicroPetro,TecnicaParaMonumentos,CaracSurcoPetroglifo,\
    CaracSurcoAmoladores,CaracSurcoBateas,CaracSurcoPuntosAcopl,\
    CaracSurcoCupulas,CaracSurcoMortero,CaracDeLaPintura,CaracMonolitos,CaracMenhires,\
    CaracDolmenArt,EstadoConserYac,ConsiderTemp,CronologiaTentativa,\
    ManifestacionesAsociadas,ObtenidaPor,OtrosValoresSitio,Observacion,LlenadaPor,SupervisadaPor
from django.contrib import admin
from forms import YacimientoForm


################################################ Admin Forms para  Yacimientos ####################################

class LocalidadYacInline(admin.StackedInline):
    model = LocalidadYacimiento
    extra = 1
    max_num = 1

class UsoActSueloYacInline(admin.StackedInline):
    model = UsoActSuelo
    extra = 1
    max_num = 1

class TenenciaYacInline(admin.StackedInline):
    model = TenenciaDeTierra
    extra = 1
    max_num = 1

class IndicacionesYacInline(admin.StackedInline):
    model = Indicaciones
    extra = 1
    max_num = 1

class CroquisYacInline(admin.TabularInline):
    model = Croquis
    extra = 1

class PlanoYacInline(admin.StackedInline):
    model = Plano
    extra = 1
    max_num = 1

class CoordenadasYacInline(admin.TabularInline):
    model = Coordenadas
    extra = 1
    max_num = 1

class DatumYacInline(admin.StackedInline):
    model = Datum
    extra = 1
    max_num = 1

class AltitudYacInline(admin.TabularInline):
    model = Altitud
    extra = 1
    max_num = 1

class FotoYacInline(admin.TabularInline):
    model = FotografiaYac
    extra = 1

class TipoYacimientoYacInline(admin.StackedInline):
    model = TipoYacimiento
    extra = 1
    max_num = 1

class UbicacionYacInline(admin.TabularInline):
    model = ManifestUbicacionYacimiento
    extra = 1

class OrientacionYacInline(admin.StackedInline):
    model = OrientacionYacimiento
    extra = 1
    max_num = 1

class TexturaYacInline(admin.StackedInline):
    model = TexturaSuelo
    extra = 1
    max_num = 1

class FloraYacInline(admin.StackedInline):
    model = FloraYacimiento
    extra = 1
    max_num = 1

class FaunaYacInline(admin.StackedInline):
    model = FaunaYacimiento
    extra = 1
    max_num = 1

class HidrologiaYacInline(admin.StackedInline):
    model = HidrologiaYacimiento
    extra = 1
    max_num = 1

class TipoExposicionYacInline(admin.StackedInline):
    model = TipoExposicionYac
    extra = 1
    max_num = 1

class ConstitucionYacInline(admin.StackedInline):
    model = ConstitucionYacimiento
    extra = 1
    max_num = 1

class MaterialYacInline(admin.StackedInline):
    model = MaterialYacimiento
    extra = 1
    max_num = 1

class TecnicaParaGeoglifoYacInline(admin.StackedInline):
    model = TecnicaParaGeoglifo
    extra = 1
    max_num = 1

class TecnicaParaPinturaYacInline(admin.StackedInline):
    model = TecnicaParaPintura
    extra = 1
    max_num = 1

class TecnicaParaPetroglifoYacInline(admin.StackedInline):
    model = TecnicaParaPetroglifo
    extra = 1
    max_num = 1


class TecnicaParaMicroPetrYacInline(admin.StackedInline):
    model = TecnicaParaMicroPetro
    extra = 1
    max_num = 1

class TecnicaParaMonumentosYacInline(admin.StackedInline):
    model = TecnicaParaMonumentos
    extra = 1
    max_num = 1

class CaracSurcoPetroglifoYacInline(admin.StackedInline):
    model = CaracSurcoPetroglifo
    extra = 1
    max_num = 1

class CaracSurcoAmoladoresYacInline(admin.TabularInline):
    model = CaracSurcoAmoladores
    extra = 1
    max_num = 1

class CaracSurcoBateasYacInline(admin.TabularInline):
    model = CaracSurcoBateas
    extra = 1
    max_num = 1

class CaracSurcoPuntosAcopladosYacInline(admin.StackedInline):
    model = CaracSurcoPuntosAcopl
    extra = 1
    max_num = 1

class CaracSurcoCupulasYacInline(admin.TabularInline):
    model = CaracSurcoCupulas
    extra = 1
    max_num = 1

class CaracSurcoMorteroYacInline(admin.TabularInline):
    model = CaracSurcoMortero
    extra = 1
    max_num = 1

class CaracDeLaPinturaYacInline(admin.StackedInline):
    model = CaracDeLaPintura
    extra = 1
    max_num = 1

class CaracMonolitosYacInline(admin.StackedInline):
    model = CaracMonolitos
    extra = 1
    max_num = 1

class CaracMenhiresYacInline(admin.StackedInline):
    model = CaracMenhires
    extra = 1
    max_num = 1

class CaracDolmenArtificialYacInline(admin.StackedInline):
    model = CaracDolmenArt
    extra = 1
    max_num = 1

class EstadoConservacionYacimientoYacInline(admin.StackedInline):
    model = EstadoConserYac
    extra = 1
    max_num = 1

class ConsideracionesTemporalidadYacInline(admin.TabularInline):
    model = ConsiderTemp
    extra = 1
    max_num = 1

class CronologiaTentativaYacInline(admin.StackedInline):
    model = CronologiaTentativa
    extra = 1

class ManifestacionesAsociadasYacInline(admin.StackedInline):
    model = ManifestacionesAsociadas
    extra = 1
    max_num = 1

class ObtenidaPorYacInline(admin.StackedInline):
    model = ObtenidaPor
    extra = 1

class OtrosValoresSitioYacInline(admin.StackedInline):
    model = OtrosValoresSitio
    extra = 1
    max_num = 1

class ObservacionYacInline(admin.StackedInline):
    model = Observacion
    extra = 1
    max_num = 1

class LlenadaPorYacInline(admin.TabularInline):
    model = LlenadaPor
    extra = 1


class SupervisadaPorYacInline(admin.TabularInline):
    model = SupervisadaPor
    extra = 1



############################################Fin de AdminForms Yacimiento #########################################



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
#    max_num = 1
    model =  TratFotografia

class SeccionTrabajadaInline(NestedTabularInline):
    extra = 1
    model =  ConjFiguraPorTipo

class CaraTrabajadaInline(NestedStackedInline):
    model = CaraTrabajada
    display_at_top = True
    extra = 1
    inlines = [SeccionTrabajadaInline]

class DimensionPiedraInline(NestedTabularInline):
    extra = 1
    max_num = 1
    model =  DimensionPiedra



###############################################ADMINISTARDORES #####################################################    
#Administrador del modelo de datos Piedra
class PiedraAdmin (NestedModelAdmin):
    model = Piedra
    inlines = [
        DimensionPiedraInline, CaraTrabajadaInline, TratFotografiaInline,FotografiaInline,
        ReproduccionGraficaEscalaReducidaInlinePiedra,ReproduccionGraficaEscalaNaturalInlinePiedra,BibPiedraInline,
    ]
 

#Administrador del modelo de datos Yacimiento
class YacimientoAdmin(admin.ModelAdmin):
    #form = YacimientoForm
    model = Yacimiento
    inlines = [
        LocalidadYacInline,UsoActSueloYacInline,TenenciaYacInline,IndicacionesYacInline,CroquisYacInline,
        PlanoYacInline,CoordenadasYacInline,DatumYacInline,AltitudYacInline,FotoYacInline,
        TipoYacimientoYacInline,UbicacionYacInline, OrientacionYacInline,
        FloraYacInline,FaunaYacInline, HidrologiaYacInline, TipoExposicionYacInline, ConstitucionYacInline,
        MaterialYacInline,TecnicaParaGeoglifoYacInline,TecnicaParaPinturaYacInline,TecnicaParaPetroglifoYacInline,
        TecnicaParaMicroPetrYacInline,TecnicaParaMonumentosYacInline,CaracSurcoPetroglifoYacInline,
        CaracSurcoAmoladoresYacInline,CaracSurcoBateasYacInline, CaracSurcoPuntosAcopladosYacInline,
        CaracSurcoCupulasYacInline,CaracSurcoMorteroYacInline,CaracDeLaPinturaYacInline,
        CaracMonolitosYacInline,CaracMenhiresYacInline, CaracDolmenArtificialYacInline,
        EstadoConservacionYacimientoYacInline,ConsideracionesTemporalidadYacInline,CronologiaTentativaYacInline,
        ManifestacionesAsociadasYacInline,ObtenidaPorYacInline,OtrosValoresSitioYacInline,ObservacionYacInline,
        LlenadaPorYacInline,SupervisadaPorYacInline

    ]

    list_display = ('codigo','pais','nombre','municipio','estado')



admin.site.register(Yacimiento, YacimientoAdmin)
admin.site.register(Piedra,PiedraAdmin)


