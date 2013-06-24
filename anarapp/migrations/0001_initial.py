# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Yacimiento'
        db.create_table('anarapp_yacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Yacimiento'])

        # Adding model 'LocalidadYacimiento'
        db.create_table('anarapp_localidadyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esCentroPoblado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esUrbano', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esRural', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esIndigena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombrePoblado', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('esCentroNoPoblado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombreNoPoblado', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['LocalidadYacimiento'])

        # Adding model 'UsoActSuelo'
        db.create_table('anarapp_usoactsuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esForestal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGanadero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAgriRiesgo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAgriTemp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSueloUrbano', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSueloTuristico', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['UsoActSuelo'])

        # Adding model 'TenenciaDeTierra'
        db.create_table('anarapp_tenenciadetierra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esPrivada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esComunal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esEjido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMunicipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esABRAE', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTenenciaOtros', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TenenciaDeTierra'])

        # Adding model 'Indicaciones'
        db.create_table('anarapp_indicaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('direcciones', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('puntoDatum', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['Indicaciones'])

        # Adding model 'Croquis'
        db.create_table('anarapp_croquis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('urlImagen', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['Croquis'])

        # Adding model 'Plano'
        db.create_table('anarapp_plano', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numeroPlano', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['Plano'])

        # Adding model 'Coordenadas'
        db.create_table('anarapp_coordenadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitud', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('latitud', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['Coordenadas'])

        # Adding model 'Datum'
        db.create_table('anarapp_datum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoDatum', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['Datum'])

        # Adding model 'Altitud'
        db.create_table('anarapp_altitud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('altura', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('superficie', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['Altitud'])

        # Adding model 'FotografiaYac'
        db.create_table('anarapp_fotografiayac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esAerea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('noEsAerea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSatelital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('urlImagen', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['FotografiaYac'])

        # Adding model 'TipoYacimiento'
        db.create_table('anarapp_tipoyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esParedRocosa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esRoca', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrigo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCueva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCuevadeRec', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTerrenoSup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTerrenoPro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TipoYacimiento'])

        # Adding model 'TipoManifestacion'
        db.create_table('anarapp_tipomanifestacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esGeoglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPetroglifoPintado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMicroPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPiedraMitNat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroMitNat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroMitConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroMitConPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroMitConDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonumentoMegalitico', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonolito', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonoConGrab', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhir', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhirConPuntos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhirConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhirConPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAmolador', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBatea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPuntoAcoplado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCupula', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMortero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TipoManifestacion'])

        # Adding model 'UbicacionYacimiento'
        db.create_table('anarapp_ubicacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enCerro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCima', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enLadera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enFalda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enFila', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPieMonte', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enBarranco', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enAcantilado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enValle', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enLecho', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enMargenDer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enMargenIzq', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enIsla', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRaudal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCosta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['UbicacionYacimiento'])

        # Adding model 'OrientacionYacimiento'
        db.create_table('anarapp_orientacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('haciaCerro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaValle', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaRio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaCosta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaCielo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('orientacion', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['OrientacionYacimiento'])

        # Adding model 'TexturaSuelo'
        db.create_table('anarapp_texturasuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esRocaMadre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPedregoso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esArenoso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esArcilloso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mixto', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TexturaSuelo'])

        # Adding model 'FloraYacimiento'
        db.create_table('anarapp_florayacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flora', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['FloraYacimiento'])

        # Adding model 'FaunaYacimiento'
        db.create_table('anarapp_faunayacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fauna', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['FaunaYacimiento'])

        # Adding model 'HidrologiaYacimiento'
        db.create_table('anarapp_hidrologiayacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('laguna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arroyo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arroyoPerenne', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('manantial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('manantialIntermitente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('distancia', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['HidrologiaYacimiento'])

        # Adding model 'TipoExposicionYac'
        db.create_table('anarapp_tipoexposicionyac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('expuesto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expuestoPeriodicamente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TipoExposicionYac'])

        # Adding model 'ConstitucionYacimiento'
        db.create_table('anarapp_constitucionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nroPiedras', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nroPiedrasGrabadas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nroPiedrasPintadas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nroPiedrasColocadas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['ConstitucionYacimiento'])

        # Adding model 'MaterialYacimiento'
        db.create_table('anarapp_materialyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esRoca', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esIgnea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMetamor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSedimentaria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('esTierra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esHueso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCorteza', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPiel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['MaterialYacimiento'])

        # Adding model 'TecnicaParaGeoglifo'
        db.create_table('anarapp_tecnicaparageoglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tecnicas', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaGeoglifo'])

        # Adding model 'TecnicaParaPintura'
        db.create_table('anarapp_tecnicaparapintura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conDedo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fibra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('soplado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaPintura'])

        # Adding model 'TecnicaParaPetroglifo'
        db.create_table('anarapp_tecnicaparapetroglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esGrabado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionDirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionIndirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionPiedra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionArena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaPetroglifo'])

        # Adding model 'TecnicaParaMicroPetro'
        db.create_table('anarapp_tecnicaparamicropetro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esGrabado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionDirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionIndirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionPiedra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionArena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaMicroPetro'])

        # Adding model 'TecnicaParaMonumentos'
        db.create_table('anarapp_tecnicaparamonumentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esMonolito', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhir', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tecnicas', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaMonumentos'])

        # Adding model 'CaracSurcoPetroglifo'
        db.create_table('anarapp_caracsurcopetroglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anchoDe', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('anchoA', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('produndidadDe', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('profundidadA', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('esBase', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBaseRedonda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBaseAguda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBajoRelieve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBajoRelieveLineal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBajoRelievePlanar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAltoRelieve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAltoRelieveLineal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAltoRelievePlanar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAreaInterlineal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAreaInterlinealPulida', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAreaInterlinealRebajada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoSuperpuesto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoRebajado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoPetroglifo'])

        # Adding model 'CaracSurcoAmoladores'
        db.create_table('anarapp_caracsurcoamoladores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('largo', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('ancho', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('diametro', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoAmoladores'])

        # Adding model 'CaracSurcoBateas'
        db.create_table('anarapp_caracsurcobateas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('largo', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('ancho', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoBateas'])

        # Adding model 'CaracSurcoPuntosAcopl'
        db.create_table('anarapp_caracsurcopuntosacopl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esPunteado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoPuntosAcopl'])

        # Adding model 'CaracSurcoCupulas'
        db.create_table('anarapp_caracsurcocupulas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('largo', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('ancho', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('diametro', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoCupulas'])

        # Adding model 'CaracSurcoMortero'
        db.create_table('anarapp_caracsurcomortero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('largo', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('ancho', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoMortero'])

        # Adding model 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esPinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTecnicaDactilar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTecnicaFibra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('esLineaSencilla', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anchoDe', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('anchoA', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('esLineaCompuesta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anchoDeComp', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('anchoAComp', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('esImpresionDeManos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esImpresionDeManosPositivo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esImpresionDeManosNegativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienesFigurasSuperpuestas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['CaracDeLaPintura'])

        # Adding model 'CaracMonolitos'
        db.create_table('anarapp_caracmonolitos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('esPinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConGrabados', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['CaracMonolitos'])

        # Adding model 'CaracMenhires'
        db.create_table('anarapp_caracmenhires', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sonPiedrasVerticales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadPiedrasVerticales', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('conPuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPuntosAcoplados', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPetroglifo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('conPinturas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPinturas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('distanciamiento', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['CaracMenhires'])

        # Adding model 'CaracDolmenArt'
        db.create_table('anarapp_caracdolmenart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPetroglifo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('conPinturas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPinturas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('notas', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['CaracDolmenArt'])

        # Adding model 'EstadoConserYac'
        db.create_table('anarapp_estadoconseryac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enBuenEstado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estadoModificado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('trasladado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trasladadoPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('sumergido', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sumergidoPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('enterrado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enterradoPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('perdido', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perdidoPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('destruido', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('destruidoPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('crecimientoVeg', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('crecimientoVegPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('patina', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('patinaPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('erosion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('erosionPa', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('estaDestruido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPorCausaNatural', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaNaturalLigera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaNaturalAguda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaHumana', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaHumanaLigera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaHumanaAguda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('especificar', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('destruccionPotencial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porAsentamientoHumand', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porObraCortoPlazo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porObraMedianoPlazo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porObraLargoPlazo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porNivelacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porExtraccionFamiliar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porExtraccionMayor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porVandalismo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionParModerada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionParSevera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionExtModerada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionExtSevera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('esDeTiempo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esInmediato', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dosAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tresAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cuatroAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cincoAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mas', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['EstadoConserYac'])

        # Adding model 'ConsiderTemp'
        db.create_table('anarapp_considertemp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cincoAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['ConsiderTemp'])

        # Adding model 'CronologiaTentativa'
        db.create_table('anarapp_cronologiatentativa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esCrono1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono3', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono4', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono5', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono6', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono7', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('bibliografia', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['CronologiaTentativa'])

        # Adding model 'ManifestacionesAsociadas'
        db.create_table('anarapp_manifestacionesasociadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esLitica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionLitica', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esCeramica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCeramica', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esOseo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionOseo', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esConcha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionConcha', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esCarbon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCarbon', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esMito', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionMito', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esCementerio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCementerio', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('esMonticulo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionMonticulo', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesAsociadas'])

        # Adding model 'ObtenidaPor'
        db.create_table('anarapp_obtenidapor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porProspeccion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porComunicacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('sitioweb', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('blog', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('verificadoEnCampo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['ObtenidaPor'])

        # Adding model 'OtrosValoresSitio'
        db.create_table('anarapp_otrosvaloressitio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valores', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['OtrosValoresSitio'])

        # Adding model 'Observacion'
        db.create_table('anarapp_observacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['Observacion'])

        # Adding model 'LlenadaPor'
        db.create_table('anarapp_llenadapor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['LlenadaPor'])

        # Adding model 'SupervisadaPor'
        db.create_table('anarapp_supervisadapor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
        ))
        db.send_create_signal('anarapp', ['SupervisadaPor'])

        # Adding model 'MaterialApoyo'
        db.create_table('anarapp_materialapoyo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MaterialApoyo'])

        # Adding model 'MecObtInformacion'
        db.create_table('anarapp_mecobtinformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MecObtInformacion'])

        # Adding model 'Piedra'
        db.create_table('anarapp_piedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('manifiestacionAsociada', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombreFiguras', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numeroCaras', self.gf('django.db.models.fields.IntegerField')()),
            ('numeroCarasTrajabadas', self.gf('django.db.models.fields.IntegerField')()),
            ('otrosValoresDeLaPiedra', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('autorFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fechaEscrituraFicha', self.gf('django.db.models.fields.DateField')()),
            ('supervisorFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fechaSupervisionFicha', self.gf('django.db.models.fields.DateField')()),
            ('revisoFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['Piedra'])

        # Adding model 'DimensionPiedra'
        db.create_table('anarapp_dimensionpiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('altoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('largoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('anchoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['DimensionPiedra'])

        # Adding model 'TratFotografia'
        db.create_table('anarapp_tratfotografia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('limpiezaCon', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('rellenoSurcos', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tratamientoDigital', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('programaVersion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('otrosTratamientosFotografia', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['TratFotografia'])

        # Adding model 'CaraTrabajada'
        db.create_table('anarapp_caratrabajada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orientacionDeLaCara', self.gf('django.db.models.fields.IntegerField')()),
            ('conexionFiguras', self.gf('django.db.models.fields.IntegerField')()),
            ('alto', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('distanciaBocaPrincipal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('altura', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('luminosidad', self.gf('django.db.models.fields.IntegerField')()),
            ('requiereAndamiaje', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneAmoladores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneCupulas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnTodaLaCaverna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnSalaPrincipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnOtraSala', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnLagoInterior', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnClaraboya', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['CaraTrabajada'])

        # Adding model 'ConjFiguraPorTipo'
        db.create_table('anarapp_conjfiguraportipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seccion', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoFigura', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cara', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.CaraTrabajada'])),
        ))
        db.send_create_signal('anarapp', ['ConjFiguraPorTipo'])

        # Adding model 'RecursoMultimedia'
        db.create_table('anarapp_recursomultimedia', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['RecursoMultimedia'])

        # Adding model 'PaginaWEB'
        db.create_table('anarapp_paginaweb', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('direccionURL', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('anarapp', ['PaginaWEB'])

        # Adding model 'Grabacion'
        db.create_table('anarapp_grabacion', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('formato', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('isFromAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopia', self.gf('django.db.models.fields.IntegerField')()),
            ('videos', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['Grabacion'])

        # Adding model 'Video'
        db.create_table('anarapp_video', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Video'])

        # Adding model 'Pelicula'
        db.create_table('anarapp_pelicula', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Pelicula'])

        # Adding model 'VideoPiedra'
        db.create_table('anarapp_videopiedra', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['VideoPiedra'])

        # Adding model 'PeliculaPiedra'
        db.create_table('anarapp_peliculapiedra', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['PeliculaPiedra'])

        # Adding model 'MatAudiovisual'
        db.create_table('anarapp_mataudiovisual', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('formato', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['MatAudiovisual'])

        # Adding model 'Bibliografia'
        db.create_table('anarapp_bibliografia', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('conDibujo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['Bibliografia'])

        # Adding model 'BibPiedra'
        db.create_table('anarapp_bibpiedra', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('conDibujo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['BibPiedra'])

        # Adding model 'MapaBibliografia'
        db.create_table('anarapp_mapabibliografia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tipoMapa', self.gf('django.db.models.fields.IntegerField')()),
            ('bibliografia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Bibliografia'])),
        ))
        db.send_create_signal('anarapp', ['MapaBibliografia'])

        # Adding model 'FotografiaBibliografia'
        db.create_table('anarapp_fotografiabibliografia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('bibliografia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Bibliografia'])),
        ))
        db.send_create_signal('anarapp', ['FotografiaBibliografia'])

        # Adding model 'ReproGraf'
        db.create_table('anarapp_reprograf', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('numPiezas', self.gf('django.db.models.fields.IntegerField')()),
            ('instituto', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('persona', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['ReproGraf'])

        # Adding model 'ImagenReproGraf'
        db.create_table('anarapp_imagenreprograf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reproduccionGrafica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.ReproGraf'])),
        ))
        db.send_create_signal('anarapp', ['ImagenReproGraf'])

        # Adding model 'ReproGrafEscalaNaturalPiedra'
        db.create_table('anarapp_reprografescalanaturalpiedra', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaNaturalPiedra'])

        # Adding model 'ReproGrafEscalaRedPied'
        db.create_table('anarapp_reprografescalaredpied', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaRedPied'])

        # Adding model 'ReproGrafEscalaNatural'
        db.create_table('anarapp_reprografescalanatural', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaNatural'])

        # Adding model 'ReproGrafEscalaRed'
        db.create_table('anarapp_reprografescalared', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaRed'])

        # Adding model 'FotografiaPiedra'
        db.create_table('anarapp_fotografiapiedra', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('fotografo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('numRollo', self.gf('django.db.models.fields.IntegerField')()),
            ('numMarcaNegativo', self.gf('django.db.models.fields.IntegerField')()),
            ('esDeAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiaAnar', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoFotografia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['FotografiaPiedra'])

        # Adding model 'ProspSistPiedra'
        db.create_table('anarapp_prospsistpiedra', (
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['ProspSistPiedra'])

        # Adding model 'ComunicacionPersonalPiedras'
        db.create_table('anarapp_comunicacionpersonalpiedras', (
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('telefonoCel', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('direccionEmail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('paginaWeb', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('nombreFacebook', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['ComunicacionPersonalPiedras'])

        # Adding model 'VerificadoEnPiedra'
        db.create_table('anarapp_verificadoenpiedra', (
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['VerificadoEnPiedra'])


    def backwards(self, orm):
        # Deleting model 'Yacimiento'
        db.delete_table('anarapp_yacimiento')

        # Deleting model 'LocalidadYacimiento'
        db.delete_table('anarapp_localidadyacimiento')

        # Deleting model 'UsoActSuelo'
        db.delete_table('anarapp_usoactsuelo')

        # Deleting model 'TenenciaDeTierra'
        db.delete_table('anarapp_tenenciadetierra')

        # Deleting model 'Indicaciones'
        db.delete_table('anarapp_indicaciones')

        # Deleting model 'Croquis'
        db.delete_table('anarapp_croquis')

        # Deleting model 'Plano'
        db.delete_table('anarapp_plano')

        # Deleting model 'Coordenadas'
        db.delete_table('anarapp_coordenadas')

        # Deleting model 'Datum'
        db.delete_table('anarapp_datum')

        # Deleting model 'Altitud'
        db.delete_table('anarapp_altitud')

        # Deleting model 'FotografiaYac'
        db.delete_table('anarapp_fotografiayac')

        # Deleting model 'TipoYacimiento'
        db.delete_table('anarapp_tipoyacimiento')

        # Deleting model 'TipoManifestacion'
        db.delete_table('anarapp_tipomanifestacion')

        # Deleting model 'UbicacionYacimiento'
        db.delete_table('anarapp_ubicacionyacimiento')

        # Deleting model 'OrientacionYacimiento'
        db.delete_table('anarapp_orientacionyacimiento')

        # Deleting model 'TexturaSuelo'
        db.delete_table('anarapp_texturasuelo')

        # Deleting model 'FloraYacimiento'
        db.delete_table('anarapp_florayacimiento')

        # Deleting model 'FaunaYacimiento'
        db.delete_table('anarapp_faunayacimiento')

        # Deleting model 'HidrologiaYacimiento'
        db.delete_table('anarapp_hidrologiayacimiento')

        # Deleting model 'TipoExposicionYac'
        db.delete_table('anarapp_tipoexposicionyac')

        # Deleting model 'ConstitucionYacimiento'
        db.delete_table('anarapp_constitucionyacimiento')

        # Deleting model 'MaterialYacimiento'
        db.delete_table('anarapp_materialyacimiento')

        # Deleting model 'TecnicaParaGeoglifo'
        db.delete_table('anarapp_tecnicaparageoglifo')

        # Deleting model 'TecnicaParaPintura'
        db.delete_table('anarapp_tecnicaparapintura')

        # Deleting model 'TecnicaParaPetroglifo'
        db.delete_table('anarapp_tecnicaparapetroglifo')

        # Deleting model 'TecnicaParaMicroPetro'
        db.delete_table('anarapp_tecnicaparamicropetro')

        # Deleting model 'TecnicaParaMonumentos'
        db.delete_table('anarapp_tecnicaparamonumentos')

        # Deleting model 'CaracSurcoPetroglifo'
        db.delete_table('anarapp_caracsurcopetroglifo')

        # Deleting model 'CaracSurcoAmoladores'
        db.delete_table('anarapp_caracsurcoamoladores')

        # Deleting model 'CaracSurcoBateas'
        db.delete_table('anarapp_caracsurcobateas')

        # Deleting model 'CaracSurcoPuntosAcopl'
        db.delete_table('anarapp_caracsurcopuntosacopl')

        # Deleting model 'CaracSurcoCupulas'
        db.delete_table('anarapp_caracsurcocupulas')

        # Deleting model 'CaracSurcoMortero'
        db.delete_table('anarapp_caracsurcomortero')

        # Deleting model 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura')

        # Deleting model 'CaracMonolitos'
        db.delete_table('anarapp_caracmonolitos')

        # Deleting model 'CaracMenhires'
        db.delete_table('anarapp_caracmenhires')

        # Deleting model 'CaracDolmenArt'
        db.delete_table('anarapp_caracdolmenart')

        # Deleting model 'EstadoConserYac'
        db.delete_table('anarapp_estadoconseryac')

        # Deleting model 'ConsiderTemp'
        db.delete_table('anarapp_considertemp')

        # Deleting model 'CronologiaTentativa'
        db.delete_table('anarapp_cronologiatentativa')

        # Deleting model 'ManifestacionesAsociadas'
        db.delete_table('anarapp_manifestacionesasociadas')

        # Deleting model 'ObtenidaPor'
        db.delete_table('anarapp_obtenidapor')

        # Deleting model 'OtrosValoresSitio'
        db.delete_table('anarapp_otrosvaloressitio')

        # Deleting model 'Observacion'
        db.delete_table('anarapp_observacion')

        # Deleting model 'LlenadaPor'
        db.delete_table('anarapp_llenadapor')

        # Deleting model 'SupervisadaPor'
        db.delete_table('anarapp_supervisadapor')

        # Deleting model 'MaterialApoyo'
        db.delete_table('anarapp_materialapoyo')

        # Deleting model 'MecObtInformacion'
        db.delete_table('anarapp_mecobtinformacion')

        # Deleting model 'Piedra'
        db.delete_table('anarapp_piedra')

        # Deleting model 'DimensionPiedra'
        db.delete_table('anarapp_dimensionpiedra')

        # Deleting model 'TratFotografia'
        db.delete_table('anarapp_tratfotografia')

        # Deleting model 'CaraTrabajada'
        db.delete_table('anarapp_caratrabajada')

        # Deleting model 'ConjFiguraPorTipo'
        db.delete_table('anarapp_conjfiguraportipo')

        # Deleting model 'RecursoMultimedia'
        db.delete_table('anarapp_recursomultimedia')

        # Deleting model 'PaginaWEB'
        db.delete_table('anarapp_paginaweb')

        # Deleting model 'Grabacion'
        db.delete_table('anarapp_grabacion')

        # Deleting model 'Video'
        db.delete_table('anarapp_video')

        # Deleting model 'Pelicula'
        db.delete_table('anarapp_pelicula')

        # Deleting model 'VideoPiedra'
        db.delete_table('anarapp_videopiedra')

        # Deleting model 'PeliculaPiedra'
        db.delete_table('anarapp_peliculapiedra')

        # Deleting model 'MatAudiovisual'
        db.delete_table('anarapp_mataudiovisual')

        # Deleting model 'Bibliografia'
        db.delete_table('anarapp_bibliografia')

        # Deleting model 'BibPiedra'
        db.delete_table('anarapp_bibpiedra')

        # Deleting model 'MapaBibliografia'
        db.delete_table('anarapp_mapabibliografia')

        # Deleting model 'FotografiaBibliografia'
        db.delete_table('anarapp_fotografiabibliografia')

        # Deleting model 'ReproGraf'
        db.delete_table('anarapp_reprograf')

        # Deleting model 'ImagenReproGraf'
        db.delete_table('anarapp_imagenreprograf')

        # Deleting model 'ReproGrafEscalaNaturalPiedra'
        db.delete_table('anarapp_reprografescalanaturalpiedra')

        # Deleting model 'ReproGrafEscalaRedPied'
        db.delete_table('anarapp_reprografescalaredpied')

        # Deleting model 'ReproGrafEscalaNatural'
        db.delete_table('anarapp_reprografescalanatural')

        # Deleting model 'ReproGrafEscalaRed'
        db.delete_table('anarapp_reprografescalared')

        # Deleting model 'FotografiaPiedra'
        db.delete_table('anarapp_fotografiapiedra')

        # Deleting model 'ProspSistPiedra'
        db.delete_table('anarapp_prospsistpiedra')

        # Deleting model 'ComunicacionPersonalPiedras'
        db.delete_table('anarapp_comunicacionpersonalpiedras')

        # Deleting model 'VerificadoEnPiedra'
        db.delete_table('anarapp_verificadoenpiedra')


    models = {
        'anarapp.altitud': {
            'Meta': {'object_name': 'Altitud'},
            'altura': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superficie': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.bibliografia': {
            'Meta': {'object_name': 'Bibliografia', '_ormbases': ['anarapp.MaterialApoyo']},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'conDibujo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.bibpiedra': {
            'Meta': {'object_name': 'BibPiedra', '_ormbases': ['anarapp.MaterialApoyo']},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'conDibujo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.caracdelapintura': {
            'Meta': {'object_name': 'CaracDeLaPintura'},
            'anchoA': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoAComp': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoDe': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoDeComp': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esImpresionDeManos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosPositivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaCompuesta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaSencilla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaDactilar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaFibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tienesFigurasSuperpuestas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracdolmenart': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracDolmenArt'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracmenhires': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracMenhires'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPuntosAcoplados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadPiedrasVerticales': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conPuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distanciamiento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sonPiedrasVerticales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracmonolitos': {
            'Meta': {'object_name': 'CaracMonolitos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConGrabados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracsurcoamoladores': {
            'Meta': {'object_name': 'CaracSurcoAmoladores'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcobateas': {
            'Meta': {'object_name': 'CaracSurcoBateas'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcocupulas': {
            'Meta': {'object_name': 'CaracSurcoCupulas'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcomortero': {
            'Meta': {'object_name': 'CaracSurcoMortero'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopetroglifo': {
            'Meta': {'object_name': 'CaracSurcoPetroglifo'},
            'anchoA': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoDe': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esAltoRelieve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAltoRelieveLineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAltoRelievePlanar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlinealPulida': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlinealRebajada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelieve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelieveLineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelievePlanar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBase': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBaseAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBaseRedonda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoRebajado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoSuperpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produndidadDe': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'profundidadA': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopuntosacopl': {
            'Meta': {'object_name': 'CaracSurcoPuntosAcopl'},
            'esPunteado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caratrabajada': {
            'Meta': {'object_name': 'CaraTrabajada'},
            'alto': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'altura': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'conexionFiguras': ('django.db.models.fields.IntegerField', [], {}),
            'distanciaBocaPrincipal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'luminosidad': ('django.db.models.fields.IntegerField', [], {}),
            'orientacionDeLaCara': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'requiereAndamiaje': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneAmoladores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ubicadaEnClaraboya': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ubicadaEnLagoInterior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ubicadaEnOtraSala': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ubicadaEnSalaPrincipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ubicadaEnTodaLaCaverna': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.comunicacionpersonalpiedras': {
            'Meta': {'object_name': 'ComunicacionPersonalPiedras', '_ormbases': ['anarapp.MecObtInformacion']},
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'direccionEmail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nombreFacebook': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'paginaWeb': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'telefonoCel': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.conjfiguraportipo': {
            'Meta': {'object_name': 'ConjFiguraPorTipo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'cara': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.CaraTrabajada']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seccion': ('django.db.models.fields.IntegerField', [], {}),
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.considertemp': {
            'Meta': {'object_name': 'ConsiderTemp'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.constitucionyacimiento': {
            'Meta': {'object_name': 'ConstitucionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nroPiedras': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasColocadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasGrabadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasPintadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.coordenadas': {
            'Meta': {'object_name': 'Coordenadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.cronologiatentativa': {
            'Meta': {'object_name': 'CronologiaTentativa'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'bibliografia': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esCrono1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono5': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono7': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.croquis': {
            'Meta': {'object_name': 'Croquis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urlImagen': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.datum': {
            'Meta': {'object_name': 'Datum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.dimensionpiedra': {
            'Meta': {'object_name': 'DimensionPiedra'},
            'altoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.estadoconseryac': {
            'Meta': {'object_name': 'EstadoConserYac'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'crecimientoVeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crecimientoVegPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'cuatroAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruccionPotencial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destruidoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'dosAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enBuenEstado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enterrado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enterradoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'erosion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'erosionPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esDeTiempo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esInmediato': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPorCausaNatural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'especificar': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'estaDestruido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estadoModificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'patina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patinaPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'perdido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perdidoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'porAsentamientoHumand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionExtModerada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionExtSevera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionParModerada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionParSevera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porExtraccionFamiliar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porExtraccionMayor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porNivelacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraCortoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraLargoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraMedianoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porVandalismo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sumergido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sumergidoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'trasladado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trasladadoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tresAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.faunayacimiento': {
            'Meta': {'object_name': 'FaunaYacimiento'},
            'fauna': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.florayacimiento': {
            'Meta': {'object_name': 'FloraYacimiento'},
            'flora': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotografiabibliografia': {
            'Meta': {'object_name': 'FotografiaBibliografia'},
            'bibliografia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Bibliografia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotografiapiedra': {
            'Meta': {'object_name': 'FotografiaPiedra', '_ormbases': ['anarapp.MaterialApoyo']},
            'esDeAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fotografo': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'numCopiaAnar': ('django.db.models.fields.IntegerField', [], {}),
            'numMarcaNegativo': ('django.db.models.fields.IntegerField', [], {}),
            'numReferencia': ('django.db.models.fields.IntegerField', [], {}),
            'numRollo': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'tipoFotografia': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotografiayac': {
            'Meta': {'object_name': 'FotografiaYac'},
            'esAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSatelital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noEsAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urlImagen': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.grabacion': {
            'Meta': {'object_name': 'Grabacion', '_ormbases': ['anarapp.MaterialApoyo']},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'formato': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'isFromAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'numCopia': ('django.db.models.fields.IntegerField', [], {}),
            'numReferencia': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'videos': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.hidrologiayacimiento': {
            'Meta': {'object_name': 'HidrologiaYacimiento'},
            'arroyo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'arroyoPerenne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distancia': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laguna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantialIntermitente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'rio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.imagenreprograf': {
            'Meta': {'object_name': 'ImagenReproGraf'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reproduccionGrafica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.ReproGraf']"})
        },
        'anarapp.indicaciones': {
            'Meta': {'object_name': 'Indicaciones'},
            'direcciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntoDatum': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.llenadapor': {
            'Meta': {'object_name': 'LlenadaPor'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.localidadyacimiento': {
            'Meta': {'object_name': 'LocalidadYacimiento'},
            'esCentroNoPoblado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCentroPoblado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esIndigena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esUrbano': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreNoPoblado': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'nombrePoblado': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesasociadas': {
            'Meta': {'object_name': 'ManifestacionesAsociadas'},
            'descripcionCarbon': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionCementerio': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionCeramica': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionConcha': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionLitica': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionMito': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionMonticulo': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionOseo': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'esCarbon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCementerio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCeramica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLitica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonticulo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esOseo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.mapabibliografia': {
            'Meta': {'object_name': 'MapaBibliografia'},
            'bibliografia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Bibliografia']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoMapa': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.mataudiovisual': {
            'Meta': {'object_name': 'MatAudiovisual', '_ormbases': ['anarapp.MaterialApoyo']},
            'formato': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.materialapoyo': {
            'Meta': {'object_name': 'MaterialApoyo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.materialyacimiento': {
            'Meta': {'object_name': 'MaterialYacimiento'},
            'esCorteza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esHueso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esIgnea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMetamor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPiel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRoca': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSedimentaria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTierra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.mecobtinformacion': {
            'Meta': {'object_name': 'MecObtInformacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.observacion': {
            'Meta': {'object_name': 'Observacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.obtenidapor': {
            'Meta': {'object_name': 'ObtenidaPor'},
            'blog': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'porComunicacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porProspeccion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sitioweb': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'verificadoEnCampo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.orientacionyacimiento': {
            'Meta': {'object_name': 'OrientacionYacimiento'},
            'haciaCerro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaCielo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaCosta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaRio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaValle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientacion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.otrosvaloressitio': {
            'Meta': {'object_name': 'OtrosValoresSitio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valores': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.paginaweb': {
            'Meta': {'object_name': 'PaginaWEB', '_ormbases': ['anarapp.MaterialApoyo']},
            'direccionURL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.pelicula': {
            'Meta': {'object_name': 'Pelicula', '_ormbases': ['anarapp.Grabacion']},
            'grabacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Grabacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.peliculapiedra': {
            'Meta': {'object_name': 'PeliculaPiedra', '_ormbases': ['anarapp.Grabacion']},
            'grabacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Grabacion']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.piedra': {
            'Meta': {'object_name': 'Piedra'},
            'autorFicha': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fechaEscrituraFicha': ('django.db.models.fields.DateField', [], {}),
            'fechaSupervisionFicha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifiestacionAsociada': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombreFiguras': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'numeroCaras': ('django.db.models.fields.IntegerField', [], {}),
            'numeroCarasTrajabadas': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'otrosValoresDeLaPiedra': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'revisoFicha': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'supervisorFicha': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.plano': {
            'Meta': {'object_name': 'Plano'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroPlano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.prospsistpiedra': {
            'Meta': {'object_name': 'ProspSistPiedra', '_ormbases': ['anarapp.MecObtInformacion']},
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.recursomultimedia': {
            'Meta': {'object_name': 'RecursoMultimedia', '_ormbases': ['anarapp.MaterialApoyo']},
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.reprograf': {
            'Meta': {'object_name': 'ReproGraf', '_ormbases': ['anarapp.MaterialApoyo']},
            'instituto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'numPiezas': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.reprografescalanatural': {
            'Meta': {'object_name': 'ReproGrafEscalaNatural', '_ormbases': ['anarapp.ReproGraf']},
            'reprograf_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ReproGraf']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.reprografescalanaturalpiedra': {
            'Meta': {'object_name': 'ReproGrafEscalaNaturalPiedra', '_ormbases': ['anarapp.ReproGraf']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'reprograf_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ReproGraf']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.reprografescalared': {
            'Meta': {'object_name': 'ReproGrafEscalaRed', '_ormbases': ['anarapp.ReproGraf']},
            'reprograf_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ReproGraf']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.reprografescalaredpied': {
            'Meta': {'object_name': 'ReproGrafEscalaRedPied', '_ormbases': ['anarapp.ReproGraf']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'reprograf_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ReproGraf']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.supervisadapor': {
            'Meta': {'object_name': 'SupervisadaPor'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.tecnicaparageoglifo': {
            'Meta': {'object_name': 'TecnicaParaGeoglifo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnicas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamicropetro': {
            'Meta': {'object_name': 'TecnicaParaMicroPetro'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamonumentos': {
            'Meta': {'object_name': 'TecnicaParaMonumentos'},
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhir': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tecnicas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapetroglifo': {
            'Meta': {'object_name': 'TecnicaParaPetroglifo'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapintura': {
            'Meta': {'object_name': 'TecnicaParaPintura'},
            'conDedo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'soplado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tenenciadetierra': {
            'Meta': {'object_name': 'TenenciaDeTierra'},
            'esABRAE': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esComunal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esEjido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMunicipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPrivada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTenenciaOtros': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.texturasuelo': {
            'Meta': {'object_name': 'TexturaSuelo'},
            'esArcilloso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esArenoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPedregoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRocaMadre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mixto': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoexposicionyac': {
            'Meta': {'object_name': 'TipoExposicionYac'},
            'expuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expuestoPeriodicamente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipomanifestacion': {
            'Meta': {'object_name': 'TipoManifestacion'},
            'esAmolador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBatea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroMitConDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroMitConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroMitConPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroMitNat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCupula': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGeoglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhir': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhirConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhirConPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhirConPuntos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMicroPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonoConGrab': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonumentoMegalitico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMortero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPetroglifoPintado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPiedraMitNat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPuntoAcoplado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoyacimiento': {
            'Meta': {'object_name': 'TipoYacimiento'},
            'esAbrigo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCueva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCuevadeRec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esParedRocosa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRoca': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTerrenoPro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTerrenoSup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tratfotografia': {
            'Meta': {'object_name': 'TratFotografia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limpiezaCon': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'otrosTratamientosFotografia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'programaVersion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'rellenoSurcos': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tratamientoDigital': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.ubicacionyacimiento': {
            'Meta': {'object_name': 'UbicacionYacimiento'},
            'enAcantilado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enBarranco': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCima': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCosta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enFalda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enFila': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enIsla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enLadera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enLecho': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enMargenDer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enMargenIzq': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPieMonte': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRaudal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enValle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.usoactsuelo': {
            'Meta': {'object_name': 'UsoActSuelo'},
            'esAgriRiesgo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAgriTemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esForestal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGanadero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSueloTuristico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSueloUrbano': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.verificadoenpiedra': {
            'Meta': {'object_name': 'VerificadoEnPiedra', '_ormbases': ['anarapp.MecObtInformacion']},
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.video': {
            'Meta': {'object_name': 'Video', '_ormbases': ['anarapp.Grabacion']},
            'grabacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Grabacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.videopiedra': {
            'Meta': {'object_name': 'VideoPiedra', '_ormbases': ['anarapp.Grabacion']},
            'grabacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Grabacion']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.yacimiento': {
            'Meta': {'object_name': 'Yacimiento'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['anarapp']