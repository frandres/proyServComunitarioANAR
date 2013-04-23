#coding: latin-1

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class MecanismoObtencionInformacion (models.Model):
    pass

class ProspeccionSistematica (MecanismoObtencionInformacion):

    def _unicode_(self):
        return self.piedra

class ComunicacionPersonal (MecanismoObtencionInformacion):

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

class VerificadoEncampo (MecanismoObtencionInformacion):
    
    def _unicode_(self):
        return self.piedra


class DestruccionPotencialSitio (models.Model):

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
    otrasCausasPosibleDestruccion = models.CharField('27.5.1.10 Otras causas posibles de destrucción', max_length = 150)


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
        (2, u'Roca metamórfica'),
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
    esDeAnar = models.BooleanField('13.1.8 ¿Es de Anar?')
    numCopiaAnar = models.IntegerField('13.1.8.1 Num Copia ANAR')
    tipoFotografia = models.IntegerField('Tipo fotografia', choices = TIPO_FOTOGRAFIA)

class ManifestacionesAsociadas (models.Model):

    OPCIONES_MANIFESTACIONES_ASOCIADAS = (
        (1, u'Lítica'),
        (2, u'Cerámica'),
        (3, u'Oseo'),
        (4, u'Carbón no superficial'),
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
    tipoDatum = models.IntegerField(choices = OPCIONES_DATUM)
    datum = models.CharField(max_length = 150)

    pais = models.CharField('Pais', max_length = 150)
    municipio = models.CharField('Municipio', max_length = 150)    
    estado = models.CharField('Estado', max_length = 150)   

    usoDelSuelo = models.ManyToManyField(UsoActualDelSuelo)
    tenenciaDeLatierra = models.ManyToManyField(TenenciaDeLaTierra)

    altura =  models.DecimalField('10.1 Altura', max_digits=12, decimal_places=6)
    superficie =  models.DecimalField('10.2 Superficie', max_digits=12, decimal_places=6)

    numeroPlano = models.IntegerField('7. Numero de plano') 

    #This must be changed to a picture.
    indicacionesEsquemaLlegada = models.CharField('6. Indicaciones para llegar al lugar ', max_length = 200) 

    fotografia = models.ManyToManyField(Fotografia, related_name='fotografias_yacimiento')

    tipoSitio = models.ManyToManyField(TipoYacimiento)

    def _unicode_(self):
        return self.nombre

    ubicacionYacimiento = models.ManyToManyField(UbicacionYacimiento)
    orientacionYacimiento = models.ManyToManyField(OrientacionYacimiento)
    texturaSuelo = models.ManyToManyField(TexturaSuelo)
    hidrologia = models.ManyToManyField(Hidrologia)

    flora = models.CharField('Flora', max_length = 150)
    fauna = models.CharField('Fauna', max_length = 150)

    materiales = models.ManyToManyField(Material)

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

    otrosConstitucionYacimiento = models.CharField('Otras características de la constitucion yacimiento', max_length = 150)

    otrasNotas = models.CharField('2.6.10 Notas', max_length = 150)

    estadoConservacion = models.ManyToManyField(EstadoConservacion)
    destruccionPotencialSitio = models.ManyToManyField(DestruccionPotencialSitio)    

    observacionesDestruccion = models.CharField('Observaciones sobre intensidad de destruccion del sitio y otros procesos no descritos.', max_length = 150)

    OPCIONES_TIEMPO_DESTRUCCION = (
        (1, u'Inmediato'),
        (2, u'1 año'),
        (3, u'2 años'),
        (4, u'3 años'),
        (5, u'4 años'),
        (6, u'5 años'),
        (7, u'Mas'),
    )

    tiempoDestruccion = models.IntegerField('Opciones tiempo destruccion', choices = OPCIONES_TIEMPO_DESTRUCCION)    

    manifestacionesAsociadas = models.ManyToManyField(ManifestacionesAsociadas)    

    materialesApoyo = models.ManyToManyField(MaterialApoyo)

    mecanismosObtencionInformacion = models.ManyToManyField(MecanismoObtencionInformacion)

    otrosValoresSitio = models.CharField('Otros valores del sitio', max_length = 150)


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

    cronologia =  models.IntegerField('Cronología tentativa', choices = POSIBLES_CRONOLOGIAS)     
    autor = models.CharField('Autor', max_length = 150)
    fecha = models.DateField('Fecha de la cronología')

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
        (7, u'Pátina'),                        
        (8, u'Erosión'),                                
    )  

    yacimiento = models.ForeignKey(Yacimiento)
    tipoModificacion =  models.IntegerField('Tipo de modificación', choices = OPCIONES_TIPO_MODIFICACION)     
    tipo = models.IntegerField('Tipo de modificacion (1 - ambiental, 2 - artificial)')
    pas = models.CharField('Codigo de las piedras', max_length = 150)


