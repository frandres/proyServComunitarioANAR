# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MecObtInformacion'
        db.create_table('anarapp_mecobtinformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MecObtInformacion'])

        # Adding model 'ProspeccionSistematica'
        db.create_table('anarapp_prospeccionsistematica', (
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['ProspeccionSistematica'])

        # Adding model 'ComunicacionPersonal'
        db.create_table('anarapp_comunicacionpersonal', (
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
        ))
        db.send_create_signal('anarapp', ['ComunicacionPersonal'])

        # Adding model 'VerificadoEncampo'
        db.create_table('anarapp_verificadoencampo', (
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['VerificadoEncampo'])

        # Adding model 'DestPotencialSitio'
        db.create_table('anarapp_destpotencialsitio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoModificacion', self.gf('django.db.models.fields.IntegerField')()),
            ('otrasCausasPosibleDestruccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['DestPotencialSitio'])

        # Adding model 'EstadoConservacion'
        db.create_table('anarapp_estadoconservacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoSitio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EstadoConservacion'])

        # Adding model 'Material'
        db.create_table('anarapp_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Material'])

        # Adding model 'Roca'
        db.create_table('anarapp_roca', (
            ('material_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Material'], unique=True, primary_key=True)),
            ('origenPiedra', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Roca'])

        # Adding model 'Tierra'
        db.create_table('anarapp_tierra', (
            ('material_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Material'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Tierra'])

        # Adding model 'Hueso'
        db.create_table('anarapp_hueso', (
            ('material_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Material'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Hueso'])

        # Adding model 'CortezaArbol'
        db.create_table('anarapp_cortezaarbol', (
            ('material_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Material'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['CortezaArbol'])

        # Adding model 'Pieles'
        db.create_table('anarapp_pieles', (
            ('material_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Material'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Pieles'])

        # Adding model 'Otros'
        db.create_table('anarapp_otros', (
            ('material_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Material'], unique=True, primary_key=True)),
            ('especificacion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Otros'])

        # Adding model 'Hidrologia'
        db.create_table('anarapp_hidrologia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hidrologia', self.gf('django.db.models.fields.IntegerField')()),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('distanciaYacimiento', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('anarapp', ['Hidrologia'])

        # Adding model 'TexturaSuelo'
        db.create_table('anarapp_texturasuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texturaSuelo', self.gf('django.db.models.fields.IntegerField')()),
            ('mixto', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['TexturaSuelo'])

        # Adding model 'OrientacionYacimiento'
        db.create_table('anarapp_orientacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('orientacionCardinal', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('orientacionYacimiento', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['OrientacionYacimiento'])

        # Adding model 'UbicacionYacimiento'
        db.create_table('anarapp_ubicacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ubicacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['UbicacionYacimiento'])

        # Adding model 'TipoYacimiento'
        db.create_table('anarapp_tipoyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoSitio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['TipoYacimiento'])

        # Adding model 'MaterialApoyo'
        db.create_table('anarapp_materialapoyo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MaterialApoyo'])

        # Adding model 'UsoActualDelSuelo'
        db.create_table('anarapp_usoactualdelsuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoUsoActualSuelo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['UsoActualDelSuelo'])

        # Adding model 'TenenciaDeLaTierra'
        db.create_table('anarapp_tenenciadelatierra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tipoTenenciaDeLaTierra', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['TenenciaDeLaTierra'])

        # Adding model 'Fotografia'
        db.create_table('anarapp_fotografia', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('fotografo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fotografia', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('numRollo', self.gf('django.db.models.fields.IntegerField')()),
            ('numMarcaNegativo', self.gf('django.db.models.fields.IntegerField')()),
            ('esDeAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiaAnar', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoFotografia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Fotografia'])

        # Adding model 'ManifestacionesAsociadas'
        db.create_table('anarapp_manifestacionesasociadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manifestacionAsociada', self.gf('django.db.models.fields.IntegerField')()),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesAsociadas'])

        # Adding model 'Yacimiento'
        db.create_table('anarapp_yacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitud', self.gf('django.db.models.fields.FloatField')()),
            ('latitud', self.gf('django.db.models.fields.FloatField')()),
            ('longitud_grados', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('longitud_minutos', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('longitud_segundos', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('latitud_grados', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('latitud_minutos', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('latitud_segundos', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('tipoDatum', self.gf('django.db.models.fields.IntegerField')()),
            ('datum', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('altura', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('superficie', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('numeroPlano', self.gf('django.db.models.fields.IntegerField')()),
            ('indicacionesEsquemaLlegada', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('flora', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('fauna', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('observacionesExposicion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tipoExposicion', self.gf('django.db.models.fields.IntegerField')()),
            ('numPiedrasYacimientoOriginal', self.gf('django.db.models.fields.IntegerField')()),
            ('numPiedrasYacimientoGrabadas', self.gf('django.db.models.fields.IntegerField')()),
            ('numPiedrasYacimientoPintadas', self.gf('django.db.models.fields.IntegerField')()),
            ('numPiedrasYacimientoColocadas', self.gf('django.db.models.fields.IntegerField')()),
            ('otrosConstitucionYacimiento', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('otrasNotas', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('observacionesDestruccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tiempoDestruccion', self.gf('django.db.models.fields.IntegerField')()),
            ('otrosValoresSitio', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Yacimiento'])

        # Adding M2M table for field usoDelSuelo on 'Yacimiento'
        db.create_table('anarapp_yacimiento_usoDelSuelo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('usoactualdelsuelo', models.ForeignKey(orm['anarapp.usoactualdelsuelo'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_usoDelSuelo', ['yacimiento_id', 'usoactualdelsuelo_id'])

        # Adding M2M table for field tenenciaDeLatierra on 'Yacimiento'
        db.create_table('anarapp_yacimiento_tenenciaDeLatierra', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('tenenciadelatierra', models.ForeignKey(orm['anarapp.tenenciadelatierra'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_tenenciaDeLatierra', ['yacimiento_id', 'tenenciadelatierra_id'])

        # Adding M2M table for field fotografia on 'Yacimiento'
        db.create_table('anarapp_yacimiento_fotografia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('fotografia', models.ForeignKey(orm['anarapp.fotografia'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_fotografia', ['yacimiento_id', 'fotografia_id'])

        # Adding M2M table for field tipoSitio on 'Yacimiento'
        db.create_table('anarapp_yacimiento_tipoSitio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('tipoyacimiento', models.ForeignKey(orm['anarapp.tipoyacimiento'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_tipoSitio', ['yacimiento_id', 'tipoyacimiento_id'])

        # Adding M2M table for field ubicacionYacimiento on 'Yacimiento'
        db.create_table('anarapp_yacimiento_ubicacionYacimiento', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('ubicacionyacimiento', models.ForeignKey(orm['anarapp.ubicacionyacimiento'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_ubicacionYacimiento', ['yacimiento_id', 'ubicacionyacimiento_id'])

        # Adding M2M table for field orientacionYacimiento on 'Yacimiento'
        db.create_table('anarapp_yacimiento_orientacionYacimiento', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('orientacionyacimiento', models.ForeignKey(orm['anarapp.orientacionyacimiento'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_orientacionYacimiento', ['yacimiento_id', 'orientacionyacimiento_id'])

        # Adding M2M table for field texturaSuelo on 'Yacimiento'
        db.create_table('anarapp_yacimiento_texturaSuelo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('texturasuelo', models.ForeignKey(orm['anarapp.texturasuelo'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_texturaSuelo', ['yacimiento_id', 'texturasuelo_id'])

        # Adding M2M table for field hidrologia on 'Yacimiento'
        db.create_table('anarapp_yacimiento_hidrologia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('hidrologia', models.ForeignKey(orm['anarapp.hidrologia'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_hidrologia', ['yacimiento_id', 'hidrologia_id'])

        # Adding M2M table for field materiales on 'Yacimiento'
        db.create_table('anarapp_yacimiento_materiales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('material', models.ForeignKey(orm['anarapp.material'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_materiales', ['yacimiento_id', 'material_id'])

        # Adding M2M table for field estadoConservacion on 'Yacimiento'
        db.create_table('anarapp_yacimiento_estadoConservacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('estadoconservacion', models.ForeignKey(orm['anarapp.estadoconservacion'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_estadoConservacion', ['yacimiento_id', 'estadoconservacion_id'])

        # Adding M2M table for field destruccionPotencialSitio on 'Yacimiento'
        db.create_table('anarapp_yacimiento_destruccionPotencialSitio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('destpotencialsitio', models.ForeignKey(orm['anarapp.destpotencialsitio'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_destruccionPotencialSitio', ['yacimiento_id', 'destpotencialsitio_id'])

        # Adding M2M table for field manifestacionesAsociadas on 'Yacimiento'
        db.create_table('anarapp_yacimiento_manifestacionesAsociadas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('manifestacionesasociadas', models.ForeignKey(orm['anarapp.manifestacionesasociadas'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_manifestacionesAsociadas', ['yacimiento_id', 'manifestacionesasociadas_id'])

        # Adding M2M table for field materialesApoyo on 'Yacimiento'
        db.create_table('anarapp_yacimiento_materialesApoyo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('materialapoyo', models.ForeignKey(orm['anarapp.materialapoyo'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_materialesApoyo', ['yacimiento_id', 'materialapoyo_id'])

        # Adding M2M table for field mecanismosObtencionInformacion on 'Yacimiento'
        db.create_table('anarapp_yacimiento_mecanismosObtencionInformacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('mecobtinformacion', models.ForeignKey(orm['anarapp.mecobtinformacion'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_mecanismosObtencionInformacion', ['yacimiento_id', 'mecobtinformacion_id'])

        # Adding model 'CronologiaTentativa'
        db.create_table('anarapp_cronologiatentativa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cronologia', self.gf('django.db.models.fields.IntegerField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['CronologiaTentativa'])

        # Adding model 'GradoDestruccionSitio'
        db.create_table('anarapp_gradodestruccionsitio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('causaYEfecto', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tipoModificacion', self.gf('django.db.models.fields.IntegerField')()),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['GradoDestruccionSitio'])

        # Adding model 'ModificacionYacimiento'
        db.create_table('anarapp_modificacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('tipoModificacion', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('pas', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['ModificacionYacimiento'])

        # Adding model 'LocalidadYacimiento'
        db.create_table('anarapp_localidadyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('nombreLocalidad', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['LocalidadYacimiento'])

        # Adding model 'LocalidadYacimientoPoblado'
        db.create_table('anarapp_localidadyacimientopoblado', (
            ('localidadyacimiento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.LocalidadYacimiento'], unique=True, primary_key=True)),
            ('tipoCentroPoblado', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['LocalidadYacimientoPoblado'])

        # Adding model 'LocYacNoPoblado'
        db.create_table('anarapp_locyacnopoblado', (
            ('localidadyacimiento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.LocalidadYacimiento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['LocYacNoPoblado'])

        # Adding model 'TipoManifestacion'
        db.create_table('anarapp_tipomanifestacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['TipoManifestacion'])

        # Adding model 'Geoglifo'
        db.create_table('anarapp_geoglifo', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('tecnicaConstruccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Geoglifo'])

        # Adding model 'TipoLinea'
        db.create_table('anarapp_tipolinea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anchoLineaDesde', self.gf('django.db.models.fields.IntegerField')()),
            ('anchoLineaHasta', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['TipoLinea'])

        # Adding model 'LineaSencilla'
        db.create_table('anarapp_lineasencilla', (
            ('tipolinea_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoLinea'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['LineaSencilla'])

        # Adding model 'LineaCompuesta'
        db.create_table('anarapp_lineacompuesta', (
            ('tipolinea_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoLinea'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['LineaCompuesta'])

        # Adding model 'TecnicaPinturaRupestre'
        db.create_table('anarapp_tecnicapinturarupestre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tecnica', self.gf('django.db.models.fields.IntegerField')()),
            ('otro', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['TecnicaPinturaRupestre'])

        # Adding model 'Color'
        db.create_table('anarapp_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parametroC', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('parametroM', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('parametroY', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('parametroK', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('anarapp', ['Color'])

        # Adding model 'ImpresionDeManos'
        db.create_table('anarapp_impresiondemanos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tecnica', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ImpresionDeManos'])

        # Adding model 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('figuraRellena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('figurasSuperPuestas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('colorBase', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['CaracDeLaPintura'])

        # Adding M2M table for field tecnicas on 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura_tecnicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('caracdelapintura', models.ForeignKey(orm['anarapp.caracdelapintura'], null=False)),
            ('tecnicapinturarupestre', models.ForeignKey(orm['anarapp.tecnicapinturarupestre'], null=False))
        ))
        db.create_unique('anarapp_caracdelapintura_tecnicas', ['caracdelapintura_id', 'tecnicapinturarupestre_id'])

        # Adding M2M table for field impresionDeManos on 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura_impresionDeManos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('caracdelapintura', models.ForeignKey(orm['anarapp.caracdelapintura'], null=False)),
            ('impresiondemanos', models.ForeignKey(orm['anarapp.impresiondemanos'], null=False))
        ))
        db.create_unique('anarapp_caracdelapintura_impresionDeManos', ['caracdelapintura_id', 'impresiondemanos_id'])

        # Adding M2M table for field colores on 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura_colores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('caracdelapintura', models.ForeignKey(orm['anarapp.caracdelapintura'], null=False)),
            ('color', models.ForeignKey(orm['anarapp.color'], null=False))
        ))
        db.create_unique('anarapp_caracdelapintura_colores', ['caracdelapintura_id', 'color_id'])

        # Adding M2M table for field tipoDeLineas on 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura_tipoDeLineas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('caracdelapintura', models.ForeignKey(orm['anarapp.caracdelapintura'], null=False)),
            ('tipolinea', models.ForeignKey(orm['anarapp.tipolinea'], null=False))
        ))
        db.create_unique('anarapp_caracdelapintura_tipoDeLineas', ['caracdelapintura_id', 'tipolinea_id'])

        # Adding model 'Positivo'
        db.create_table('anarapp_positivo', (
            ('impresiondemanos_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ImpresionDeManos'], unique=True, primary_key=True)),
            ('planoNegro', self.gf('django.db.models.fields.IntegerField')()),
            ('planoBlanco', self.gf('django.db.models.fields.IntegerField')()),
            ('planoAmarillo', self.gf('django.db.models.fields.IntegerField')()),
            ('planoUnRojo', self.gf('django.db.models.fields.IntegerField')()),
            ('planoDosRojo', self.gf('django.db.models.fields.IntegerField')()),
            ('planoTresRojo', self.gf('django.db.models.fields.IntegerField')()),
            ('caracteristicasPinturaRupestre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.CaracDeLaPintura'])),
        ))
        db.send_create_signal('anarapp', ['Positivo'])

        # Adding model 'Negativo'
        db.create_table('anarapp_negativo', (
            ('impresiondemanos_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ImpresionDeManos'], unique=True, primary_key=True)),
            ('planoNegro', self.gf('django.db.models.fields.IntegerField')()),
            ('planoBlanco', self.gf('django.db.models.fields.IntegerField')()),
            ('planoAmarillo', self.gf('django.db.models.fields.IntegerField')()),
            ('planoUnRojo', self.gf('django.db.models.fields.IntegerField')()),
            ('planoDosRojo', self.gf('django.db.models.fields.IntegerField')()),
            ('planoTresRojo', self.gf('django.db.models.fields.IntegerField')()),
            ('caracteristicasPinturaRupestre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.CaracDeLaPintura'])),
        ))
        db.send_create_signal('anarapp', ['Negativo'])

        # Adding model 'PinturaRupestre'
        db.create_table('anarapp_pinturarupestre', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['PinturaRupestre'])

        # Adding M2M table for field caracteristicas on 'PinturaRupestre'
        db.create_table('anarapp_pinturarupestre_caracteristicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pinturarupestre', models.ForeignKey(orm['anarapp.pinturarupestre'], null=False)),
            ('caracdelapintura', models.ForeignKey(orm['anarapp.caracdelapintura'], null=False))
        ))
        db.create_unique('anarapp_pinturarupestre_caracteristicas', ['pinturarupestre_id', 'caracdelapintura_id'])

        # Adding model 'TecnicaPetroglifo'
        db.create_table('anarapp_tecnicapetroglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material', self.gf('django.db.models.fields.IntegerField')()),
            ('otro', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['TecnicaPetroglifo'])

        # Adding model 'CaracDePetroglifo'
        db.create_table('anarapp_caracdepetroglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caracteristicasSurcoGrabado', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['CaracDePetroglifo'])

        # Adding model 'Petroglifo'
        db.create_table('anarapp_petroglifo', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('pintado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anchoMinimo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('anchoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('profundidadMinima', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('profundidadMaxima', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['Petroglifo'])

        # Adding M2M table for field tecnicas on 'Petroglifo'
        db.create_table('anarapp_petroglifo_tecnicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('petroglifo', models.ForeignKey(orm['anarapp.petroglifo'], null=False)),
            ('tecnicapetroglifo', models.ForeignKey(orm['anarapp.tecnicapetroglifo'], null=False))
        ))
        db.create_unique('anarapp_petroglifo_tecnicas', ['petroglifo_id', 'tecnicapetroglifo_id'])

        # Adding M2M table for field caracteristicasPetroglifo on 'Petroglifo'
        db.create_table('anarapp_petroglifo_caracteristicasPetroglifo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('petroglifo', models.ForeignKey(orm['anarapp.petroglifo'], null=False)),
            ('caracdepetroglifo', models.ForeignKey(orm['anarapp.caracdepetroglifo'], null=False))
        ))
        db.create_unique('anarapp_petroglifo_caracteristicasPetroglifo', ['petroglifo_id', 'caracdepetroglifo_id'])

        # Adding model 'MicroPetroglifo'
        db.create_table('anarapp_micropetroglifo', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MicroPetroglifo'])

        # Adding model 'PiedriaMiticaNatural'
        db.create_table('anarapp_piedriamiticanatural', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['PiedriaMiticaNatural'])

        # Adding model 'CerroMiticoNatural'
        db.create_table('anarapp_cerromiticonatural', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('conPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('conPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('conDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['CerroMiticoNatural'])

        # Adding model 'MonumentoMegalitico'
        db.create_table('anarapp_monumentomegalitico', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MonumentoMegalitico'])

        # Adding model 'Monolito'
        db.create_table('anarapp_monolito', (
            ('monumentomegalitico_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MonumentoMegalitico'], unique=True, primary_key=True)),
            ('cantidadDeMonolitos', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidadDeMonolitosGrabados', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Monolito'])

        # Adding model 'Menhir'
        db.create_table('anarapp_menhir', (
            ('monumentomegalitico_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MonumentoMegalitico'], unique=True, primary_key=True)),
            ('cantidadPiedrasVerticales', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidadConPuntosAcoplados', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidadConPetroglifos', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidadConPinturas', self.gf('django.db.models.fields.IntegerField')()),
            ('distanciamiento', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['Menhir'])

        # Adding model 'Dolmen'
        db.create_table('anarapp_dolmen', (
            ('monumentomegalitico_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MonumentoMegalitico'], unique=True, primary_key=True)),
            ('cantidadConPetroglifos', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidadConPinturas', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Dolmen'])

        # Adding model 'Amolador'
        db.create_table('anarapp_amolador', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('diametro', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['Amolador'])

        # Adding model 'Batea'
        db.create_table('anarapp_batea', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['Batea'])

        # Adding model 'PuntosAcoplados'
        db.create_table('anarapp_puntosacoplados', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('punteado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['PuntosAcoplados'])

        # Adding model 'Cupulas'
        db.create_table('anarapp_cupulas', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('diametro', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['Cupulas'])

        # Adding model 'Mortero'
        db.create_table('anarapp_mortero', (
            ('tipomanifestacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TipoManifestacion'], unique=True, primary_key=True)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['Mortero'])

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
            ('altoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('largoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('anchoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('otrosValoresDeLaPiedra', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('autorFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fechaEscrituraFicha', self.gf('django.db.models.fields.DateField')()),
            ('supervisorFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fechaSupervisionFicha', self.gf('django.db.models.fields.DateField')()),
            ('revisoFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['Piedra'])

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

        # Adding model 'ComunicacionPersonalPiedra'
        db.create_table('anarapp_comunicacionpersonalpiedra', (
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
        db.send_create_signal('anarapp', ['ComunicacionPersonalPiedra'])

        # Adding model 'VerificadoEnPiedra'
        db.create_table('anarapp_verificadoenpiedra', (
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['VerificadoEnPiedra'])


    def backwards(self, orm):
        # Deleting model 'MecObtInformacion'
        db.delete_table('anarapp_mecobtinformacion')

        # Deleting model 'ProspeccionSistematica'
        db.delete_table('anarapp_prospeccionsistematica')

        # Deleting model 'ComunicacionPersonal'
        db.delete_table('anarapp_comunicacionpersonal')

        # Deleting model 'VerificadoEncampo'
        db.delete_table('anarapp_verificadoencampo')

        # Deleting model 'DestPotencialSitio'
        db.delete_table('anarapp_destpotencialsitio')

        # Deleting model 'EstadoConservacion'
        db.delete_table('anarapp_estadoconservacion')

        # Deleting model 'Material'
        db.delete_table('anarapp_material')

        # Deleting model 'Roca'
        db.delete_table('anarapp_roca')

        # Deleting model 'Tierra'
        db.delete_table('anarapp_tierra')

        # Deleting model 'Hueso'
        db.delete_table('anarapp_hueso')

        # Deleting model 'CortezaArbol'
        db.delete_table('anarapp_cortezaarbol')

        # Deleting model 'Pieles'
        db.delete_table('anarapp_pieles')

        # Deleting model 'Otros'
        db.delete_table('anarapp_otros')

        # Deleting model 'Hidrologia'
        db.delete_table('anarapp_hidrologia')

        # Deleting model 'TexturaSuelo'
        db.delete_table('anarapp_texturasuelo')

        # Deleting model 'OrientacionYacimiento'
        db.delete_table('anarapp_orientacionyacimiento')

        # Deleting model 'UbicacionYacimiento'
        db.delete_table('anarapp_ubicacionyacimiento')

        # Deleting model 'TipoYacimiento'
        db.delete_table('anarapp_tipoyacimiento')

        # Deleting model 'MaterialApoyo'
        db.delete_table('anarapp_materialapoyo')

        # Deleting model 'UsoActualDelSuelo'
        db.delete_table('anarapp_usoactualdelsuelo')

        # Deleting model 'TenenciaDeLaTierra'
        db.delete_table('anarapp_tenenciadelatierra')

        # Deleting model 'Fotografia'
        db.delete_table('anarapp_fotografia')

        # Deleting model 'ManifestacionesAsociadas'
        db.delete_table('anarapp_manifestacionesasociadas')

        # Deleting model 'Yacimiento'
        db.delete_table('anarapp_yacimiento')

        # Removing M2M table for field usoDelSuelo on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_usoDelSuelo')

        # Removing M2M table for field tenenciaDeLatierra on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_tenenciaDeLatierra')

        # Removing M2M table for field fotografia on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_fotografia')

        # Removing M2M table for field tipoSitio on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_tipoSitio')

        # Removing M2M table for field ubicacionYacimiento on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_ubicacionYacimiento')

        # Removing M2M table for field orientacionYacimiento on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_orientacionYacimiento')

        # Removing M2M table for field texturaSuelo on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_texturaSuelo')

        # Removing M2M table for field hidrologia on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_hidrologia')

        # Removing M2M table for field materiales on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_materiales')

        # Removing M2M table for field estadoConservacion on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_estadoConservacion')

        # Removing M2M table for field destruccionPotencialSitio on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_destruccionPotencialSitio')

        # Removing M2M table for field manifestacionesAsociadas on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_manifestacionesAsociadas')

        # Removing M2M table for field materialesApoyo on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_materialesApoyo')

        # Removing M2M table for field mecanismosObtencionInformacion on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_mecanismosObtencionInformacion')

        # Deleting model 'CronologiaTentativa'
        db.delete_table('anarapp_cronologiatentativa')

        # Deleting model 'GradoDestruccionSitio'
        db.delete_table('anarapp_gradodestruccionsitio')

        # Deleting model 'ModificacionYacimiento'
        db.delete_table('anarapp_modificacionyacimiento')

        # Deleting model 'LocalidadYacimiento'
        db.delete_table('anarapp_localidadyacimiento')

        # Deleting model 'LocalidadYacimientoPoblado'
        db.delete_table('anarapp_localidadyacimientopoblado')

        # Deleting model 'LocYacNoPoblado'
        db.delete_table('anarapp_locyacnopoblado')

        # Deleting model 'TipoManifestacion'
        db.delete_table('anarapp_tipomanifestacion')

        # Deleting model 'Geoglifo'
        db.delete_table('anarapp_geoglifo')

        # Deleting model 'TipoLinea'
        db.delete_table('anarapp_tipolinea')

        # Deleting model 'LineaSencilla'
        db.delete_table('anarapp_lineasencilla')

        # Deleting model 'LineaCompuesta'
        db.delete_table('anarapp_lineacompuesta')

        # Deleting model 'TecnicaPinturaRupestre'
        db.delete_table('anarapp_tecnicapinturarupestre')

        # Deleting model 'Color'
        db.delete_table('anarapp_color')

        # Deleting model 'ImpresionDeManos'
        db.delete_table('anarapp_impresiondemanos')

        # Deleting model 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura')

        # Removing M2M table for field tecnicas on 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura_tecnicas')

        # Removing M2M table for field impresionDeManos on 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura_impresionDeManos')

        # Removing M2M table for field colores on 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura_colores')

        # Removing M2M table for field tipoDeLineas on 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura_tipoDeLineas')

        # Deleting model 'Positivo'
        db.delete_table('anarapp_positivo')

        # Deleting model 'Negativo'
        db.delete_table('anarapp_negativo')

        # Deleting model 'PinturaRupestre'
        db.delete_table('anarapp_pinturarupestre')

        # Removing M2M table for field caracteristicas on 'PinturaRupestre'
        db.delete_table('anarapp_pinturarupestre_caracteristicas')

        # Deleting model 'TecnicaPetroglifo'
        db.delete_table('anarapp_tecnicapetroglifo')

        # Deleting model 'CaracDePetroglifo'
        db.delete_table('anarapp_caracdepetroglifo')

        # Deleting model 'Petroglifo'
        db.delete_table('anarapp_petroglifo')

        # Removing M2M table for field tecnicas on 'Petroglifo'
        db.delete_table('anarapp_petroglifo_tecnicas')

        # Removing M2M table for field caracteristicasPetroglifo on 'Petroglifo'
        db.delete_table('anarapp_petroglifo_caracteristicasPetroglifo')

        # Deleting model 'MicroPetroglifo'
        db.delete_table('anarapp_micropetroglifo')

        # Deleting model 'PiedriaMiticaNatural'
        db.delete_table('anarapp_piedriamiticanatural')

        # Deleting model 'CerroMiticoNatural'
        db.delete_table('anarapp_cerromiticonatural')

        # Deleting model 'MonumentoMegalitico'
        db.delete_table('anarapp_monumentomegalitico')

        # Deleting model 'Monolito'
        db.delete_table('anarapp_monolito')

        # Deleting model 'Menhir'
        db.delete_table('anarapp_menhir')

        # Deleting model 'Dolmen'
        db.delete_table('anarapp_dolmen')

        # Deleting model 'Amolador'
        db.delete_table('anarapp_amolador')

        # Deleting model 'Batea'
        db.delete_table('anarapp_batea')

        # Deleting model 'PuntosAcoplados'
        db.delete_table('anarapp_puntosacoplados')

        # Deleting model 'Cupulas'
        db.delete_table('anarapp_cupulas')

        # Deleting model 'Mortero'
        db.delete_table('anarapp_mortero')

        # Deleting model 'Piedra'
        db.delete_table('anarapp_piedra')

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

        # Deleting model 'ComunicacionPersonalPiedra'
        db.delete_table('anarapp_comunicacionpersonalpiedra')

        # Deleting model 'VerificadoEnPiedra'
        db.delete_table('anarapp_verificadoenpiedra')


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
        'anarapp.comunicacionpersonalpiedra': {
            'Meta': {'object_name': 'ComunicacionPersonalPiedra', '_ormbases': ['anarapp.MecObtInformacion']},
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
        'anarapp.dolmen': {
            'Meta': {'object_name': 'Dolmen', '_ormbases': ['anarapp.MonumentoMegalitico']},
            'cantidadConPetroglifos': ('django.db.models.fields.IntegerField', [], {}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {}),
            'monumentomegalitico_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MonumentoMegalitico']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.estadoconservacion': {
            'Meta': {'object_name': 'EstadoConservacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoSitio': ('django.db.models.fields.IntegerField', [], {})
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
            'altoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'autorFicha': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fechaEscrituraFicha': ('django.db.models.fields.DateField', [], {}),
            'fechaSupervisionFicha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
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