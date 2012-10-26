#coding: latin-1

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

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
    datum = models.IntegerField(choices = OPCIONES_DATUM)

    def _unicode_(self):
        return self.nombre

#    def transformacion_a_horas_minutos_segundos(self):
#        return 

class Piedra(models.Model):

    codigo = models.CharField('0. Codigo de la piedra', max_length=20)#, primary_key=True)        
    nombre = models.CharField('1. Nombre de la piedra', max_length=150)
    manifiestacionAsociada = models.CharField('1.1 Manifestaciones Asociadas', max_length=150)
    nombreFiguras = models.CharField('2. Nombre Figuras',max_length=150)
    locGeograficaEstado= models.CharField('3. Nombre Figuras',max_length=40)
    locGeograficaMunicipio= models.CharField('2. Nombre Figuras',max_length=40)
    numeroCaras = models.IntegerField('Numero de Caras')
    numerocarasTrajabadas = models.IntegerField('Numero de caras trabajadas')
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

    
class TratamientoFotografia(models.Model):

    limpiezaCon = models.CharField('12.1 Limpieza con', max_length = 40)
    rellenoSurcos = models.CharField('12.2 Relleno de surcos con', max_length = 40)
    tratamientoDigital = models.CharField('12.3 Tratamiento digital', max_length = 40)
    programaVersion = models.CharField('12.4 Programa/versión', max_length = 40)
    otros = models.CharField('12.5 Otros:', max_length = 150)

class PosibleUbicacionCarasTrajabadas(models.Model): # Enumeration (N)

    OPCIONES_UBICACION_CARA_TRABAJADA = (
        (1, 'En toda la caverna'),
        (2, 'En áreas específicas'),
        (3, 'Sala Principal'),
        (4, 'Otra sala'),
        (5, 'Lago interior'),
        (6, 'Claraboya'),
        (7, 'Luminosidad'),
        (8, 'Fotico'),
        (9, 'Escótico'),
    )

    ubic = models.IntegerField(choices = OPCIONES_UBICACION_CARA_TRABAJADA)

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

    orientacionDeLaCara = models.IntegerField('6. Orientación de la cara', choices = OPCIONES_ORIENTACION_CARA_TRABAJADA)

    alto = models.DecimalField('7.1 Alto',max_digits=12, decimal_places=6)
    ancho = models.DecimalField('7.2 Ancho',max_digits=12, decimal_places=6)
    diametro = models.DecimalField('7.3 Diametro',max_digits=12, decimal_places=6)
    distanciaBocaPrincipal = models.DecimalField('8.3 Distancia Boca Principal',max_digits=12, decimal_places=6)    
    altura = models.DecimalField('8.3.2 Altura',max_digits=12, decimal_places=6)   
    altura = models.DecimalField('8.3.1.1 Altura',max_digits=12, decimal_places=6)   
    requiereAndamiaje = models.BooleanField()

    ubicacionCaracasTrabajadas = models.ManyToManyField(PosibleUbicacionCarasTrajabadas)


class EsquemaDeCara(models.Model):

    numCara =  models.IntegerField('6. Orientación de la cara')

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
    tipoFigura = models.IntegerField('9.a Tipo de figura',choices = OPCIONES_UBICACION_CARA_TRABAJADA)
    descripcion = models.CharField('9.c Descripcion',max_length=150) 
    esquemaCara = models.ForeignKey(EsquemaDeCara)

class MaterialApoyo (models.Model):

    piedra =  models.ForeignKey(Piedra)

class RecursoMultimedia (MaterialApoyo):
    descripcion = models.CharField('13.4.1 Técnica',max_length=150) 
    imagen = models.CharField(max_length=150) # models.ImageField()

class PaginaWEB (MaterialApoyo):
    direccionURL = models.URLField ('13.8 Página Web')

class Grabacion (MaterialApoyo):

    formato = models.CharField('13.6.0 Formato',max_length=40)
    titulo = models.CharField('13.6.1 Titulo',max_length=60)
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

class MecanismoObtencionInformacion (models.Model):
    piedra = models.ForeignKey(Piedra)

class ProspeccionSistematica (MecanismoObtencionInformacion):

    def _unicode_(self):
        return self.piedra

class ComunicacionPersonal (MecanismoObtencionInformacion):

    nombre = models.CharField('14.2.1 Nombre', max_length=40)
    direccion = models.CharField('14.2.2 Direccoin', max_length=150)
    telefono = models.CharField('14.2.3 Telefono/Fax', max_length=16)
    telefono = models.CharField('14.2.3 Telefono celular', max_length=16)
    direccionEmail = models.EmailField('14.2.5 Correo electrónico')
    paginaWeb = models.URLField('14.2.6 Pagina WEB')
    twitter = models.CharField('14.2.7 Twitter', max_length=40)
    nombreFacebook = models.CharField('14.2.8 Nombre de Perfil Facebook', max_length=40)
    paginaWeb = models.URLField('14.2.9 Blog')
    fecha = models.DateField('14.2.10 Fecha')

class VerificadoEncampo (MecanismoObtencionInformacion):
    
    def _unicode_(self):
        return self.piedra

class Fotografia (MaterialApoyo):

    TIPO_REPRODUCCION_GRAFICA_ESCALA_NATURAL = (
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

