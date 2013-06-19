#coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Definición de los modelos 

class MecObtInformacion (models.Model):
    pass

class ProspeccionSistematica (MecObtInformacion):
    pass

class ComunicacionPersonal (MecObtInformacion):

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

class VerificadoEncampo (MecObtInformacion):
    pass


class DestPotencialSitio (models.Model):

    POSIBLES_CAUSAS_DESTRUCCION_SITIO = (
        (1, u'Asentamiento humano'),
        (2, u'Obra de infraestructura a corto plazo'),
        (3, u'Obra de infraestructura a mediano plazo'),
        (4, u'Obra de infraestructura a largo plazo'),
        (4, u'Nivelacion del terreno como obra agricola'),
        (4, u'Extraccion como actividad familiar'),
        (4, u'Extraccion como actividad mayor'),
        (5, u'Vandalismo'),        
        (6, u'Erosión'),                                        
        (6, u'Erosión parcial moderada'),                                        
        (6, u'Erosión parcial severa'),  
        (6, u'Erosión extensiva moderada'),  
        (6, u'Erosión extensiva severa'),                          
    )
    tipoModificacion =  models.IntegerField('Tipo de destruccion del sitio', choices = POSIBLES_CAUSAS_DESTRUCCION_SITIO)     
    otrasCausasPosibleDestruccion = models.CharField('27.5.1.10 Otras causas posibles de destrucciÃ³n', max_length = 150)


class EstadoConservacion(models.Model):
    OPCIONES_ESTADO_CONSERVACION = (
        (1, u'Bueno'),
        (2, u'Modificado'),
    )

    tipoSitio =  models.IntegerField('Estado de conservacion', choices = OPCIONES_ESTADO_CONSERVACION) 


class Material(models.Model):
    pass

class Roca(Material):

    OPCIONES_ORIGEN_PIEDRA = (
        (1, u'Roca ignea'),
        (2, u'Roca metamÃ³rfica'),
        (3, u'Roca sedimentaria'),
    )

    origenPiedra = models.IntegerField(choices=OPCIONES_ORIGEN_PIEDRA)
    tipo = models.CharField('Tipo de roca', max_length = 150)

class Tierra(Material):
    pass

class Hueso(Material):
    pass

class CortezaArbol(Material):
    pass

class Pieles(Material):
    pass

class Otros(Material):
    especificacion = models.CharField('Otros', max_length = 150)
    pass


class Hidrologia (models.Model):

    OPCIONES_HIDROLOGIA = (
        (1, u'Rio'),
        (2, u'Laguna'),
        (3, u'Arroyo'),
        (4, u'Arroyo Perenne'),
        (5, u'Manantial'),
        (6, u'Manantial intermitente'),
    )

    hidrologia = models.IntegerField('Hidrologia', choices = OPCIONES_HIDROLOGIA)

    otros = models.CharField('Otros', max_length = 150)

    nombre = models.CharField('Nombre', max_length = 150)

    distanciaYacimiento = models.DecimalField('Distancia al yacimiento', max_digits=12, decimal_places=6)

    observaciones = models.CharField('Observaciones', max_length = 400)

class TexturaSuelo (models.Model):

    OPCIONES_TEXTURA_SUELO = (
        (1, u'Roca madre'),
        (2, u'Pedregoso'),
        (3, u'Arenoso'),
        (4, u'Arcilloso'),
        (5, u'Mixto'),
    )

    texturaSuelo = models.IntegerField('Textura suelo', choices = OPCIONES_TEXTURA_SUELO)
    mixto = models.CharField('15.6 Mixto', max_length = 150)

class OrientacionYacimiento (models.Model):

    OPCIONES_ORIENTACION = (
        (1, u'Hacia cerro'),
        (2, u'Hacia valle'),
        (3, u'Hacia rio'),
        (4, u'Hacia costa'),
        (5, u'Hacia cielo'),
    )

    otros = models.CharField('15.6 Otros', max_length = 150)
    orientacionCardinal = models.CharField('15.7 Orientacion cardinal', max_length = 150)
    orientacionYacimiento = models.IntegerField('Orientacion del yacimiento', choices = OPCIONES_ORIENTACION)

class UbicacionYacimiento(models.Model):

    OPCIONES_UBICACION = (
        (1, u'Cerro'),
        (2, u'Cerro: cima'),
        (3, u'Cerro: ladera'),
        (4, u'Cerro: falda'),
        (5, u'Cerro: fila'),
        (6, u'Cerro: pie de monte'),
        (7, u'Cerro: barranco'),
        (8, u'Cerro: acantilado'),
        (9, u'Valle'),
        (10, u'Rio'),
        (11, u'Rio: raudal'),
        (12, u'Rio: isla'),
        (13, u'Rio: margen izquierda'),
        (14, u'Rio: margen derecha'),
        (15, u'Rio: lecho'),
        (16, u'Costa'),
    )

    ubicacion = models.IntegerField(choices = OPCIONES_UBICACION)