class LocalidadYacimiento(models.Model):
    yacimiento = models.ForeignKey(Yacimiento)
    nombreLocalidad = models.CharField('Nombre', max_length = 150)   

class LocalidadYacimientoPoblado(LocalidadYacimiento):
    OPCIONES_TIPO_CENTRO_POBLADO = (
        (1, u'Urbano'),
        (2, u'Rural'),
        (3, u'Indígena'),
        (4, u'Otro')
    )  

    tipoCentroPoblado = models.IntegerField('Tipo de Centro Poblado', choices = OPCIONES_TIPO_CENTRO_POBLADO) 

class LocalidadYacimientoNoPoblado(LocalidadYacimiento):
    pass


# Diagrama de manifestacion

class TipoManifestacion(models.Model):
    pass

class Geoglifo(TipoManifestacion):
    tecnicaConstruccion = models.CharField('Técnica de Construcción', max_length = 150)

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

class CaracteristicasDeLaPintura(models.Model):
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
    caracteristicasPinturaRupestre = models.ForeignKey(CaracteristicasDeLaPintura)

class Negativo(ImpresionDeManos):
    planoNegro = models.IntegerField('Plano negro')
    planoBlanco = models.IntegerField('Plano blanco')
    planoAmarillo = models.IntegerField('Plano amarillo')
    planoUnRojo = models.IntegerField('Plano un rojo')
    planoDosRojo = models.IntegerField('Plano dos rojos')
    planoTresRojo = models.IntegerField('Plano tres rojos')
    caracteristicasPinturaRupestre = models.ForeignKey(CaracteristicasDeLaPintura)



class PinturaRupestre(TipoManifestacion):
    descripcion = models.CharField('Descripción', max_length = 150)
    caracteristicas = models.ManyToManyField(CaracteristicasDeLaPintura)
    
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

class CaracteristicasDePetroglifo(models.Model):

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
    caracteristicasPetroglifo = models.ManyToManyField(CaracteristicasDePetroglifo)

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

class PosibleUbicacionCarasTrajabadas(models.Model): # Enumeration (N)

    OPCIONES_UBICACION_CARA_TRABAJADA = (
        (1, 'En toda la caverna'),
        (2, 'En áreas específicas'),
        (3, 'Sala Principal'),
        (4, 'Otra sala'),
        (5, 'Lago interior'),
        (6, 'Claraboya'),
        (7, 'Luminosidad'),
    )

    ubic = models.IntegerField(choices = OPCIONES_UBICACION_CARA_TRABAJADA)

class  ManifestacionesEnCarasTrabajadas(models.Model):

    OPCIONES_MANIFESTACIONES_EN_CARAS_TRABAJADAS = (
        (0, 'Petroglifo'),
        (1, 'Pintura Rupestre'),
        (2, 'Amoladores'),
        (3, 'Puntos Acoplados'),
        (4, 'Cupulas'),
    )

    manif = models.IntegerField(choices = OPCIONES_MANIFESTACIONES_EN_CARAS_TRABAJADAS)

# Diagrama de piedra

