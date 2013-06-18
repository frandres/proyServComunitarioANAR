# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UbicacionCarasTrabajadas'
        db.create_table('anarapp_ubicacioncarastrabajadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('todaLaCaverna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('areasEspecificas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('salaPrincipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otraSala', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lagoInterior', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('claraboya', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bocaPrincipal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('tieneLuminosidad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('luminosidad', self.gf('django.db.models.fields.IntegerField')()),
            ('altura', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('requiereAndamiaje', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['UbicacionCarasTrabajadas'])

        # Adding model 'EsquemaPorCara'
        db.create_table('anarapp_esquemaporcara', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cara', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.CaraTrabajada'])),
            ('textoCara', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('posicion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['EsquemaPorCara'])

        # Adding model 'ManifestacionesPiedra'
        db.create_table('anarapp_manifestacionespiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('tienePetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneAmoladores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneCupulas', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesPiedra'])

        # Deleting field 'CaraTrabajada.luminosidad'
        db.delete_column('anarapp_caratrabajada', 'luminosidad')

        # Deleting field 'CaraTrabajada.tienePetroglifo'
        db.delete_column('anarapp_caratrabajada', 'tienePetroglifo')

        # Deleting field 'CaraTrabajada.ubicadaEnOtraSala'
        db.delete_column('anarapp_caratrabajada', 'ubicadaEnOtraSala')

        # Deleting field 'CaraTrabajada.ubicadaEnTodaLaCaverna'
        db.delete_column('anarapp_caratrabajada', 'ubicadaEnTodaLaCaverna')

        # Deleting field 'CaraTrabajada.tieneCupulas'
        db.delete_column('anarapp_caratrabajada', 'tieneCupulas')

        # Deleting field 'CaraTrabajada.ubicadaEnClaraboya'
        db.delete_column('anarapp_caratrabajada', 'ubicadaEnClaraboya')

        # Deleting field 'CaraTrabajada.orientacionDeLaCara'
        db.delete_column('anarapp_caratrabajada', 'orientacionDeLaCara')

        # Deleting field 'CaraTrabajada.conexionFiguras'
        db.delete_column('anarapp_caratrabajada', 'conexionFiguras')

        # Deleting field 'CaraTrabajada.tienePuntosAcoplados'
        db.delete_column('anarapp_caratrabajada', 'tienePuntosAcoplados')

        # Deleting field 'CaraTrabajada.ubicadaEnSalaPrincipal'
        db.delete_column('anarapp_caratrabajada', 'ubicadaEnSalaPrincipal')

        # Deleting field 'CaraTrabajada.tieneAmoladores'
        db.delete_column('anarapp_caratrabajada', 'tieneAmoladores')

        # Deleting field 'CaraTrabajada.requiereAndamiaje'
        db.delete_column('anarapp_caratrabajada', 'requiereAndamiaje')

        # Deleting field 'CaraTrabajada.ubicadaEnLagoInterior'
        db.delete_column('anarapp_caratrabajada', 'ubicadaEnLagoInterior')

        # Deleting field 'CaraTrabajada.distanciaBocaPrincipal'
        db.delete_column('anarapp_caratrabajada', 'distanciaBocaPrincipal')

        # Deleting field 'CaraTrabajada.tienePinturaRupestre'
        db.delete_column('anarapp_caratrabajada', 'tienePinturaRupestre')

        # Deleting field 'CaraTrabajada.altura'
        db.delete_column('anarapp_caratrabajada', 'altura')

        # Adding field 'CaraTrabajada.numero'
        db.add_column('anarapp_caratrabajada', 'numero',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'CaraTrabajada.orientacion'
        db.add_column('anarapp_caratrabajada', 'orientacion',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Piedra.conexionFiguras'
        db.add_column('anarapp_piedra', 'conexionFiguras',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'ConjFiguraPorTipo.seccion'
        db.delete_column('anarapp_conjfiguraportipo', 'seccion')


    def backwards(self, orm):
        # Deleting model 'UbicacionCarasTrabajadas'
        db.delete_table('anarapp_ubicacioncarastrabajadas')

        # Deleting model 'EsquemaPorCara'
        db.delete_table('anarapp_esquemaporcara')

        # Deleting model 'ManifestacionesPiedra'
        db.delete_table('anarapp_manifestacionespiedra')

        # Adding field 'CaraTrabajada.luminosidad'
        db.add_column('anarapp_caratrabajada', 'luminosidad',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'CaraTrabajada.tienePetroglifo'
        db.add_column('anarapp_caratrabajada', 'tienePetroglifo',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.ubicadaEnOtraSala'
        db.add_column('anarapp_caratrabajada', 'ubicadaEnOtraSala',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.ubicadaEnTodaLaCaverna'
        db.add_column('anarapp_caratrabajada', 'ubicadaEnTodaLaCaverna',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.tieneCupulas'
        db.add_column('anarapp_caratrabajada', 'tieneCupulas',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.ubicadaEnClaraboya'
        db.add_column('anarapp_caratrabajada', 'ubicadaEnClaraboya',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.orientacionDeLaCara'
        db.add_column('anarapp_caratrabajada', 'orientacionDeLaCara',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'CaraTrabajada.conexionFiguras'
        db.add_column('anarapp_caratrabajada', 'conexionFiguras',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'CaraTrabajada.tienePuntosAcoplados'
        db.add_column('anarapp_caratrabajada', 'tienePuntosAcoplados',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.ubicadaEnSalaPrincipal'
        db.add_column('anarapp_caratrabajada', 'ubicadaEnSalaPrincipal',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.tieneAmoladores'
        db.add_column('anarapp_caratrabajada', 'tieneAmoladores',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.requiereAndamiaje'
        db.add_column('anarapp_caratrabajada', 'requiereAndamiaje',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.ubicadaEnLagoInterior'
        db.add_column('anarapp_caratrabajada', 'ubicadaEnLagoInterior',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.distanciaBocaPrincipal'
        db.add_column('anarapp_caratrabajada', 'distanciaBocaPrincipal',
                      self.gf('django.db.models.fields.DecimalField')(default=4, max_digits=12, decimal_places=6),
                      keep_default=False)

        # Adding field 'CaraTrabajada.tienePinturaRupestre'
        db.add_column('anarapp_caratrabajada', 'tienePinturaRupestre',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CaraTrabajada.altura'
        db.add_column('anarapp_caratrabajada', 'altura',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3),
                      keep_default=False)

        # Deleting field 'CaraTrabajada.numero'
        db.delete_column('anarapp_caratrabajada', 'numero')

        # Deleting field 'CaraTrabajada.orientacion'
        db.delete_column('anarapp_caratrabajada', 'orientacion')

        # Deleting field 'Piedra.conexionFiguras'
        db.delete_column('anarapp_piedra', 'conexionFiguras')

        # Adding field 'ConjFiguraPorTipo.seccion'
        db.add_column('anarapp_conjfiguraportipo', 'seccion',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    models = {
        'anarapp.amolador': {
            'Meta': {'object_name': 'Amolador', '_ormbases': ['anarapp.TipoManifestacion']},
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'diametro': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.batea': {
            'Meta': {'object_name': 'Batea', '_ormbases': ['anarapp.TipoManifestacion']},
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
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
            'colorBase': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'colores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.Color']", 'symmetrical': 'False'}),
            'figuraRellena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'figurasSuperPuestas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impresionDeManos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.ImpresionDeManos']", 'symmetrical': 'False'}),
            'tecnicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TecnicaPinturaRupestre']", 'symmetrical': 'False'}),
            'tipoDeLineas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TipoLinea']", 'symmetrical': 'False'})
        },
        'anarapp.caracdepetroglifo': {
            'Meta': {'object_name': 'CaracDePetroglifo'},
            'caracteristicasSurcoGrabado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.caratrabajada': {
            'Meta': {'object_name': 'CaraTrabajada'},
            'alto': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'orientacion': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.cerromiticonatural': {
            'Meta': {'object_name': 'CerroMiticoNatural', '_ormbases': ['anarapp.TipoManifestacion']},
            'conDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.color': {
            'Meta': {'object_name': 'Color'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parametroC': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parametroK': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parametroM': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parametroY': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'anarapp.comunicacionpersonal': {
            'Meta': {'object_name': 'ComunicacionPersonal', '_ormbases': ['anarapp.MecObtInformacion']},
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'direccionEmail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nombreFacebook': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'paginaWeb': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'telefonoCel': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.cortezaarbol': {
            'Meta': {'object_name': 'CortezaArbol', '_ormbases': ['anarapp.Material']},
            'material_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Material']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.cronologiatentativa': {
            'Meta': {'object_name': 'CronologiaTentativa'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'cronologia': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.cupulas': {
            'Meta': {'object_name': 'Cupulas', '_ormbases': ['anarapp.TipoManifestacion']},
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'diametro': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.destpotencialsitio': {
            'Meta': {'object_name': 'DestPotencialSitio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otrasCausasPosibleDestruccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tipoModificacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.dimensionpiedra': {
            'Meta': {'object_name': 'DimensionPiedra'},
            'altoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.dolmen': {
            'Meta': {'object_name': 'Dolmen', '_ormbases': ['anarapp.MonumentoMegalitico']},
            'cantidadConPetroglifos': ('django.db.models.fields.IntegerField', [], {}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {}),
            'monumentomegalitico_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MonumentoMegalitico']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.esquemaporcara': {
            'Meta': {'object_name': 'EsquemaPorCara'},
            'cara': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.CaraTrabajada']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posicion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'textoCara': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.estadoconservacion': {
            'Meta': {'object_name': 'EstadoConservacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoSitio': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fichapiedra': {
            'Meta': {'object_name': 'FichaPiedra'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fechaLlenado': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fechaSupervision': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'supervisor': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.fotografia': {
            'Meta': {'object_name': 'Fotografia', '_ormbases': ['anarapp.MaterialApoyo']},
            'esDeAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fotografia': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fotografo': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'numCopiaAnar': ('django.db.models.fields.IntegerField', [], {}),
            'numMarcaNegativo': ('django.db.models.fields.IntegerField', [], {}),
            'numReferencia': ('django.db.models.fields.IntegerField', [], {}),
            'numRollo': ('django.db.models.fields.IntegerField', [], {}),
            'tipoFotografia': ('django.db.models.fields.IntegerField', [], {})
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
        'anarapp.geoglifo': {
            'Meta': {'object_name': 'Geoglifo', '_ormbases': ['anarapp.TipoManifestacion']},
            'tecnicaConstruccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
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
        'anarapp.gradodestruccionsitio': {
            'Meta': {'object_name': 'GradoDestruccionSitio'},
            'causaYEfecto': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoModificacion': ('django.db.models.fields.IntegerField', [], {}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.hidrologia': {
            'Meta': {'object_name': 'Hidrologia'},
            'distanciaYacimiento': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'hidrologia': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.hueso': {
            'Meta': {'object_name': 'Hueso', '_ormbases': ['anarapp.Material']},
            'material_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Material']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.imagenreprograf': {
            'Meta': {'object_name': 'ImagenReproGraf'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reproduccionGrafica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.ReproGraf']"})
        },
        'anarapp.impresiondemanos': {
            'Meta': {'object_name': 'ImpresionDeManos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.lineacompuesta': {
            'Meta': {'object_name': 'LineaCompuesta', '_ormbases': ['anarapp.TipoLinea']},
            'tipolinea_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoLinea']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.lineasencilla': {
            'Meta': {'object_name': 'LineaSencilla', '_ormbases': ['anarapp.TipoLinea']},
            'tipolinea_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoLinea']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.localidadyacimiento': {
            'Meta': {'object_name': 'LocalidadYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreLocalidad': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.localidadyacimientopoblado': {
            'Meta': {'object_name': 'LocalidadYacimientoPoblado', '_ormbases': ['anarapp.LocalidadYacimiento']},
            'localidadyacimiento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LocalidadYacimiento']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoCentroPoblado': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.locyacnopoblado': {
            'Meta': {'object_name': 'LocYacNoPoblado', '_ormbases': ['anarapp.LocalidadYacimiento']},
            'localidadyacimiento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LocalidadYacimiento']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.manifestacionesasociadas': {
            'Meta': {'object_name': 'ManifestacionesAsociadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifestacionAsociada': ('django.db.models.fields.IntegerField', [], {}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.manifestacionespiedra': {
            'Meta': {'object_name': 'ManifestacionesPiedra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'tieneAmoladores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        'anarapp.material': {
            'Meta': {'object_name': 'Material'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.materialapoyo': {
            'Meta': {'object_name': 'MaterialApoyo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.mecobtinformacion': {
            'Meta': {'object_name': 'MecObtInformacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.menhir': {
            'Meta': {'object_name': 'Menhir', '_ormbases': ['anarapp.MonumentoMegalitico']},
            'cantidadConPetroglifos': ('django.db.models.fields.IntegerField', [], {}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {}),
            'cantidadConPuntosAcoplados': ('django.db.models.fields.IntegerField', [], {}),
            'cantidadPiedrasVerticales': ('django.db.models.fields.IntegerField', [], {}),
            'distanciamiento': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'monumentomegalitico_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MonumentoMegalitico']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.micropetroglifo': {
            'Meta': {'object_name': 'MicroPetroglifo', '_ormbases': ['anarapp.TipoManifestacion']},
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.modificacionyacimiento': {
            'Meta': {'object_name': 'ModificacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pas': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipoModificacion': ('django.db.models.fields.IntegerField', [], {}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.monolito': {
            'Meta': {'object_name': 'Monolito', '_ormbases': ['anarapp.MonumentoMegalitico']},
            'cantidadDeMonolitos': ('django.db.models.fields.IntegerField', [], {}),
            'cantidadDeMonolitosGrabados': ('django.db.models.fields.IntegerField', [], {}),
            'monumentomegalitico_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MonumentoMegalitico']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.monumentomegalitico': {
            'Meta': {'object_name': 'MonumentoMegalitico', '_ormbases': ['anarapp.TipoManifestacion']},
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.mortero': {
            'Meta': {'object_name': 'Mortero', '_ormbases': ['anarapp.TipoManifestacion']},
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.negativo': {
            'Meta': {'object_name': 'Negativo', '_ormbases': ['anarapp.ImpresionDeManos']},
            'caracteristicasPinturaRupestre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.CaracDeLaPintura']"}),
            'impresiondemanos_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ImpresionDeManos']", 'unique': 'True', 'primary_key': 'True'}),
            'planoAmarillo': ('django.db.models.fields.IntegerField', [], {}),
            'planoBlanco': ('django.db.models.fields.IntegerField', [], {}),
            'planoDosRojo': ('django.db.models.fields.IntegerField', [], {}),
            'planoNegro': ('django.db.models.fields.IntegerField', [], {}),
            'planoTresRojo': ('django.db.models.fields.IntegerField', [], {}),
            'planoUnRojo': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.orientacionyacimiento': {
            'Meta': {'object_name': 'OrientacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientacionCardinal': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'orientacionYacimiento': ('django.db.models.fields.IntegerField', [], {}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.otros': {
            'Meta': {'object_name': 'Otros', '_ormbases': ['anarapp.Material']},
            'especificacion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'material_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Material']", 'unique': 'True', 'primary_key': 'True'})
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
        'anarapp.petroglifo': {
            'Meta': {'object_name': 'Petroglifo', '_ormbases': ['anarapp.TipoManifestacion']},
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMinimo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'caracteristicasPetroglifo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.CaracDePetroglifo']", 'symmetrical': 'False'}),
            'pintado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profundidadMaxima': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'profundidadMinima': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tecnicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TecnicaPetroglifo']", 'symmetrical': 'False'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.piedra': {
            'Meta': {'object_name': 'Piedra'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'conexionFiguras': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifiestacionAsociada': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombreFiguras': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'numeroCaras': ('django.db.models.fields.IntegerField', [], {}),
            'numeroCarasTrajabadas': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'otrosValoresDeLaPiedra': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.piedriamiticanatural': {
            'Meta': {'object_name': 'PiedriaMiticaNatural', '_ormbases': ['anarapp.TipoManifestacion']},
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.pieles': {
            'Meta': {'object_name': 'Pieles', '_ormbases': ['anarapp.Material']},
            'material_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Material']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.pinturarupestre': {
            'Meta': {'object_name': 'PinturaRupestre', '_ormbases': ['anarapp.TipoManifestacion']},
            'caracteristicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.CaracDeLaPintura']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.positivo': {
            'Meta': {'object_name': 'Positivo', '_ormbases': ['anarapp.ImpresionDeManos']},
            'caracteristicasPinturaRupestre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.CaracDeLaPintura']"}),
            'impresiondemanos_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ImpresionDeManos']", 'unique': 'True', 'primary_key': 'True'}),
            'planoAmarillo': ('django.db.models.fields.IntegerField', [], {}),
            'planoBlanco': ('django.db.models.fields.IntegerField', [], {}),
            'planoDosRojo': ('django.db.models.fields.IntegerField', [], {}),
            'planoNegro': ('django.db.models.fields.IntegerField', [], {}),
            'planoTresRojo': ('django.db.models.fields.IntegerField', [], {}),
            'planoUnRojo': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.prospeccionsistematica': {
            'Meta': {'object_name': 'ProspeccionSistematica', '_ormbases': ['anarapp.MecObtInformacion']},
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.prospsistpiedra': {
            'Meta': {'object_name': 'ProspSistPiedra', '_ormbases': ['anarapp.MecObtInformacion']},
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.puntosacoplados': {
            'Meta': {'object_name': 'PuntosAcoplados', '_ormbases': ['anarapp.TipoManifestacion']},
            'punteado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipomanifestacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TipoManifestacion']", 'unique': 'True', 'primary_key': 'True'})
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
        'anarapp.roca': {
            'Meta': {'object_name': 'Roca', '_ormbases': ['anarapp.Material']},
            'material_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Material']", 'unique': 'True', 'primary_key': 'True'}),
            'origenPiedra': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.tecnicapetroglifo': {
            'Meta': {'object_name': 'TecnicaPetroglifo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.IntegerField', [], {}),
            'otro': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.tecnicapinturarupestre': {
            'Meta': {'object_name': 'TecnicaPinturaRupestre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otro': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tecnica': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.tenenciadelatierra': {
            'Meta': {'object_name': 'TenenciaDeLaTierra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tipoTenenciaDeLaTierra': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.texturasuelo': {
            'Meta': {'object_name': 'TexturaSuelo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mixto': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'texturaSuelo': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.tierra': {
            'Meta': {'object_name': 'Tierra', '_ormbases': ['anarapp.Material']},
            'material_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Material']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.tipolinea': {
            'Meta': {'object_name': 'TipoLinea'},
            'anchoLineaDesde': ('django.db.models.fields.IntegerField', [], {}),
            'anchoLineaHasta': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.tipomanifestacion': {
            'Meta': {'object_name': 'TipoManifestacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.tipoyacimiento': {
            'Meta': {'object_name': 'TipoYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoSitio': ('django.db.models.fields.IntegerField', [], {})
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
        'anarapp.ubicacioncarastrabajadas': {
            'Meta': {'object_name': 'UbicacionCarasTrabajadas'},
            'altura': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'areasEspecificas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bocaPrincipal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'claraboya': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lagoInterior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'luminosidad': ('django.db.models.fields.IntegerField', [], {}),
            'otraSala': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'requiereAndamiaje': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'salaPrincipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneLuminosidad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'todaLaCaverna': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.ubicacionyacimiento': {
            'Meta': {'object_name': 'UbicacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ubicacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.usoactualdelsuelo': {
            'Meta': {'object_name': 'UsoActualDelSuelo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoUsoActualSuelo': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.verificadoencampo': {
            'Meta': {'object_name': 'VerificadoEncampo', '_ormbases': ['anarapp.MecObtInformacion']},
            'mecobtinformacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MecObtInformacion']", 'unique': 'True', 'primary_key': 'True'})
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
            'altura': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'datum': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'destruccionPotencialSitio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.DestPotencialSitio']", 'symmetrical': 'False'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'estadoConservacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.EstadoConservacion']", 'symmetrical': 'False'}),
            'fauna': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'flora': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'fotografia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fotografias_yacimiento'", 'symmetrical': 'False', 'to': "orm['anarapp.Fotografia']"}),
            'hidrologia': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.Hidrologia']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicacionesEsquemaLlegada': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'latitud': ('django.db.models.fields.FloatField', [], {}),
            'latitud_grados': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'latitud_minutos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'latitud_segundos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {}),
            'longitud_grados': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'longitud_minutos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'longitud_segundos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'manifestacionesAsociadas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.ManifestacionesAsociadas']", 'symmetrical': 'False'}),
            'materiales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.Material']", 'symmetrical': 'False'}),
            'materialesApoyo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.MaterialApoyo']", 'symmetrical': 'False'}),
            'mecanismosObtencionInformacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.MecObtInformacion']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numPiedrasYacimientoColocadas': ('django.db.models.fields.IntegerField', [], {}),
            'numPiedrasYacimientoGrabadas': ('django.db.models.fields.IntegerField', [], {}),
            'numPiedrasYacimientoOriginal': ('django.db.models.fields.IntegerField', [], {}),
            'numPiedrasYacimientoPintadas': ('django.db.models.fields.IntegerField', [], {}),
            'numeroPlano': ('django.db.models.fields.IntegerField', [], {}),
            'observacionesDestruccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'observacionesExposicion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'orientacionYacimiento': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.OrientacionYacimiento']", 'symmetrical': 'False'}),
            'otrasNotas': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'otrosConstitucionYacimiento': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'otrosValoresSitio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'superficie': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tenenciaDeLatierra': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TenenciaDeLaTierra']", 'symmetrical': 'False'}),
            'texturaSuelo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TexturaSuelo']", 'symmetrical': 'False'}),
            'tiempoDestruccion': ('django.db.models.fields.IntegerField', [], {}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {}),
            'tipoExposicion': ('django.db.models.fields.IntegerField', [], {}),
            'tipoSitio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TipoYacimiento']", 'symmetrical': 'False'}),
            'ubicacionYacimiento': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.UbicacionYacimiento']", 'symmetrical': 'False'}),
            'usoDelSuelo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.UsoActualDelSuelo']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['anarapp']