class TipoYacimiento(models.Model):
    OPCIONES_TIPO_SITIO = (
        (1, u'Pared rocosa'),
        (2, u'Roca'),
        (3, u'Dolmen'),
        (4, u'Abrigo'),
        (5, u'Cueva'),        
        (6, u'Cueva de recubrimiento'),                
        (7, u'Terreno superficial'),                        
        (8, u'Terreno profundo'),                                
    )  

    tipoSitio =  models.IntegerField('Tipo de Yacimiento', choices = OPCIONES_TIPO_SITIO) 

class MaterialApoyo (models.Model):
    pass

class UsoActualDelSuelo(models.Model):
    OPCIONES_USO_ACTUAL_SUELO = (
        (1, u'Forestal'),
        (2, u'Ganadero'),
        (3, u'Agricultura de riego'),
        (4, u'Agricultura temporal'),
        (5, u'Urbano'),
        (6, u'Turistico'),
    )

    tipoUsoActualSuelo = models.IntegerField('Uso actual del suelo', choices = OPCIONES_USO_ACTUAL_SUELO) 

class TenenciaDeLaTierra(models.Model):

    OPCIONES_TENENCIA_ACTUAL_SUELO = (
        (1, u'Privada'),
        (2, u'Comunal'),
        (3, u'Ejido'),
        (4, u'Municipal'),
        (5, u'ABRAE'),
        (6, u'Otros'),
    )

    otros = models.CharField('Otros', max_length = 150)   
    tipoTenenciaDeLaTierra = models.IntegerField('Tenencia de la tierra', choices = OPCIONES_TENENCIA_ACTUAL_SUELO) 

class Fotografia (MaterialApoyo):
    TIPO_FOTOGRAFIA = (
        (1, 'Aerea'),
        (2, 'No aerea'),
        (3, 'Satelital'),
    )

    fecha = models.DateField('13.1.1 Fecha')
    fotografo  = models.CharField('13.2.3 Fotografo ', max_length=40)
    institucion  = models.CharField('13.2.3 Institucion ', max_length=40)
    fotografia  = models.CharField('Fotografia', max_length=40)
    numReferencia = models.IntegerField('13.1.4 Num Referencia')
    numRollo = models.IntegerField('13.1.5 Num Rollo')
    numMarcaNegativo = models.IntegerField('13.1.6 Num Marca Negativo')
    esDeAnar = models.BooleanField('13.1.8 Â¿Es de Anar?')
    numCopiaAnar = models.IntegerField('13.1.8.1 Num Copia ANAR')
    tipoFotografia = models.IntegerField('Tipo fotografia', choices = TIPO_FOTOGRAFIA)

class ManifestacionesAsociadas (models.Model):

    OPCIONES_MANIFESTACIONES_ASOCIADAS = (
        (1, u'LÃ­tica'),
        (2, u'CerÃ¡mica'),
        (3, u'Oseo'),
        (4, u'CarbÃ³n no superficial'),
        (5, u'Concha'),
        (6, u'Mitos'),
        (7, u'Cementerios'),
        (8, u'Monticulos'),
        (9, u'Otros'),
    )

    manifestacionAsociada = models.IntegerField('Manifestaciones asociadas', choices = OPCIONES_MANIFESTACIONES_ASOCIADAS)    
    otros = models.CharField('Otros', max_length = 150)