class Piedra(models.Model):

    yacimiento = models.ForeignKey(Yacimiento)
    codigo = models.CharField('0. Codigo de la piedra', max_length=20)#, primary_key=True)        
    nombre = models.CharField('1. Nombre de la piedra', max_length=150)
    manifiestacionAsociada = models.CharField('1.1 Manifestaciones Asociadas', max_length=150)
    nombreFiguras = models.CharField('2. Nombre Figuras',max_length=150)
    estado= models.CharField('3. Estado',max_length=40)
    
    numeroCaras = models.IntegerField('Numero de Caras')
    numeroCarasTrajabadas = models.IntegerField('Numero de caras trabajadas')
    altoMaximo =  models.DecimalField('7.a Alto Maximo', max_digits=12, decimal_places=6)
    largoMaximo = models.DecimalField('7.b Largo Maximo',max_digits=12, decimal_places=6)
    anchoMaximo = models.DecimalField('7.c Ancho Maximo',max_digits=12, decimal_places=6)
    otrosValoresDeLaPiedra = models.CharField('15. Otros valores de la piedra',max_length=150)
    observaciones = models.CharField('16. Observaciones',max_length=150)
    
    autorFicha = models.CharField('17a. Ficha llenada por', max_length=40)
    fechaEscrituraFicha = models.DateField('17.b Ficha llenada Fecha')

    supervisorFicha = models.CharField('17a. Ficha supervisada por', max_length=40)
    fechaSupervisionFicha = models.DateField('17.b Ficha supervisada Fecha')

    revisoFicha = models.CharField('17a. Ficha rellena por', max_length=40)

    OPCIONES_CONEXION_FIGURAS = (
        (1, 'Presencia de una sola figura'),
        (2, 'Menos del 10% interconectadas'),
        (3, '50% interconectadas'),
        (4, 'Mas del 80% interconectadas'),
    )

    conexionFiguras = models.IntegerField('11 Conexion Figuras', choices = OPCIONES_CONEXION_FIGURAS)

    limpiezaCon = models.CharField('12.1 Limpieza con', max_length = 40)
    rellenoSurcos = models.CharField('12.2 Relleno de surcos con', max_length = 40)
    tratamientoDigital = models.CharField('12.3 Tratamiento digital', max_length = 40)
    programaVersion = models.CharField('12.4 Programa/versión', max_length = 40)
    otrosTratamientosFotografia = models.CharField('12.5 Otros tratamientos fotografía:', max_length = 150)

    materialesApoyo = models.ManyToManyField(MaterialApoyo)
    mecanismosObtencionInformacion = models.ManyToManyField(MecanismoObtencionInformacion)

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

        (0, 'Fotico'),
        (1, 'Escotico'),

    )

    orientacionDeLaCara = models.IntegerField('6. Orientación de la cara', choices = OPCIONES_ORIENTACION_CARA_TRABAJADA)

    alto = models.DecimalField('7.1 Alto',max_digits=12, decimal_places=6)
    ancho = models.DecimalField('7.2 Ancho',max_digits=12, decimal_places=6)
    largo = models.DecimalField('7.3 Largo',max_digits=12, decimal_places=6)
    distanciaBocaPrincipal = models.DecimalField('8.3 Distancia Boca Principal',max_digits=12, decimal_places=6)    
    altura = models.DecimalField('8.3.2 Altura',max_digits=12, decimal_places=6)   
    luminosidad = models.IntegerField('8.3.1 Luminosidad', choices = OPCIONES_LUMINOSIDAD) 
    requiereAndamiaje = models.BooleanField()

    manifestaciones = models.ManyToManyField(ManifestacionesEnCarasTrabajadas)
    ubicacionCaracasTrabajadas = models.ManyToManyField(PosibleUbicacionCarasTrajabadas)
    piedra = models.ForeignKey(Piedra)

class ConjuntoFiguraPorTipo(models.Model):

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

    cantidad =  models.IntegerField('9.b Cantidad')
    seccion =   models.IntegerField('Seccion de la cara.')
    tipoFigura = models.IntegerField('9.a Tipo de figura',choices = OPCIONES_UBICACION_CARA_TRABAJADA)
    descripcion = models.CharField('9.c Descripcion',max_length=150) 
    posicion = models.CharField('9.c Posicion de las figuras',max_length=150) 
    cara = models.ForeignKey(CaraTrabajada)

class RecursoMultimedia (MaterialApoyo):

    tecnica = models.CharField('13.4.1 Técnica',max_length=150) 
    imagen = models.CharField(max_length=150) # models.ImageField()

class PaginaWEB (MaterialApoyo):

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

class MaterialAudiovisual (MaterialApoyo):

    formato = models.CharField('13.5.1 Formato', max_length=40)
    imagen = models.CharField('13.5.2 Imagen', max_length=40)

class Bibliografia (MaterialApoyo):

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


class ReproduccionGrafica (MaterialApoyo):

    numPiezas = models.IntegerField('13.2.1 Número de piezas')
    instituto  = models.CharField('13.2.2 Instituto ', max_length=40)
    persona  = models.CharField('13.2.3 Persona ', max_length=40)

class ImagenReproduccionGrafica(models.Model):

    reproduccionGrafica = models.ForeignKey(ReproduccionGrafica)

class ReproduccionGraficaEscalaNatural(ReproduccionGrafica):

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

class ReproduccionGraficaEscalaReducida(ReproduccionGrafica):

    TIPO_REPRODUCCION_GRAFICA_ESCALA_REDUCIDA = (
        (1, 'Dibujo'),
        (2, 'Matriz'),
    )

    tipoReproduccion = models.IntegerField('Tipo de reproduccion grafica de escala reducida', choices = TIPO_REPRODUCCION_GRAFICA_ESCALA_REDUCIDA)   

