# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms


############################################# Diagrama de Yacimiento ######################################################

class Yacimiento(models.Model):
   
    
    codigo = models.CharField('00. Codigo ANAR',max_length=20)
    pais = models.CharField('0. Pais', max_length = 150)
    nombre = models.CharField('1. Nombre del Yacimiento',max_length=100)
    municipio = models.CharField('2. Municipio', max_length = 150)    
    estado = models.CharField('3. Estado', max_length = 150)   
     
     
    #representacion en string de un objeto tipo Yacimiento
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Yacimiento'
        verbose_name_plural = 'Yacimientos'



class LocalidadYacimiento(models.Model):
    
    esCentroPoblado = models.BooleanField('4.1 Centro de Poblado')
    esUrbano = models.BooleanField('4.1.1 Urbano')
    esRural = models.BooleanField('4.1.2 Rural')
    esIndigena = models.BooleanField('4.1.3 Indigena')
    nombrePoblado = models.CharField('4.1.4 Nombre', max_length = 150 ,blank = True)
    esCentroNoPoblado = models.BooleanField('4.2 No Poblado')
    nombreNoPoblado = models.CharField('4.2.1 Nombre', max_length = 150, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '4. Localidad'
        verbose_name_plural = '4. Localidad'

    def __unicode__(self):
        return 'Localidad del Yacimiento'


class UsoActSuelo(models.Model):

    esForestal = models.BooleanField('5.1 Forestal')
    esGanadero = models.BooleanField('5.2 Ganadero')
    esAgriRiesgo = models.BooleanField('5.3 Agricultura de Riesgo')
    esAgriTemp = models.BooleanField('5.4 Agricultura Temporal')
    esSueloUrbano = models.BooleanField('5.5 Urbano')
    esSueloTuristico = models.BooleanField('5.6 Turistico')
    yacimiento = models.ForeignKey(Yacimiento)
   
    class Meta:
        verbose_name = '5. Uso Actual Del Suelo'
        verbose_name_plural = '5. Uso Actual Del Suelo'

    def __unicode__(self):
        return 'Uso Actual del Suelo del Yacimiento'

class TenenciaDeTierra(models.Model):
    
    esPrivada = models.BooleanField('5.7.1 Privada')
    esComunal = models.BooleanField('5.7.2 Comunal')
    esEjido = models.BooleanField('5.7.3 Ejido')
    esMunicipal = models.BooleanField('5.7.4 Municipal')
    esABRAE = models.BooleanField('5.7.5 ABRAE (Area Bajo Regimen Especial)')
    esTenenciaOtros = models.CharField('5.7.6 Otros', max_length = 150, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
   
    class Meta:
        verbose_name = '5.7 Tenencia de la Tierra'
        verbose_name_plural = '5.7 Tenencia de la Tierra'

    def __unicode__(self):
        return 'Tenencia de la Tierra del Yacimiento'

class Indicaciones(models.Model):
    direcciones = models.CharField('6. Indicaciones', max_length = 400, blank = True) 
    puntoDatum = models.CharField('6.1 Punto Datum ', max_length = 400, blank = True) 
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '6. Indicaciones para llegar al Lugar'
        verbose_name_plural = '6. Indicaciones para llegar al Lugar'

    def __unicode__(self):
        return 'Como llegar al Yacimiento'

class Croquis (models.Model):

    urlImagen = models.CharField('6.2.1 Url de la Imagen', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '6.2 Croquis y Esquema'
        verbose_name_plural = '6.2 Croquis para Llegar al Sitio'

    def __unicode__(self):
        return 'Croquis e Imagenes para llegar al Yacimiento'

class Plano (models.Model):
    
    numeroPlano = models.IntegerField('7. Numero de plano', blank = True, null = True, )
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '7. Numero de Plano'
        verbose_name_plural = '7. Numero de Plano'

    def __unicode__(self):
        return 'Numero de Plano'

 
class Coordenadas (models.Model):
    
    longitud = models.CharField('Long. O(W)', max_length = 400, blank = True)
    latitud = models.CharField('Lat. N', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '8. Coordenadas'
        verbose_name_plural = '8. Coordenadas'

    def __unicode__(self):
        return 'Longitud y Latitud'

class Datum (models.Model):
    
    OPCIONES_DATUM = (
        (1, '9.1 WGS 84'),
        (2, '9.2 La Canoa - Provisional Suramérica 1956'),
    )  
    
    tipoDatum = models.IntegerField('9. Datum GPS',choices = OPCIONES_DATUM, blank = True,null = True)
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '9. Datum GPS'
        verbose_name_plural = '9. Datum GPS'

    def __unicode__(self):
        return 'Datum GPS' 

class Altitud (models.Model):
   
    altura = models.CharField('10.1 Altura en mts', max_length = 400, blank = True)
    superficie = models.CharField('10.2 Superficie en m2', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    
    class Meta:
        verbose_name = '10. Altitud'
        verbose_name_plural = '10. Altitud'  

    def __unicode__(self):
        return 'Altitud'

class FotografiaYac (models.Model):
   
    esAerea = models.BooleanField('Aerea')
    noEsAerea = models.BooleanField('No Aerea')
    esSatelital = models.BooleanField('Satelital')
    fecha = models.DateField('Fecha',blank = True, null= True)
    urlImagen = models.CharField('11. Url de la Imagen', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    
    class Meta:
        verbose_name = '11. Fotografia'
        verbose_name_plural = '11. Fotografias'  

    def __unicode__(self):
        return 'Fotografias del Yacimiento'

class TipoYacimiento (models.Model):

    esParedRocosa = models.BooleanField('12.1 Pared Rocosa')
    esRoca = models.BooleanField('12.2 Roca')
    esDolmen = models.BooleanField('12.3 Dolmen(natural)')
    esAbrigo = models.BooleanField('12.4 Abrigo')
    esCueva = models.BooleanField('12.5 Cueva')
    esCuevadeRec = models.BooleanField('12.6 Cueva de Recubrimiento')
    esTerrenoSup = models.BooleanField('12.7 Terreno Superficial')
    esTerrenoPro = models.BooleanField('12.8 Terreno Profundo')
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '12. Tipo de Yacimiento'
        verbose_name_plural = '12. Tipo de Yacimiento'
    def __unicode__(self):
        return 'Tipo de Yacimiento'


class ManifestUbicacionYacimiento (models.Model):

    OPCIONES_TIPO_MANIFEST = (
        (1,'13.1 Geoglifo'),
        (2,'13.2 Pintura Rupestre'),
        (3,'13.3 Petroglifo'),
        (4,'13.3.1 Petroglifo Pintado'),
        (5,'13.4 Micro-Petroglifo'),
        (6,'13.5 Piedra Mítica Natural'),
        (7,'13.6 Cerro Mítico Natural'),
        (8,'13.6.1 Cerro Mitico Natural con Petroglifo'),
        (9,'13.6.2 Cerro Mitico Natural Con Pintura'),
        (10,'13.6.3 Cerro Mitico Natural Con Dolmen'),
        (11,'13.7 Monumentos Megalíticos'),
        (12,'13.7.1 Monolitos'),
        (13,'13.7.1.1 Monolitos Con Grabados'),
        (14,'13.7.2 Menhires'),
        (15,'13.7.2.1 Menhires Con Puntos Acoplados'),
        (16,'13.7.2.2 Menhires Con Petroglifo'),
        (17,'13.7.2.3 Menhires Con Pintura'),
        (18,'13.8 Amolador'),
        (19,'13.9 Batea'),
        (20,'13.10 Puntos Acoplados'),
        (21,'13.11 Cupulas'),
        (22,'13.12 Mortero o Metate'),
    )  

    OPCIONES_UBI_MANIFEST = (
        (1,'14.1 Cerro'),
        (2,'14.1.1 Cerro - Cima'),
        (3,'14.1.2 Cerro - Ladera'),
        (4,'14.1.4 Cerro - Fila'),
        (5,'14.1.5 Cerro - Pie de Monte'),
        (6,'14.1.6 Cerro - Barranco'),
        (7,'14.1.7 Cerro - Acantilado'),
        (8,'14.2 Valle'),
        (9,'14.3 Río'),
        (10,'14.3.1 Río - Lecho'),
        (11,'14.3.2 Río - Margen Derecha'),
        (12,'14.3.3 Río - Margen Izquierda'),
        (13,'14.3.4 Río - Isla'),
        (14,'14.3.5 Río - Raudal'),
        (15,'14.4 Costa'),
       
    ) 
    
    tipoManifestacion = models.IntegerField('13. Tipo de Manifestacion',choices = OPCIONES_TIPO_MANIFEST, blank = True,null = True)
    ubicacionManifestacion = models.IntegerField('14. Ubicación de la Manifestacion',choices = OPCIONES_UBI_MANIFEST, blank = True,null = True)
    
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '13. Tipo de Manifestación'
        verbose_name_plural = '13. Tipo de Manifestación'
    def __unicode__(self):
        return 'Tipo - Ubicacion'

class OrientacionYacimiento (models.Model):

    haciaCerro = models.BooleanField('15.1 Hacia Cerro')
    haciaValle = models.BooleanField('15.2 Hacia Valle')
    haciaRio = models.BooleanField('15.3 Hacia Rio')
    haciaCosta = models.BooleanField('15.4 Hacia Costa')
    haciaCielo = models.BooleanField('15.5 Hacia Cielo')
    otros = models.CharField('15.6 Otros', max_length = 400, blank = True)
    orientacion = models.CharField('15.7 Orientacion Cardinal', max_length = 400, blank = True)
    
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '15. Orientacion del Yacimiento'
        verbose_name_plural = '15. Orientacion del Yacimiento'
    def __unicode__(self):
        return 'Orientacion del Yacimiento'

class TexturaSuelo (models.Model):

    esRocaMadre = models.BooleanField('16.1 Roca Madre')
    esPedregoso = models.BooleanField('16.2 Pedregoso')
    esArenoso = models.BooleanField('16.3 Arenoso')
    esArcilloso = models.BooleanField('16.4 Arcilloso')
    mixto = models.CharField('16.5 Mixto', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)

    class Meta:
        verbose_name = '16. Textura del Suelo'
        verbose_name_plural = '16. Textura del Suelo'
    def __unicode__(self):
        return 'Textura del Suelo'

class FloraYacimiento (models.Model):
    
    flora = models.CharField('17. Flora', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    
    class Meta:
        verbose_name = '17. Flora'
        verbose_name_plural = '17. Flora'
    def __unicode__(self):
        return 'Flora del Yacimiento'

class FaunaYacimiento (models.Model):
    
    fauna = models.CharField('18. Fauna', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    
    class Meta:
        verbose_name = '18. Fauna'
        verbose_name_plural = '18. Fauna'
    def __unicode__(self):
        return 'Fauna del Yacimiento'

class HidrologiaYacimiento (models.Model):

    rio = models.BooleanField('19.1 Rio')
    laguna = models.BooleanField('19.2 Laguna')
    arroyo = models.BooleanField('19.3 Arroyo')
    arroyoPerenne= models.BooleanField('19.3.1 Perenne')
    manantial = models.BooleanField('19.4 Manantial')
    manantialIntermitente = models.BooleanField('19.4.1 Intermitente')
    otros = models.CharField('19.5 Otros', max_length = 400, blank = True)
    nombre = models.CharField('19.6 Nombre', max_length = 400, blank = True)
    distancia = models.CharField('19.7 Distancia al Yacimiento', max_length = 400, blank = True)
    observaciones = models.CharField('19.8 Observaciones', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '19. Hidrología'
        verbose_name_plural = '19. Hidrología'
    def __unicode__(self):
        return 'Hidrologia'

class TipoExposicionYac(models.Model):

    expuesto = models.BooleanField('20.1 Expuesto')
    expuesto = models.BooleanField('20.2 No Expuesto')
    expuestoPeriodicamente = models.BooleanField('20.3 Expuesto Periódicamente')
    observaciones = models.CharField('20.4 Observaciones', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '20. Exposición'
        verbose_name_plural = '20. Exposición'
    def __unicode__(self):
        return 'Exposicion'

class ConstitucionYacimiento (models.Model):

    nroPiedras = models.IntegerField('21.1 Nro de Piedras en el Yacimiento Original', blank = True, null = True, )
    nroPiedrasGrabadas = models.IntegerField('21.1.1 Nro de Piedras Grabadas', blank = True, null = True, )
    nroPiedrasPintadas = models.IntegerField('21.1.2 Nro de Piedras Pintadas', blank = True, null = True, )
    nroPiedrasColocadas = models.IntegerField('21.1.3 Nro Piedras Colocadas', blank = True, null = True, )
    otros = models.CharField('21.2 Otros', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '21. Constitución del Yacimiento'
        verbose_name_plural = '21. Constitución del Yacimiento'
    def __unicode__(self):
        return 'Constituicion'

class MaterialYacimiento(models.Model):
    
    esRoca = models.BooleanField('22.1 Roca')
    esIgnea = models.BooleanField('22.1.1.1 Ignea')
    esMetamor= models.BooleanField('22.1.1.2 Metamórfica')
    esSedimentaria = models.BooleanField('22.1.1.3 Sedimentaria')
    tipo = models.CharField('22.1.1.4 Tipo', max_length = 400, blank = True)
    esTierra = models.BooleanField('22.2 Tierra')
    esHueso = models.BooleanField('22.3 Hueso')
    esCorteza = models.BooleanField('22.4 Corteza de árbol')
    esPiel = models.BooleanField('22.5 Pieles')
    otros = models.CharField('22.6 Otros', max_length = 400, blank = True)
    

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '22. Material'
        verbose_name_plural = '22. Material'
    def __unicode__(self):
        return 'Material Yacimiento'  

class TecnicaParaGeoglifo (models.Model):
    
    tecnicas = models.CharField('23.1 Técnicas de Construcción', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '23. Técnica-13.1 Geoglifo'
        verbose_name_plural = '23. Técnica-13.1 Geoglifo'
    def __unicode__(self):
        return 'Tecnica' 

class TecnicaParaPintura (models.Model):
    
    conDedo = models.BooleanField('23.2 Dedo')
    fibra = models.BooleanField('23.3 Fibra')
    soplado = models.BooleanField('23.4 Soplado')
    otros = models.CharField('23.5 Otros', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '23. Técnica-13.2 Pintura Rupestre'
        verbose_name_plural = '23. Técnica-13.2 Pintura Rupestre'
    def __unicode__(self):
        return 'Tecnica'     

class TecnicaParaPetroglifo (models.Model):
    
    esGrabado = models.BooleanField('23.6 Grabado')
    esGrabadoPercusion = models.BooleanField('23.6.1 Percusión')
    esGrabadoPercusionDirecta = models.BooleanField('23.6.1.1 Directa')
    esGrabadoPercusionIndirecta = models.BooleanField('23.6.1.2 Indirecta')
    esAbrasion = models.BooleanField('23.6.2 Abrasión')
    esAbrasionPiedra = models.BooleanField('23.6.2.1 Piedra')
    esAbrasionArena = models.BooleanField('23.6.2.2 Arena')
    esAbrasion = models.BooleanField('23.6.2.3 Concha')
    otros = models.CharField('23.6.3 Otros', max_length = 400, blank = True)


    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '23. Técnica-13.3 Petroglifo'
        verbose_name_plural = '23. Técnica-13.3 Petroglifo'
    def __unicode__(self):
        return 'Tecnica'

class TecnicaParaMicroPetro (models.Model):
    
    esGrabado = models.BooleanField('23.6 Grabado')
    esGrabadoPercusion = models.BooleanField('23.6.1 Percusión')
    esGrabadoPercusionDirecta = models.BooleanField('23.6.1.1 Directa')
    esGrabadoPercusionIndirecta = models.BooleanField('23.6.1.2 Indirecta')
    esAbrasion = models.BooleanField('23.6.2 Abrasión')
    esAbrasionPiedra = models.BooleanField('23.6.2.1 Piedra')
    esAbrasionArena = models.BooleanField('23.6.2.2 Arena')
    esAbrasion = models.BooleanField('23.6.2.3 Concha')
    otros = models.CharField('23.6.3 Otros', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '23. Técnica-13.4 Micro-Petroglifo'
        verbose_name_plural = '23. Técnica-13.4 Micro-Petroglifo'
    def __unicode__(self):
        return 'Tecnica' 

class TecnicaParaMonumentos (models.Model):
    
    esMonolito = models.BooleanField('13.7.1 Monolitos')
    esMenhir = models.BooleanField('13.7.2 Menhires')
    esDolmen = models.BooleanField('13.7.3 Dolmen (artificial)')
    tecnicas = models.CharField('23.7 Técnicas de Construcción', max_length = 400, blank = True)
    otros = models.CharField('23.8 Otros', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '23. Técnica-13.7 Monumentos '
        verbose_name_plural = '23. Técnica-13.7 Monumentos'
    def __unicode__(self):
        return 'Tecnica' 

class CaracSurcoPetroglifo (models.Model):

    anchoDe = models.CharField('24.1 Ancho de (en cm)', max_length = 400, blank = True)
    anchoA = models.CharField('24.1 Ancho a (en cm)', max_length = 400, blank = True)
    produndidadDe = models.CharField('24.2 Profundidad de (en cm)', max_length = 400, blank = True)
    profundidadA = models.CharField('24.2 Profundidad a (en cm)', max_length = 400, blank = True)
    esBase = models.BooleanField('24.3 Base')
    esBaseRedonda = models.BooleanField('24.3.1 Base Redonda')
    esBaseAguda = models.BooleanField('24.3.2 Base Aguda')
    esBajoRelieve = models.BooleanField('24.4 Bajo Relieve')
    esBajoRelieveLineal = models.BooleanField('24.5.1 Lineal')
    esBajoRelievePlanar = models.BooleanField('24.5.2 Planar')
    esAltoRelieve = models.BooleanField('24.4.1 Alto Relieve')
    esAltoRelieveLineal = models.BooleanField('24.4.1 Lineal')
    esAltoRelievePlanar = models.BooleanField('24.4.2 Planar')
    esAreaInterlineal = models.BooleanField('24.6 Áreas Interlineales')
    esAreaInterlinealPulida = models.BooleanField('24.6.1 Pulidas')
    esAreaInterlinealRebajada = models.BooleanField('24.6.2 Rebajadas')
    esGrabadoSuperpuesto = models.BooleanField('24.7 Grabados Superpuestos')
    esGrabadoRebajado = models.BooleanField('24.8 Grabados Rebajados')
    
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '24. Caract. Surco - 13.3 Petroglifo'
        verbose_name_plural = '24. Caract. Surco - 13.3 Petroglifo'
    def __unicode__(self):
        return 'Caracteristica del Surco Grabado'

class CaracSurcoAmoladores(models.Model):
    
    largo = models.CharField('24.9 Largo (en cm)', max_length = 400, blank = True)
    ancho = models.CharField('24.10 Ancho (en cm)', max_length = 400, blank = True)
    diametro = models.CharField('24.11 Diámetro(en cm)', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '24. Caract. Surco - 13.9 Amoladores'
        verbose_name_plural = '24. Caract. Surco - 13.9 Amoladores'
    def __unicode__(self):
        return 'Caracteristica del Surco Grabado'
class CaracSurcoBateas(models.Model):

    largo = models.CharField('24.12 Largo (en cm)', max_length = 400, blank = True)
    ancho = models.CharField('24.13 Ancho (en cm)', max_length = 400, blank = True)
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '24. Caract. Surco - 13.10 Bateas'
        verbose_name_plural = '24. Caract. Surco - 13.10 Bateas'
    def __unicode__(self):
        return 'Caracteristica del Surco Grabado'


class CaracSurcoPuntosAcopl (models.Model):

    esPunteado= models.BooleanField('24.14 Punteado')
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '24. Car. Surco - 13.11 Puntos Acoplados'
        verbose_name_plural = '24. Car. Surco - 13.11 Puntos Acoplados'
    def __unicode__(self):
        return 'Caracteristica del Surco Grabado'

class CaracSurcoCupulas (models.Model):

    largo = models.CharField('24.9 Largo (en cm)', max_length = 400, blank = True)
    ancho = models.CharField('24.10 Ancho (en cm)', max_length = 400, blank = True)
    diametro = models.CharField('24.11 Diámetro(en cm)', max_length = 400, blank = True)
    
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '24. Caract. Surco - 13.12 Cúpula'
        verbose_name_plural = '24. Caract. Surco - 13.12 Cúpula'
    def __unicode__(self):
        return 'Caracteristica del Surco Grabado'

class CaracSurcoMortero (models.Model):

    largo = models.CharField('24.9 Largo (en cm)', max_length = 400, blank = True)
    ancho = models.CharField('24.10 Ancho (en cm)', max_length = 400, blank = True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '24. Caract. Surco - 13.13 Mortero'
        verbose_name_plural = '24. Caract. Surco - 13.13 Mortero'
    def __unicode__(self):
        return 'Caracteristica del Surco Grabado'


class CaracDeLaPintura (models.Model):

    esPinturaRupestre = models.BooleanField('13.2 Pintura Rupestre')
    esTecnicaDactilar = models.BooleanField('25.1 Técnica/ 25.1.1 Dactilar')
    esTecnicaFibra = models.BooleanField('25.1 Técnica/ 25.1.2 Fibra')
    otros = models.CharField('25.1 Técnica/ 25.1.3 Otros', max_length = 400, blank = True)
    esLineaSencilla= models.BooleanField('25.2 Tipo de Línea/ 25.2.1 Línea Sencilla')
    anchoDe = models.CharField('25.2.1.1 Ancho de la Línea Sencilla/ Ancho de (en cm)', max_length = 400, blank = True)
    anchoA = models.CharField('25.2.1.1 Ancho de la Línea Sencilla/ Ancho a (en cm)', max_length = 400, blank = True)
    esLineaCompuesta= models.BooleanField('25.2 Tipo de Línea/ 25.2.1 Línea Compuesta')
    anchoDeComp = models.CharField('25.2.1.1 Ancho de la Línea Compuesta/ Ancho de (en cm)', max_length = 400, blank = True)
    anchoAComp = models.CharField('25.2.1.1 Ancho de la Línea Compuesta/ Ancho a (en cm)', max_length = 400, blank = True)
    esImpresionDeManos = models.BooleanField('25.4 Impresión de Manos')
    esImpresionDeManosPositivo = models.BooleanField('25.4 Impresión de Manos/ 25.4.1 Positivo')
    esImpresionDeManosNegativo = models.BooleanField('25.4 Impresión de Manos/ 25.4.2 Negativo')
    tienesFigurasSuperpuestas = models.BooleanField('25.5 Figuras Superpuestas')

    ###IMPORTANTE FALTA 25.6 COLORES ------ PREGUNTAR A RUBY .... 25.6.2 y 25.6.1
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '25. Caract. - 13.2 Pintura Rupestre'
        verbose_name_plural = '25. Caract. - 13.2 Pintura Rupestre'
    def __unicode__(self):
        return 'Caracteristicas de la Pintura'

class CaracMonolitos(models.Model):

    cantidad = models.IntegerField('26.1 Cantidad ', blank = True, null = True, )
    esPinturaRupestre = models.BooleanField('13.7.1.1 Con Grabados')
    cantidadConGrabados = models.IntegerField('26.2 Cantidad con Grabados', blank = True, null = True, )

    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '26. Caract. MM - 13.7.1 Monolitos'
        verbose_name_plural = '26. Caract. MM - 13.7.1 Monolitos'
    def __unicode__(self):
        return 'Caracteristicas del Monumento Megalitico'

class CaracMenhires(models.Model):

    sonPiedrasVerticales = models.BooleanField('26.0 Piedras Verticales')
    cantidadPiedrasVerticales = models.IntegerField('26.3 Cantidad', blank = True, null = True, )
    conPuntosAcoplados = models.BooleanField('13.7.2.1 Con Puntos Acoplados')
    cantidadConPuntosAcoplados = models.IntegerField('26.4 Cantidad', blank = True, null = True, )
    ConPetroglifo = models.BooleanField('13.7.2.2 Con Petroglifo')
    cantidadConPetroglifo = models.IntegerField('26.5 Cantidad', blank = True, null = True, )
    conPinturas = models.BooleanField('13.7.2.3 Con Pinturas')
    cantidadConPinturas = models.IntegerField('26.6 Cantidad', blank = True, null = True, )
    distanciamiento = models.IntegerField('26.7 Distanciamiento (en cm)', blank = True, null = True, )

    
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '26. Caract. MM - 13.7.2 Menhires'
        verbose_name_plural = '26. Caract. MM - 13.7.2 Menhires'
    def __unicode__(self):
        return 'Caracteristicas del Monumento Megalitico'

class CaracDolmenArt(models.Model):

    ConPetroglifo = models.BooleanField('13.7.3.1 Con Petroglifo')
    cantidadConPetroglifo = models.IntegerField('26.8 Cantidad', blank = True, null = True, )
    conPinturas = models.BooleanField('13.7.3.2 Con Pinturas')
    cantidadConPinturas = models.IntegerField('26.9 Cantidad', blank = True, null = True, )
    notas = models.CharField('26.10 Notas', max_length = 400, blank = True)
   
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '26. Caract. MM - 13.7.3 Dolmen'
        verbose_name_plural = '26. Caract. MM - 13.7.3 Dolmen'
    def __unicode__(self):
        return 'Caracteristicas del Monumento Megalitico'

class EstadoConserYac(models.Model):
   
    enBuenEstado = models.BooleanField('27.1 Bueno')
    estadoModificado = models.BooleanField('27.2 Modificado')
    trasladado = models.IntegerField('27.2.1 Trasladado', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    trasladadoPa = models.CharField('27.2.1 Trasladado Pa(s) Nro ', max_length = 400, blank = True)
    sumergido = models.IntegerField('27.2.2 Sumergido', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    sumergidoPa = models.CharField('27.2.2 Sumergido Pa(s) Nro ', max_length = 400, blank = True)
    enterrado = models.IntegerField('27.2.3 Enterrado', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    enterradoPa = models.CharField('27.2.3 Enterrado Pa(s) Nro ', max_length = 400, blank = True)
    perdido = models.IntegerField('27.2.4 Perdido', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    perdidoPa = models.CharField('27.2.4 Perdido Pa(s) Nro ', max_length = 400, blank = True)
    destruido = models.IntegerField('27.2.5 Destruido', blank = True, null = True,
                                     validators=[MinValueValidator(1), MaxValueValidator(2)] )
    destruidoPa = models.CharField('27.2.5 Destruido Pa(s) Nro ', max_length = 400, blank = True)
    crecimientoVeg = models.IntegerField('27.2.6 Crecimiento Vegetal', blank = True, null = True,
                                        validators=[MinValueValidator(1), MaxValueValidator(2)] )
    crecimientoVegPa = models.CharField('27.2.6 Crecimiento Vegetal Pa(s) Nro ', max_length = 400, blank = True)
    patina = models.IntegerField('27.2.7 Pátina', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    patinaPa = models.CharField('27.2.7 Pátina Pa(s) Nro ', max_length = 400, blank = True)
    erosion = models.IntegerField('27.2.8 Erosión ', blank = True, null = True,
                                     validators=[MinValueValidator(1), MaxValueValidator(2)] )
    erosionPa = models.CharField('27.2.8 Erosión Pa(s) Nro ', max_length = 400, blank = True)
    
    estaDestruido = models.BooleanField('27.3 Grado de Destrucción del Sitio')
    esPorCausaNatural = models.BooleanField('27.3.1 Natural')
    enPorCausaNaturalLigera = models.BooleanField('27.3.1.1 Ligera')
    enPorCausaNaturalAguda = models.BooleanField('27.3.1.2 Aguda')
    enPorCausaHumana = models.BooleanField('27.3.2 Humana')
    enPorCausaHumanaLigera = models.BooleanField('27.3.2.1 Ligera')
    enPorCausaHumanaAguda = models.BooleanField('27.3.2.1 Aguda')
    especificar = models.CharField('27.4 Especificar Causa y Efecto', max_length = 400, blank = True)
    destruccionPotencial = models.BooleanField('27.5 Destrucción Potencial del Sitio')
    porAsentamientoHumand = models.BooleanField('27.5.1 Causas / 27.5.1.1 Asentamiento Humano')
    porObraCortoPlazo = models.BooleanField('27.5.1 Causas / 27.5.1.2 Obra Infraestrucrura a Corto Plazo')
    porObraMedianoPlazo = models.BooleanField('27.5.1 Causas / 27.5.1.3 Obra Infraestrucrura a Mediano Plazo')
    porObraLargoPlazo = models.BooleanField('27.5.1 Causas / 27.5.1.4 Obra Infraestrucrura a Largo Plazo')
    porNivelacion = models.BooleanField('27.5.1 Causas / 27.5.1.5 Nivelación del Terreno Como Obra Agrícola')
    porExtraccionFamiliar = models.BooleanField('27.5.1 Causas / 27.5.1.6 Extracción Como Actividad Familiar')
    porExtraccionMayor = models.BooleanField('27.5.1 Causas / 27.5.1.7 Extracción Como Actividad Mayor')
    porVandalismo = models.BooleanField('27.5.1 Causas / 27.5.1.8 Vandalismo')
    porErosion = models.BooleanField('27.5.1 Causas / 27.5.1.9 Erosión')
    porErosionParModerada = models.BooleanField('27.5.1 Causas / 27.5.1.9.1 Erosión Parcial Moderada')
    porErosionParSevera = models.BooleanField('27.5.1 Causas / 27.5.1.9.2 Erosión Parcial Severa')
    porErosionExtModerada = models.BooleanField('27.5.1 Causas / 27.5.1.9.3 Erosión Extensiva Moderada')
    porErosionExtSevera = models.BooleanField('27.5.1 Causas / 27.5.1.9.4 Erosión Extensiva Severa')
    otros = models.CharField('27.5.1 Causas/ 27.5.1.10 Otros', max_length = 400, blank = True)
    observaciones = models.CharField('27.6 Observaciones Sobre Intensidad de Destrucción del Sitio, y Otros Procesos No Descritos', max_length = 400, blank = True)
    esDeTiempo = models.BooleanField('27.6.1 Tiempo')
    esInmediato = models.BooleanField('27.6.1.1 Inmediato')
    unAno = models.BooleanField('27.6.1.2 Un Año')
    dosAno = models.BooleanField('27.6.1.3  Dos Años')
    tresAno = models.BooleanField('27.6.1.4 Tres Años')
    cuatroAno = models.BooleanField('27.6.1.5 Cuatro Años')
    cincoAno = models.BooleanField('27.6.1.6 Cindo Años')
    mas = models.CharField('27.6.1.7 Más', max_length = 400, blank = True)


    
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '27. Estado de la Conservación'
        verbose_name_plural = '27. Estado de la Conservación'
    def __unicode__(self):
        return 'Estado de la Conservacion'

class ConsiderTemp(models.Model):

    cincoAno = models.BooleanField('28.1 Patina')
    otros = models.CharField('28.2 Otros', max_length = 400, blank = True)
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '28. Consider. Sobre Temporaladidad'
        verbose_name_plural = '28. Consider. Sobre Temporaladidad'
    def __unicode__(self):
        return 'Consideraciones Sobre Temporaladidad'

class CronologiaTentativa(models.Model):

    esCrono1 = models.BooleanField('29.1 Anterior a 5000 a.p.')
    esCrono2 = models.BooleanField('29.2 5000 - 1500 a.p.')
    esCrono3 = models.BooleanField('29.3 1500 a.p. - 200 n.e.')
    esCrono4 = models.BooleanField('29.4 200 - 650/900 n.e.')
    esCrono5 = models.BooleanField('29.5 650/900 - 1200 n.e.')
    esCrono6 = models.BooleanField('29.6 1200 - 1521 n.e.')
    esCrono7 = models.BooleanField('29.7 Post 1521 n.e.')
    autor = models.CharField('29.8  Autor', max_length = 400, blank = True)
    fecha = models.CharField('29.8.1 Fecha', max_length = 400, blank = True)
    institucion = models.CharField('29.8.2 Institución', max_length = 400, blank = True)
    pais = models.CharField('29.8.3 País', max_length = 400, blank = True)
    direccion = models.CharField('29.8.4 Dirección', max_length = 400, blank = True)
    telefono = models.CharField('29.8.5 Tel/Fax', max_length = 400, blank = True)
    mail = models.CharField('29.8.6 Correo Electrónico', max_length = 400, blank = True)
    tecnica = models.CharField('29.8.7 Técnica', max_length = 400, blank = True)
    bibliografia = models.CharField('29.8.8 Bibliografía', max_length = 400, blank = True)
    twitter = models.CharField('29.8.9 Twitter', max_length = 400, blank = True)
    facebook = models.CharField('29.8.10 Facebook', max_length = 400, blank = True)
    
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '29. Cronología Tentativa'
        verbose_name_plural = '29. Cronología Tentativa'
    def __unicode__(self):
        return 'Cronologia Tentativa'

class ManifestacionesAsociadas(models.Model):

    esLitica = models.BooleanField('30.1 Lítica')
    descripcionLitica = models.CharField('30.1 Descripción Lítica', max_length = 1200, blank = True)
    esCeramica = models.BooleanField('30.2 Cerámica')
    descripcionCeramica = models.CharField('30.2 Descripción Cerámica', max_length = 1200, blank = True)
    esOseo = models.BooleanField('30.3 Oseo')
    descripcionOseo = models.CharField('30.3 Descripción Oseo', max_length = 1200, blank = True)
    esConcha = models.BooleanField('30.4 Concha')
    descripcionConcha = models.CharField('30.4 Descripción Concha', max_length = 1200, blank = True)
    esCarbon = models.BooleanField('30.5 Carbón No Superficial')
    descripcionCarbon = models.CharField('30.5 Descripción Carbón No Superficial', max_length = 1200, blank = True)
    esMito = models.BooleanField('30.6 Mitos')
    descripcionMito = models.CharField('30.6 Descripción Mitos', max_length = 1200, blank = True)
    esCementerio = models.BooleanField('30.7 Cementerios')
    descripcionCementerio = models.CharField('30.7 Descripción Cementerios', max_length = 1200, blank = True)
    esMonticulo = models.BooleanField('30.8 Montículos')
    descripcionMonticulo = models.CharField('30.8 Descripción Montículos', max_length = 1200, blank = True)
    otros = models.CharField('30.9 Otros', max_length = 1200, blank = True)

    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = '30. Manifestaciones Asociadas'
    def __unicode__(self):
        return 'Manifestaciones Asociadas'


class ObtenidaPor(models.Model):

    porProspeccion = models.BooleanField('32.1 Prospección Sistemática')
    
    porComunicacion = models.BooleanField('32.2 Comunicación Personal')
    nombre = models.CharField('32.2.1 Nombre', max_length = 200, blank = True)
    direccion = models.CharField('32.2.2 Dirección', max_length = 200, blank = True)
    telefono = models.CharField('32.2.3 Telf/Fax', max_length = 200, blank = True)
    celular = models.CharField('32.2.4 Celular', max_length = 200, blank = True)
    mail = models.CharField('32.2.5 Correo Electrónico', max_length = 200, blank = True)
    sitioweb = models.CharField('32.2.6 Web', max_length = 200, blank = True)
    twitter = models.CharField('32.2.7 Twitter', max_length = 200, blank = True)
    facebook = models.CharField('32.2.8 Facebook', max_length = 200, blank = True)
    blog = models.CharField('32.2.9 Blog', max_length = 200, blank = True)
    fecha = models.DateField('32.2.10 Fecha',blank = True, null= True)   
    verificadoEnCampo = models.BooleanField('32.3 Verificado en el Campo')

    

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '32. Información Obtenida'
        verbose_name_plural = '32. Información Obtenida'
    def __unicode__(self):
        return 'Informacion Obtenida Por'


class OtrosValoresSitio(models.Model):
   
    valores = models.CharField('33. Otros Valores del Sitio', max_length = 1200, blank = True)
    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '33. Otros Valores'
        verbose_name_plural = '33. Otros Valores'
    def __unicode__(self):
        return 'Otros Valores del Sitio' 


class Observacion(models.Model):
   
    observaciones = models.CharField('34. Observaciones', max_length = 1200, blank = True)

    yacimiento = models.OneToOneField(Yacimiento)
    class Meta:
        verbose_name = '34. Observaciones'
        verbose_name_plural = '34. Observaciones'
    def __unicode__(self):
        return 'Observaciones'    

class LlenadaPor(models.Model):

    nombre = models.CharField('35.1 Llenada Por: ', max_length = 200, blank = True)
    fecha = models.DateField('35.2 Fecha',blank = True, null= True)

    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '35. Ficha Llenada Por'
        verbose_name_plural = '35. Ficha Llenada Por'
    def __unicode__(self):
        return 'Ficha Llenada Por'

class SupervisadaPor(models.Model):

    nombre = models.CharField('36.1 Supervisada Por: ', max_length = 200, blank = True)
    fecha = models.DateField('36.2 Fecha',blank = True, null= True)
    yacimiento = models.ForeignKey(Yacimiento)
    class Meta:
        verbose_name = '36. Ficha Supervisada Por'
        verbose_name_plural = '36. Ficha Supervisada Por'
    def __unicode__(self):
        return 'Ficha Supervisada Por'


############################################# Fin Clases Yacimiento ######################################################

############################################# Diagrama de piedra #########################################################


class MaterialApoyo (models.Model):
    pass

class MecObtInformacion (models.Model):
    pass

class Piedra(models.Model):

    yacimiento = models.ForeignKey(Yacimiento)
    codigo = models.CharField('0. Codigo de la piedra', max_length=20)      
    nombre = models.CharField('1. Nombre de la piedra', max_length=150)
    manifiestacionAsociada = models.CharField('1.1 Manifestaciones Asociadas', max_length=150)
    nombreFiguras = models.CharField('2. Nombre de las figuras',max_length=150)
    estado= models.CharField('3. Estado',max_length=40)
    
    numeroCaras = models.IntegerField('4. Numero de Caras')
    numeroCarasTrajabadas = models.IntegerField('5. Numero de caras trabajadas')
    otrosValoresDeLaPiedra = models.CharField('15. Otros valores de la piedra',max_length=150)
    observaciones = models.CharField('16. Observaciones',max_length=150)
    
    autorFicha = models.CharField('17a. Ficha llenada por', max_length=40)
    fechaEscrituraFicha = models.DateField('17.b Ficha llenada Fecha')

    supervisorFicha = models.CharField('17a. Ficha supervisada por', max_length=40)
    fechaSupervisionFicha = models.DateField('17.b Ficha supervisada Fecha')

    revisoFicha = models.CharField('17a. Ficha rellena por', max_length=40)

    # materialesApoyo = models.ManyToManyField(MaterialApoyo)
    # mecanismosObtencionInformacion = models.ManyToManyField(MecObtInformacion)

class DimensionPiedra(models.Model):

    piedra = models.ForeignKey(Piedra)
    altoMaximo =  models.DecimalField('7.a Alto Maximo', max_digits=12, decimal_places=6)
    largoMaximo = models.DecimalField('7.b Largo Maximo',max_digits=12, decimal_places=6)
    anchoMaximo = models.DecimalField('7.c Ancho Maximo',max_digits=12, decimal_places=6)
    
    class Meta:
        verbose_name = '7. Dimensiones de la piedra'
        verbose_name_plural = '7. Dimensiones de la piedra'

class TratFotografia(models.Model):
    
    piedra = models.ForeignKey(Piedra)
    limpiezaCon = models.CharField('12.1 Limpieza con', max_length = 40)
    rellenoSurcos = models.CharField('12.2 Relleno de surcos con', max_length = 40)
    tratamientoDigital = models.CharField('12.3 Tratamiento digital', max_length = 40)
    programaVersion = models.CharField('12.4 Programa/versión', max_length = 40)
    otrosTratamientosFotografia = models.CharField('12.5 Otros tratamientos fotografía:', max_length = 150)

class CaraTrabajada(models.Model):

    OPCIONES_ORIENTACION_CARA_TRABAJADA = (
        (0, 'Tope'),
        (1, 'Norte'),
        (2, 'Noreste'),
        (3, 'Este'),
        (4, 'Sureste'),
        (5, 'Sur'),
        (6, 'Suroeste'),
        (7, 'Oeste'),
        (8, 'Noroeste'),
        (9, 'Piso o plano inclinado'),
    )

    OPCIONES_LUMINOSIDAD = (

        (0, 'Fótico'),
        (1, 'Escótico'),

    )

    orientacionDeLaCara = models.IntegerField('6. Orientación', choices = OPCIONES_ORIENTACION_CARA_TRABAJADA)

    OPCIONES_CONEXION_FIGURAS = (
        (1, 'Presencia de una sola figura'),
        (2, 'Menos del 10% interconectadas'),
        (3, '50% interconectadas'),
        (4, 'Mas del 80% interconectadas'),
    )

    conexionFiguras = models.IntegerField('11 Conexion Figuras', choices = OPCIONES_CONEXION_FIGURAS)

    alto = models.DecimalField('7.1 Alto',max_digits=6, decimal_places=3)
    ancho = models.DecimalField('7.2 Ancho',max_digits=6, decimal_places=3)
    largo = models.DecimalField('7.3 Largo',max_digits=6, decimal_places=3)
    distanciaBocaPrincipal = models.DecimalField('8.3 Distancia Boca Principal',max_digits=12, decimal_places=6)    
    altura = models.DecimalField('8.3.2 Altura',max_digits=6, decimal_places=3)   
    luminosidad = models.IntegerField('8.3.1 Luminosidad', choices = OPCIONES_LUMINOSIDAD) 
    requiereAndamiaje = models.BooleanField('¿Requiere andamiaje?')

    # Manifestaciones

    tienePetroglifo = models.BooleanField('Petroglifo')
    tienePinturaRupestre = models.BooleanField('Pintura Rupestre')
    tieneAmoladores = models.BooleanField('Amoladores')
    tienePuntosAcoplados = models.BooleanField('Puntos Acoplados')
    tieneCupulas = models.BooleanField('Cupulas')

    # Ubicacion

    ubicadaEnTodaLaCaverna = models.BooleanField('En toda la caverna')
    # ubicadaEnAreasEspecificas = models.BooleanField('Pintura Rupestre')
    ubicadaEnSalaPrincipal = models.BooleanField('En sala principal')
    ubicadaEnOtraSala = models.BooleanField('En otra sala')
    ubicadaEnLagoInterior = models.BooleanField('En lago interior')
    ubicadaEnClaraboya = models.BooleanField('En claraboya')
    
    piedra = models.ForeignKey(Piedra)

class ConjFiguraPorTipo(models.Model):

    OPCIONES_UBICACION_CARA_TRABAJADA = (
        (1, 'Antropomorfas'),
        (2, 'Zoomorfas'),
        (3, 'Geométricas'),
        (4, 'Puntos Acoplados'),
        (5, 'Cupulas'),
        (6, 'Zoo-antropomorfas'),
        (7, 'Antropo-geométricas'),
        (8, 'Zoo-geométricas'),
        (9, 'Amoladores'),
        (10, 'Bateas'),
    )

    seccion =   models.IntegerField('Seccion de la cara.')
    tipoFigura = models.IntegerField('9.a Tipo de figura',choices = OPCIONES_UBICACION_CARA_TRABAJADA)
    cantidad =  models.IntegerField('9.b Cantidad')
       
    descripcion = models.CharField('9.c Descripcion',max_length=150) 
    # posicion = models.CharField('9.c Posicion de las figuras',max_length=150) 
    cara = models.ForeignKey(CaraTrabajada)

    class Meta:
        verbose_name = 'Conjunt de Figuras por Tipo'
        verbose_name_plural = 'Conjuntos de Figuras por tipo'
    

class RecursoMultimedia (MaterialApoyo):

    tecnica = models.CharField('13.4.1 Técnica',max_length=150) 
    imagen = models.CharField(max_length=150) # models.ImageField()

class PaginaWEB (MaterialApoyo):
    piedra = models.ForeignKey(Piedra)
    direccionURL = models.URLField ('13.8 Página Web')

class Grabacion (MaterialApoyo):

    formato = models.CharField('13.6.0 Formato',max_length=40)
    ano = models.IntegerField('13.6.5.1 N. Año')
    titulo = models.CharField('13.6.1 Titulo',max_length=60)
    autor = models.CharField('13.6.2 Autor',max_length=60)    
    institucion = models.CharField('13.6.3 Institucion',max_length=40)
    numReferencia = models.IntegerField('13.6.4 N. Referencia')
    isFromAnar = models.BooleanField('13.6.5 ¿Es de ANAR')
    numCopia = models.IntegerField('13.6.5.1 N. Copia')
    videos = models.CharField('Video; ', max_length = 40)

class Video (Grabacion):

    def _unicode_(self):
        return self.titulo

class Pelicula (Grabacion):

    def _unicode_(self):
        return self.titulo

class VideoPiedra (Grabacion):
    piedra = models.ForeignKey(Piedra)
    def _unicode_(self):
        return self.titulo

class PeliculaPiedra (Grabacion):
    piedra = models.ForeignKey(Piedra)
    def _unicode_(self):
        return self.titulo


class MatAudiovisual (MaterialApoyo):

    formato = models.CharField('13.5.1 Formato', max_length=40)
    imagen = models.CharField('13.5.2 Imagen', max_length=40)

class Bibliografia (MaterialApoyo):

    codigo = models.CharField('13.4.0 Codigo', max_length=40)
    titulo = models.CharField('13.4.1 Titulo', max_length=40)
    autor  = models.CharField('13.4.2 Autor ', max_length=40)
    ano = models.IntegerField('13.4.3 Ano')
    institucion  = models.CharField('13.4.2 Institucion ', max_length=40)
    conDibujo = models.BooleanField()

class BibPiedra (MaterialApoyo):
    piedra = models.ForeignKey(Piedra)
    codigo = models.CharField('13.4.0 Codigo', max_length=40)
    titulo = models.CharField('13.4.1 Titulo', max_length=40)
    autor  = models.CharField('13.4.2 Autor ', max_length=40)
    ano = models.IntegerField('13.4.3 Ano')
    institucion  = models.CharField('13.4.2 Institucion ', max_length=40)
    conDibujo = models.BooleanField()

class MapaBibliografia (models.Model):

    OPCIONES_UBICACION_CARA_TRABAJADA = (
        (1, 'Radar'),
        (2, 'Satelital'),
    )
    descripcion  = models.CharField('Descripcion ', max_length=40)
    tipoMapa = models.IntegerField('Tipo de mapa', choices = OPCIONES_UBICACION_CARA_TRABAJADA)
    bibliografia = models.ForeignKey(Bibliografia)

class FotografiaBibliografia (models.Model):

    TIPO_FOTOGRAFIA_BIBLIOGRAFIA = (
        (1, 'Color'),
        (2, 'Blanco y Negro'),
        (3, 'Diapositiva'),
        (4, 'Papel'),
        (5, 'Digital'),
        (6, 'Negativo'),
        (7, 'Antropo-geométricas'),
        (8, 'Zoo-geométricas'),
        (9, 'Amoladores'),
        (10, 'Bateas'),
    )

    tipo = models.IntegerField('Tipo de fotografia', choices = TIPO_FOTOGRAFIA_BIBLIOGRAFIA)

    bibliografia = models.ForeignKey(Bibliografia)


class ReproGraf (MaterialApoyo):

    numPiezas = models.IntegerField('13.2.1 Número de piezas')
    instituto  = models.CharField('13.2.2 Instituto ', max_length=40)
    persona  = models.CharField('13.2.3 Persona ', max_length=40)

class ImagenReproGraf(models.Model):

    reproduccionGrafica = models.ForeignKey(ReproGraf)

class ReproGrafEscalaNaturalPiedra(ReproGraf):
    piedra = models.ForeignKey(Piedra)
    TIPO_REPRODUCCION_GRAFICA_ESCALA_NATURAL = (
        (1, 'Plana'),
        (2, 'Frotage'),
        (3, 'Calco'),
        (4, 'Tridimensional'),
        (5, 'Resina'),
        (6, 'Yeso'),
        (7, 'Papel de arroz'),
    )

    tipoReproduccion = models.IntegerField('Tipo de reproduccion grafica de escala natural', choices = TIPO_REPRODUCCION_GRAFICA_ESCALA_NATURAL)
###
class ReproGrafEscalaRedPied(ReproGraf):
    piedra = models.ForeignKey(Piedra)
    TIPO_REPRODUCCION_GRAFICA_ESCALA_REDUCIDA = (
        (1, 'Dibujo'),
        (2, 'Matriz'),
    )

    tipoReproduccion = models.IntegerField('Tipo de reproduccion grafica de escala reducida', choices = TIPO_REPRODUCCION_GRAFICA_ESCALA_REDUCIDA)   

class ReproGrafEscalaNatural(ReproGraf):

    TIPO_REPRODUCCION_GRAFICA_ESCALA_NATURAL = (
        (1, 'Plana'),
        (2, 'Frotage'),
        (3, 'Calco'),
        (4, 'Tridimensional'),
        (5, 'Resina'),
        (6, 'Yeso'),
        (7, 'Papel de arroz'),
    )

    tipoReproduccion = models.IntegerField('Tipo de reproduccion grafica de escala natural', choices = TIPO_REPRODUCCION_GRAFICA_ESCALA_NATURAL)

class ReproGrafEscalaRed(ReproGraf):

    TIPO_REPRODUCCION_GRAFICA_ESCALA_REDUCIDA = (
        (1, 'Dibujo'),
        (2, 'Matriz'),
    )

    tipoReproduccion = models.IntegerField('Tipo de reproduccion grafica de escala reducida', choices = TIPO_REPRODUCCION_GRAFICA_ESCALA_REDUCIDA)   

class FotografiaPiedra (MaterialApoyo):
    piedra = models.ForeignKey(Piedra)
    TIPO_FOTOGRAFIA = (
        (1, 'Aerea'),
        (2, 'No aerea'),
        (3, 'Satelital'),
    )

    fecha = models.DateField('13.1.1 Fecha')
    fotografo  = models.CharField('13.2.3 Fotografo ', max_length=40)
    institucion  = models.CharField('13.2.3 Institucion ', max_length=40)
    # fotografia  = models.CharField('Fotografia', max_length=40)
    numReferencia = models.IntegerField('13.1.4 Num Referencia')
    numRollo = models.IntegerField('13.1.5 Num Rollo')
    numMarcaNegativo = models.IntegerField('13.1.6 Num Marca Negativo')
    esDeAnar = models.BooleanField('13.1.8 ¿Es de Anar?')
    numCopiaAnar = models.IntegerField('13.1.8.1 Num Copia ANAR')
    tipoFotografia = models.IntegerField('Tipo fotografia', choices = TIPO_FOTOGRAFIA)

class ProspSistPiedra (MecObtInformacion):
    piedra = models.ForeignKey(Piedra)


class ComunicacionPersonalPiedras (MecObtInformacion):

    nombre = models.CharField('14.2.1 Nombre', max_length=40)
    direccion = models.CharField('14.2.2 Direccoin', max_length=150)
    telefono = models.CharField('14.2.3 Telefono/Fax', max_length=16)
    telefonoCel = models.CharField('14.2.3 Telefono celular', max_length=16)
    direccionEmail = models.EmailField('14.2.5 Correo electrónico')
    paginaWeb = models.URLField('14.2.6 Pagina WEB')
    twitter = models.CharField('14.2.7 Twitter', max_length=40)
    nombreFacebook = models.CharField('14.2.8 Nombre de Perfil Facebook', max_length=40)
    blog = models.URLField('14.2.9 Blog')
    fecha = models.DateField('14.2.10 Fecha')

    piedra = models.ForeignKey(Piedra)

class VerificadoEnPiedra(MecObtInformacion):
    piedra = models.ForeignKey(Piedra)



############################################# Fin Clases Piedra #########################################################