class Yacimiento(models.Model):
    OPCIONES_DATUM = (
        (1, 'WGS 84'),
        (2, 'La Canoa - Provisional SuramÃ©rica 1956'),
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
    tipoDatum = models.IntegerField(choices = OPCIONES_DATUM)
    datum = models.CharField(max_length = 150)

    pais = models.CharField('Pais', max_length = 150)
    municipio = models.CharField('Municipio', max_length = 150)    
    estado = models.CharField('Estado', max_length = 150)   

    usoDelSuelo = models.ManyToManyField(UsoActualDelSuelo, blank=True)
    tenenciaDeLatierra = models.ManyToManyField(TenenciaDeLaTierra, blank=True)

    altura =  models.DecimalField('10.1 Altura', max_digits=12, decimal_places=6)
    superficie =  models.DecimalField('10.2 Superficie', max_digits=12, decimal_places=6)

    numeroPlano = models.IntegerField('7. Numero de plano') 

    #This must be changed to a picture.
    indicacionesEsquemaLlegada = models.CharField('6. Indicaciones para llegar al lugar ', max_length = 200) 

    fotografia = models.ManyToManyField(Fotografia, related_name='fotografias_yacimiento', blank=True)

    tipoSitio = models.ManyToManyField(TipoYacimiento, blank=True)

    ubicacionYacimiento = models.ManyToManyField(UbicacionYacimiento, blank=True)
    orientacionYacimiento = models.ManyToManyField(OrientacionYacimiento, blank=True)
    texturaSuelo = models.ManyToManyField(TexturaSuelo, blank=True)
    hidrologia = models.ManyToManyField(Hidrologia, blank=True)

    flora = models.CharField('Flora', max_length = 150)
    fauna = models.CharField('Fauna', max_length = 150)

    materiales = models.ManyToManyField(Material, blank=True)

    OPCIONES_EXPOSICION = (
        (1, u'Expuesto'),
        (2, u'No expuesto'),
        (3, u'Expuesto periodicamente'),
    )

    observacionesExposicion = models.CharField('Observaciones', max_length = 150)

    tipoExposicion = models.IntegerField('Exposicion', choices = OPCIONES_EXPOSICION)

    # Constitucion del yacimiento 

    numPiedrasYacimientoOriginal = models.IntegerField('Numero de piedras en el yacimiento original')
    numPiedrasYacimientoGrabadas = models.IntegerField('Numero de piedras grabadas.')
    numPiedrasYacimientoPintadas = models.IntegerField('Numero de piedras pintadas.')
    numPiedrasYacimientoColocadas = models.IntegerField('Numero de piedras colocadas.')

    otrosConstitucionYacimiento = models.CharField('Otras caracterÃ­sticas de la constitucion yacimiento', max_length = 150)

    otrasNotas = models.CharField('2.6.10 Notas', max_length = 150)

    estadoConservacion = models.ManyToManyField(EstadoConservacion, blank=True)
    destruccionPotencialSitio = models.ManyToManyField(DestPotencialSitio, blank=True)    

    observacionesDestruccion = models.CharField('Observaciones sobre intensidad de destruccion del sitio y otros procesos no descritos.', max_length = 150)

    OPCIONES_TIEMPO_DESTRUCCION = (
        (1, u'Inmediato'),
        (2, u'1 aÃ±o'),
        (3, u'2 aÃ±os'),
        (4, u'3 aÃ±os'),
        (5, u'4 aÃ±os'),
        (6, u'5 aÃ±os'),
        (7, u'Mas'),
    )

    tiempoDestruccion = models.IntegerField('Opciones tiempo destruccion', choices = OPCIONES_TIEMPO_DESTRUCCION)    

    manifestacionesAsociadas = models.ManyToManyField(ManifestacionesAsociadas, blank=True)    

    materialesApoyo = models.ManyToManyField(MaterialApoyo, blank=True)

    mecanismosObtencionInformacion = models.ManyToManyField(MecObtInformacion, blank=True)

    otrosValoresSitio = models.CharField('Otros valores del sitio', max_length = 150)

    def __unicode__(self):
        return 'PB1-' +  '-' + self.nombre #self.codigo + '-' + self.nombre



class CronologiaTentativa (models.Model):
    POSIBLES_CRONOLOGIAS = (
        (1, u'Anterior a 5000 a.p.'),
        (2, u'5000-1500 a.p'),
        (3, u'1500.a.p. - 200 n.e'),
        (4, u'200-650/900 n.e.'),
        (5, u'650/900-1200 n.e'),
        (6, u'1200-1521 n.e.'),
        (7, u'Post 1521 n.e.'),
    )

    cronologia =  models.IntegerField('CronologÃ­a tentativa', choices = POSIBLES_CRONOLOGIAS)     
    autor = models.CharField('Autor', max_length = 150)
    fecha = models.DateField('Fecha de la cronologÃ­a')

    institucion = models.CharField('Institucion', max_length = 150)
    pais = models.CharField('Pais', max_length = 150)
    direccion = models.CharField('Direccion', max_length = 150)
    telefono = models.CharField('Telefono', max_length = 150)
    email = models.CharField('Email', max_length = 150)
    
    yacimiento = models.ForeignKey(Yacimiento)

class GradoDestruccionSitio(models.Model):
    OPCIONES_TIPO_DESTRUCCION = (
        (1, u'Natural'),
        (2, u'Natural ligera'),
        (3, u'Natural aguda'),
        (4, u'Humana'),
        (5, u'Humana ligera'),        
        (6, u'Humana aguda'),                                        
    )

    causaYEfecto = models.CharField('Causa y efecto', max_length = 150)
    tipoModificacion =  models.IntegerField('Tipo de destruccion del sitio', choices = OPCIONES_TIPO_DESTRUCCION)     
    yacimiento = models.ForeignKey(Yacimiento)

class ModificacionYacimiento(models.Model):
    OPCIONES_TIPO_MODIFICACION = (
        (1, u'Traslado'),
        (2, u'Sumergido'),
        (3, u'Enterrado'),
        (4, u'Perdido'),
        (5, u'Destruido'),        
        (6, u'Crecimiento vegetal'),                
        (7, u'PÃ¡tina'),                        
        (8, u'ErosiÃ³n'),                                
    )  

    yacimiento = models.ForeignKey(Yacimiento)
    tipoModificacion =  models.IntegerField('Tipo de modificaciÃ³n', choices = OPCIONES_TIPO_MODIFICACION)     
    tipo = models.IntegerField('Tipo de modificacion (1 - ambiental, 2 - artificial)')
    pas = models.CharField('Codigo de las piedras', max_length = 150)


class LocalidadYacimiento(models.Model):
    yacimiento = models.ForeignKey(Yacimiento)
    nombreLocalidad = models.CharField('Nombre', max_length = 150)   

class LocalidadYacimientoPoblado(LocalidadYacimiento):
    OPCIONES_TIPO_CENTRO_POBLADO = (
        (1, u'Urbano'),
        (2, u'Rural'),
        (3, u'IndÃ­gena'),
        (4, u'Otro')
    )  

    tipoCentroPoblado = models.IntegerField('Tipo de Centro Poblado', choices = OPCIONES_TIPO_CENTRO_POBLADO) 

class LocYacNoPoblado(LocalidadYacimiento):
    pass


# Diagrama de manifestacion

class TipoManifestacion(models.Model):
    pass

class Geoglifo(TipoManifestacion):
    tecnicaConstruccion = models.CharField('TÃ©cnica de ConstrucciÃ³n', max_length = 150)

class TipoLinea(models.Model):
    anchoLineaDesde = models.IntegerField()
    anchoLineaHasta = models.IntegerField()
    pass

class LineaSencilla (TipoLinea):
    pass

class LineaCompuesta (TipoLinea):
    pass

class TecnicaPinturaRupestre(models.Model):
    TECNICA_PINTURA = (
        (1, u'Dactilar'),
        (2, u'Fibra'),
        (3, u'Otros')
    )
    tecnica = models.IntegerField(choices=TECNICA_PINTURA)
    otro = models.CharField('Otra tecnica de pintura', max_length = 150)

class Color (models.Model):
    parametroC = models.CharField('C', max_length=20)
    parametroM = models.CharField('M', max_length=20)
    parametroY = models.CharField('Y', max_length=20)
    parametroK = models.CharField('K', max_length=20)
# Falta implementar positiva, negativa, color_base


class ImpresionDeManos(models.Model):
    OPCIONES_IMPRESION_MANOS = (
        (1, u'Positivo'),
        (2, u'Negativo'),
    )

    tecnica = models.IntegerField(choices=OPCIONES_IMPRESION_MANOS)

class CaracDeLaPintura(models.Model):
    tecnicas = models.ManyToManyField(TecnicaPinturaRupestre)
    impresionDeManos = models.ManyToManyField(ImpresionDeManos)
    figuraRellena = models.BooleanField()
    figurasSuperPuestas = models.BooleanField()
    colores = models.ManyToManyField(Color)
    tipoDeLineas = models.ManyToManyField (TipoLinea)
    colorBase = models.CharField('Color base (areas interlineales)', max_length = 150)

class Positivo(ImpresionDeManos):
    planoNegro = models.IntegerField('Plano negro')
    planoBlanco = models.IntegerField('Plano blanco')
    planoAmarillo = models.IntegerField('Plano amarillo')
    planoUnRojo = models.IntegerField('Plano un rojo')
    planoDosRojo = models.IntegerField('Plano dos rojos')
    planoTresRojo = models.IntegerField('Plano tres rojos')
    caracteristicasPinturaRupestre = models.ForeignKey(CaracDeLaPintura)

class Negativo(ImpresionDeManos):
    planoNegro = models.IntegerField('Plano negro')
    planoBlanco = models.IntegerField('Plano blanco')
    planoAmarillo = models.IntegerField('Plano amarillo')
    planoUnRojo = models.IntegerField('Plano un rojo')
    planoDosRojo = models.IntegerField('Plano dos rojos')
    planoTresRojo = models.IntegerField('Plano tres rojos')
    caracteristicasPinturaRupestre = models.ForeignKey(CaracDeLaPintura)

class PinturaRupestre(TipoManifestacion):
    descripcion = models.CharField('DescripciÃ³n', max_length = 150)
    caracteristicas = models.ManyToManyField(CaracDeLaPintura)
    
class TecnicaPetroglifo(models.Model):
    TECNICA_PETROGLIFO = (
        (1, u'1. Grabado'),
        (2, u'1.1 Percusion'),
        (2, u'1.1.1 Percusion directa'),
        (3, u'1.1.1 Percusion indirecta'),
        (3, u'1.2 Abrasion'),
        (3, u'1.2.1 Abrasion con piedra'),
        (3, u'1.2.2 Abrasion con arena'),
        (3, u'1.2.3 Abrasion con concha'),
        (3, u'Otros')
    )
    material = models.IntegerField(choices=TECNICA_PETROGLIFO)
    otro = models.CharField('Otra tecnica', max_length = 150)

class CaracDePetroglifo(models.Model):

    OPCIONES_CARACTERISTICAS_SURCO_PETROGLIFO = (
        (1, u'24.3 Base'),
        (2, u'24.3.1 Base redonda'),
        (3, u'24.3.2 Base aguda'),

        (4, u'24.4 Bajo relieve'),
        (5, u'24.4.1 Bajo relieve lineal'),
        (6, u'24.4.2 Bajo relieve planar'),

        (7, u'24.5 Alto relieve'),
        (8, u'24.5.1 Alto relieve lineal'),
        (9, u'24.5.2 Alto relieve planar'),

        (10, u'24.6 Areas interlineales'),
        (11, u'24.6.1 Areas interlineales pulidas'),
        (12, u'24.6.2 Areas interlineales rebajadas'),

        (13, u'24.7 Grabados superpuestos'),
        (14, u'24.8 Grabados rebajados')
       
    )

    caracteristicasSurcoGrabado = models.IntegerField(choices=OPCIONES_CARACTERISTICAS_SURCO_PETROGLIFO)

class Petroglifo(TipoManifestacion):

    pintado = models.BooleanField()
    tecnicas = models.ManyToManyField(TecnicaPetroglifo)
    caracteristicasPetroglifo = models.ManyToManyField(CaracDePetroglifo)

    anchoMinimo =  models.DecimalField('24.1 Ancho Minimo', max_digits=12, decimal_places=6)
    anchoMaximo =  models.DecimalField('24.1 Ancho Maximo', max_digits=12, decimal_places=6)

    profundidadMinima =  models.DecimalField('24.2 Profundidad Minima', max_digits=12, decimal_places=6)
    profundidadMaxima =  models.DecimalField('24.2 Profundidad Maxima', max_digits=12, decimal_places=6)


class MicroPetroglifo(TipoManifestacion):
    pass

class PiedriaMiticaNatural(TipoManifestacion):
    pass

class CerroMiticoNatural(TipoManifestacion):
    conPetroglifo = models.BooleanField()
    conPintura = models.BooleanField()
    conDolmen = models.BooleanField()

class MonumentoMegalitico(TipoManifestacion):
    pass

class Monolito(MonumentoMegalitico):
    cantidadDeMonolitos = models.IntegerField('Cantidad de monolitos')
    cantidadDeMonolitosGrabados = models.IntegerField('Cantidad de monolitos grabados')

class Menhir(MonumentoMegalitico):
    cantidadPiedrasVerticales = models.IntegerField('Cantidad de piedras verticales')
    cantidadConPuntosAcoplados = models.IntegerField('Cantidad de menhires con puntos acoplados')
    cantidadConPetroglifos = models.IntegerField('Cantidad de menhires con petroglifos')
    cantidadConPinturas = models.IntegerField('Cantidad de menhires con pinturas')

    distanciamiento =  models.DecimalField('Distanciamiento', max_digits=12, decimal_places=6)

class Dolmen(MonumentoMegalitico):
    cantidadConPetroglifos = models.IntegerField('Cantidad de menhires con petroglifos')
    cantidadConPinturas = models.IntegerField('Cantidad de menhires con pinturas')

class Amolador(TipoManifestacion):
    largo =  models.DecimalField('24.9 Largo', max_digits=12, decimal_places=6)
    ancho =  models.DecimalField('24.10 Ancho', max_digits=12, decimal_places=6)
    diametro =  models.DecimalField('24.11 Diametro', max_digits=12, decimal_places=6)
    pass

class Batea(TipoManifestacion):    
    largo =  models.DecimalField('24.12 Largo', max_digits=12, decimal_places=6)
    ancho =  models.DecimalField('24.13 Ancho', max_digits=12, decimal_places=6)
    pass

class PuntosAcoplados(TipoManifestacion):    
    punteado = models.BooleanField('24.14 Punteado')
    pass

class Cupulas(TipoManifestacion):    
    largo =  models.DecimalField('24.15 Largo', max_digits=12, decimal_places=6)
    ancho =  models.DecimalField('24.16 Ancho', max_digits=12, decimal_places=6)
    diametro =  models.DecimalField('24.17 Diametro', max_digits=12, decimal_places=6)
    pass

class Mortero(TipoManifestacion):    
    largo =  models.DecimalField('24.18 Largo', max_digits=12, decimal_places=6)
    ancho =  models.DecimalField('24.19 Ancho', max_digits=12, decimal_places=6)    
    pass












########################################################################################
# Diagrama de piedra
########################################################################################


class Piedra(models.Model):

    CONEXION_FIGURAS = (
        (1, '1 - Presencia de una sola figura'),
        (2, '2 - Menos del 10% interconectadas'),
        (3, '3 - 50% interconectadas'),
        (4, '4 - Mas del 80% interconectadas'),
    )

    """Representa la información de la ficha pa, recoge la información básica"""

    yacimiento = models.ForeignKey(Yacimiento)
    codigo = models.CharField('0. Codigo de la piedra', max_length=20)#, primary_key=True)        
    nombre = models.CharField('1. Nombre de la piedra', max_length=150)
    manifiestacionAsociada = models.CharField('1.1 Manifestaciones asociadas', max_length=150)
    nombreFiguras = models.CharField('2. Nombre de las figuras',max_length=150)
    estado= models.CharField('3. Estado',max_length=40)    
    numeroCaras = models.IntegerField('4. Numero de Caras')
    numeroCarasTrajabadas = models.IntegerField('5. Numero de caras trabajadas')

    conexionFiguras = models.IntegerField('11. Conexion de figuras', choices = CONEXION_FIGURAS)
    
    otrosValoresDeLaPiedra = models.CharField('15. Otros valores de la piedra',max_length=150)
    observaciones = models.CharField('16. Observaciones',max_length=150)
 
    def __unicode__(self):
        return 'Pa-' + self.codigo + '-' + self.nombre

class DimensionPiedra(models.Model):

    """Representa la información de las dimensiones de la piedra"""

    piedra = models.ForeignKey(Piedra)
    altoMaximo =  models.DecimalField('7.a Alto Maximo', max_digits=12, decimal_places=6)
    largoMaximo = models.DecimalField('7.b Largo Maximo',max_digits=12, decimal_places=6)
    anchoMaximo = models.DecimalField('7.c Ancho Maximo',max_digits=12, decimal_places=6)
    
    class Meta:
        verbose_name = 'Dimensiones de la piedra'
        verbose_name_plural = '7. Dimensiones de la piedra'

class FichaPiedra(models.Model):

    """Representa la información de la ficha pa, recoge los datos de
    las personas que llenaron la ficha"""

    piedra = models.ForeignKey(Piedra)    
    autor = models.CharField('17a. Ficha llenada por', max_length=40)
    fechaLlenado = models.DateField('17b. Fecha llenado', blank = True)
    supervisor = models.CharField('18a. Ficha supervisada por', max_length=40)
    fechaSupervision = models.DateField('18b. Fecha supervisión', blank = True)
    
    class Meta:
        verbose_name = 'Llenado de la ficha'
        verbose_name_plural = '17-18. Llenado de la ficha'


class CaraTrabajada(models.Model):

    """Representa la información de la ficha pa, referente a las caras trabajadas """
    
    ORIENTACION_CARA_TRABAJADA = (
        (0, '0 - Tope'),
        (1, '1 - Norte'),
        (2, '2 - Noreste'),
        (3, '3 - Este'),
        (4, '4 - Sureste'),
        (5, '5 - Sur'),
        (6, '6 - Suroeste'),
        (7, '7 - Oeste'),
        (8, '8 - Noroeste'),
        (9, '9 - Piso o plano inclinado'),
    )

    piedra = models.ForeignKey(Piedra)
    numero = models.IntegerField('6a. Número de cara trabajada')
    orientacion = models.IntegerField('6b. Orientación de la cara', choices = ORIENTACION_CARA_TRABAJADA)
    alto = models.DecimalField('7.1. Alto',max_digits=6, decimal_places=3)
    ancho = models.DecimalField('7.2. Ancho',max_digits=6, decimal_places=3)
    largo = models.DecimalField('7.3. Largo',max_digits=6, decimal_places=3)

    class Meta:
        verbose_name = 'Cara trabajada'
        verbose_name_plural = '6-7. Caras trabajadas'

class UbicacionCaras(models.Model):

    """Representa la información de la ficha pa, referente a la ubicacion
    de las  caras trabajadas """

    LUMINOSIDAD = (
        (0, 'No tiene'),
        (1, 'Fótico'),
        (2, 'Escótico'),
    )

    piedra = models.ForeignKey(Piedra)
    todaLaCaverna = models.BooleanField('8.1. Toda la caverna')
    areasEspecificas = models.BooleanField('8.2. Áreas específicas')
    salaPrincipal = models.BooleanField('8.2.1. Sala principal')
    otraSala = models.BooleanField('8.2.2. Otra sala')
    lagoInterior = models.BooleanField('8.2.3. Lago interior')
    claraboya = models.BooleanField('8.2.4. Claraboya')

    bocaPrincipal = models.DecimalField('8.3. Distancia Boca Principal',max_digits=12, decimal_places=6)
    luminosidad = models.IntegerField('8.3.1. Luminosidad', choices = LUMINOSIDAD)
    altura = models.DecimalField('8.3.2. Altura',max_digits=6, decimal_places=3)   
    requiereAndamiaje = models.BooleanField('8.3.2.1. ¿Requiere andamiaje?')
    
    class Meta:
        verbose_name = 'Ubicación de cara trabajada'
        verbose_name_plural = '8. Ubicación de caras trabajadas'
        

class FigurasPorTipo(models.Model):

    """Representa la información de la ficha pa, referente a los conjuntos de
    figuras por tipo presentes en cada cara"""

    TIPO_FIGURA = (
        (1, '1 - Antropomorfas'),
        (2, '2 - Zoomorfas'),
        (3, '3 - Geométricas'),
        (4, '4 - Puntos Acoplados'),
        (5, '5 - Cupulas'),
        (6, '6 - Zoo-antropomorfas'),
        (7, '7 - Antropo-geométricas'),
        (8, '8 - Zoo-geométricas'),
        (9, '9 - Amoladores'),
        (10, '10 - Bateas'),
    )

    piedra = models.ForeignKey(Piedra)
    numero = models.IntegerField('9a. Número de cara trabajada')
    tipoFigura = models.IntegerField('9b. Tipo de figura',choices = TIPO_FIGURA)
    cantidad =  models.IntegerField('9c. Cantidad')
    descripcion = models.CharField('9d. Descripcion',max_length=150) 
    
    class Meta:
        verbose_name = 'Conjunto de figuras por Tipo'
        verbose_name_plural = '9. Conjuntos de figuras por tipo'
    

class EsquemaPorCara(models.Model):

    """Representa la información de la ficha pa, referente al esquema
    de la cara de la piedra"""

    piedra = models.ForeignKey(Piedra)
    numero = models.IntegerField('10a. Número de cara trabajada')
    textoCara = models.CharField('10b. Cara',max_length=150) 
    posicion = models.CharField('10c. Posicion de las figuras en la cara',max_length=150) 

    class Meta:
        verbose_name = 'Esquema por cara'
        verbose_name_plural = '10. Esquemas por caras'


class Manifestaciones(models.Model):

    """Representa la información de la ficha pa, indicando el tipo de manifestacion"""

    piedra = models.ForeignKey(Piedra)
    tienePetroglifo = models.BooleanField('¿Tiene Petroglifos?')
    tienePinturaRupestre = models.BooleanField('¿Tiene Pintura Rupestre?')
    tieneAmoladores = models.BooleanField('¿Tiene Amoladores?')
    tienePuntosAcoplados = models.BooleanField('¿Tiene Puntos Acoplados?')
    tieneCupulas = models.BooleanField('¿Tiene Cupulas?')
    
    class Meta:
        verbose_name = 'Manifestaciones de la piedra'
        verbose_name_plural = 'X. Manifestaciones de la piedra'

class TratFoto(models.Model):

    """Representa la información de la ficha pa, referente al tratamiento fotografico dado
    a las fotografias recopiladas"""
    
    piedra = models.ForeignKey(Piedra)
    limpiezaCon = models.CharField('12.1. Limpieza con', max_length = 40)
    rellenoSurcos = models.CharField('12.2. Relleno de surcos con', max_length = 40)
    tratamientoDigital = models.CharField('12.3. Tratamiento digital', max_length = 40)
    programaVersion = models.CharField('12.4. Programa/versión', max_length = 40)
    otrosTratamientos = models.CharField('12.5. Otros tratamientos fotografía', max_length = 150)

    class Meta:
        verbose_name = 'Tratamiento para fotografías'
        verbose_name_plural = '12. Tratamiento para fotografías'


class InfoFoto(models.Model):

    """Representa la información de la ficha pa, referente a las fotografias"""
    
    TIPO_FOTOGRAFIA = (
        (1, 'a - Aérea'),
        (2, 'b - No aérea'),
        (3, 'c - Satelital'),
    )

    piedra = models.ForeignKey(Piedra)
    negativo  = models.CharField('13.1a. Negativo ', max_length=100)
    tipo = models.IntegerField('13.1b. Tipo fotografía', choices = TIPO_FOTOGRAFIA)
    fecha = models.DateField('13.1.1. Fecha')
    fotografo  = models.CharField('13.1.2. Fotógrafo ', max_length=100)
    institucion  = models.CharField('13.1.3. Institución ', max_length=100)
    numReferencia = models.CharField('13.1.4. Nro. Referencia', max_length=100)
    numRollo = models.CharField('13.1.5. Nro. Rollo', max_length=100)
    numFoto = models.CharField('13.1.6. Nro. foto', max_length=100)
    numMarcaNegativo = models.CharField('13.1.7. Nro. Marca en Negativo', max_length=100)
    esDeAnar = models.BooleanField('13.1.8. ¿Es de Anar?')
    numCopiaAnar = models.IntegerField('13.1.8.1 Num Copia ANAR')

    class Meta:
        verbose_name = 'Información de Fotografía'
        verbose_name_plural = '13.1. Información de Fotografías'

        
class MatApoyoPiedra(models.Model):

    """Representa la información de la ficha pa, agrupa los distintos tipos
    de materiales de apoyo y las demás clases descienden de el """
    
    piedra = models.ForeignKey(Piedra)

class FotoDigital(MatApoyoPiedra):

    """Representa la información de la ficha pa, referente a los archivos
    de fotografías"""
    
    class Meta:
        verbose_name = 'Fotografía Digitalizada'
        verbose_name_plural = '13.1. Fotografías Digitalizadas'

class ReproGraf (MatApoyoPiedra):

    """Representa la información de la ficha pa, agrupa los distintos tipos
    de reproducciones gráficas a escala natural y reducida"""

    numPiezas = models.IntegerField('1a. Número de piezas')
    instituto  = models.CharField('1b. Institución ', max_length=40)
    persona  = models.CharField('1c. Persona ', max_length=40)
          
class EscalaNatPiedra(ReproGraf):

    TIPO_REPRODUCCION_NATURAL = (
        (1, '1 - Plana'),
        (2, '2 - Frotage'),
        (3, '3 - Calco'),
        (4, '4 - Tridimensional'),
        (5, '5 - Resina'),
        (6, '6 - Yeso'),
        (7, '7 - Papel de arroz'),
    )
    tipoReproduccion = models.IntegerField('13.2.1. Reproducción gráfica', choices = TIPO_REPRODUCCION_NATURAL)

    class Meta:
        verbose_name = 'Reproducción gráf. escala natural'
        verbose_name_plural = '13.2. Reproducción gráf. escala natural'

class EscalaRedPiedra(ReproGraf):

    """Representa la información de la ficha pa, de reproducciones gráficas
    a escala reducida"""
        
    TIPO_REPRODUCCION_REDUCIDA = (
        (1, '1 - Dibujo'),
        (2, '2 - Matriz'),
    )
    tipoReproduccion = models.IntegerField('13.3.1. Reproducción gráfica', choices = TIPO_REPRODUCCION_REDUCIDA)

    class Meta:
        verbose_name = 'Reproducción gráf. escala natural'
        verbose_name_plural = '13.3. Reproducción gráf. escala reducida'

class BibPiedra(MatApoyoPiedra):

    """Representa la información de la ficha pa, con respecto a su bibliografia"""

    codigo = models.CharField('13.4.0. Código', max_length=100)
    titulo = models.CharField('13.4.1. Título', max_length=100)
    autor  = models.CharField('13.4.2. Autor ', max_length=100)
    ano = models.IntegerField('13.4.3. Año')
    institucion  = models.CharField('13.4.4. Institución', max_length=100)
    conDibujo = models.CharField('13.4.5. Con dibujo', max_length=100)

    class Meta:
        verbose_name = 'Apoyo - Bibliografía'
        verbose_name_plural = '13.4. Bibliografía'


class FotoBibPiedra (MatApoyoPiedra):

    """Representa la información de la ficha pa, con respecto a
    las fotografías incluidas en la bibliografia"""

    TIPO_MAPA = (
        (1, '1 - Radar'),
        (2, '2 - Satelital'),
    )
        
    esFotografia = models.BooleanField('13.4.6. Con fotografía')
    escolor = models.BooleanField('a. Color')
    esBlancoYNegro = models.BooleanField('b. Blanco y Negro')
    esDiapositiva = models.BooleanField('c. Diapositiva')
    esPapel = models.BooleanField('d. Papel')
    esDigital = models.BooleanField('e. Digital')
    esNegativo = models.BooleanField('f. Negativo')
    descripcion  = models.CharField('g. Con mapa ', max_length=100)
    tipoMapa = models.IntegerField('h. Tipo de mapa', choices = TIPO_MAPA)

    class Meta:
        verbose_name = 'Bibliografía fotográfica'
        verbose_name_plural = '13.4.6. Bibliografía fotográfica'
 
########################################################################################
# Fin Diagrama de piedra 
########################################################################################

class RecursoMultimedia (MaterialApoyo):

    tecnica = models.CharField('13.4.1 TÃ©cnica',max_length=150) 
    imagen = models.CharField(max_length=150) # models.ImageField()

class PaginaWEB (MaterialApoyo):
    piedra = models.ForeignKey(Piedra)
    direccionURL = models.URLField ('13.8 PÃ¡gina Web')

class Grabacion (MaterialApoyo):

    formato = models.CharField('13.6.0 Formato',max_length=40)
    ano = models.IntegerField('13.6.5.1 N. AÃ±o')
    titulo = models.CharField('13.6.1 Titulo',max_length=60)
    autor = models.CharField('13.6.2 Autor',max_length=60)    
    institucion = models.CharField('13.6.3 Institucion',max_length=40)
    numReferencia = models.IntegerField('13.6.4 N. Referencia')
    isFromAnar = models.BooleanField('13.6.5 ¿Es de ANAR?')
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












class ImagenReproGraf(models.Model):

    reproduccionGrafica = models.ForeignKey(ReproGraf)



class ProspSistPiedra (MecObtInformacion):
    piedra = models.ForeignKey(Piedra)


class ComunicacionPersonalPiedras (MecObtInformacion):

    nombre = models.CharField('14.2.1 Nombre', max_length=40)
    direccion = models.CharField('14.2.2 Direccoin', max_length=150)
    telefono = models.CharField('14.2.3 Telefono/Fax', max_length=16)
    telefonoCel = models.CharField('14.2.3 Telefono celular', max_length=16)
    direccionEmail = models.EmailField('14.2.5 Correo electrÃ³nico')
    paginaWeb = models.URLField('14.2.6 Pagina WEB')
    twitter = models.CharField('14.2.7 Twitter', max_length=40)
    nombreFacebook = models.CharField('14.2.8 Nombre de Perfil Facebook', max_length=40)
    blog = models.URLField('14.2.9 Blog')
    fecha = models.DateField('14.2.10 Fecha')

    piedra = models.ForeignKey(Piedra)

class VerificadoEnPiedra(MecObtInformacion):
    piedra = models.ForeignKey(Piedra)
