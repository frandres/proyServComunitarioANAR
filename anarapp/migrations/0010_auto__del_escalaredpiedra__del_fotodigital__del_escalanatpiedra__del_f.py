# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EscalaRedPiedra'
        db.delete_table('anarapp_escalaredpiedra')

        # Deleting model 'FotoDigital'
        db.delete_table('anarapp_fotodigital')

        # Deleting model 'EscalaNatPiedra'
        db.delete_table('anarapp_escalanatpiedra')

        # Deleting model 'Fotografia'
        db.delete_table('anarapp_fotografia')

        # Deleting model 'ReproGraf'
        db.delete_table('anarapp_reprograf')

        # Deleting model 'MatApoyoPiedra'
        db.delete_table('anarapp_matapoyopiedra')

        # Deleting model 'ImagenReproGraf'
        db.delete_table('anarapp_imagenreprograf')

        # Deleting model 'RecursoMultimedia'
        db.delete_table('anarapp_recursomultimedia')

        # Adding model 'MultimediaPiedra'
        db.create_table('anarapp_multimediapiedra', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['MultimediaPiedra'])

        # Adding model 'Multimedia'
        db.create_table('anarapp_multimedia', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Multimedia'])

        # Adding model 'EscRedPiedra'
        db.create_table('anarapp_escredpiedra', (
            ('repgrafpiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.RepGrafPiedra'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EscRedPiedra'])

        # Adding model 'FotoBibliografia'
        db.create_table('anarapp_fotobibliografia', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('esFotografia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('escolor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBlancoYNegro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDiapositiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPapel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDigital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esNegativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipoMapa', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['FotoBibliografia'])

        # Adding model 'Bibliografia'
        db.create_table('anarapp_bibliografia', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('conDibujo', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('anarapp', ['Bibliografia'])

        # Adding model 'Foto'
        db.create_table('anarapp_foto', (
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
        db.send_create_signal('anarapp', ['Foto'])

        # Adding model 'EscNatPiedra'
        db.create_table('anarapp_escnatpiedra', (
            ('repgrafpiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.RepGrafPiedra'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EscNatPiedra'])

        # Adding model 'PaginaWebPiedra'
        db.create_table('anarapp_paginawebpiedra', (
            ('paginaweb_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.PaginaWeb'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['PaginaWebPiedra'])

        # Adding model 'MatAVPiedra'
        db.create_table('anarapp_matavpiedra', (
            ('mataudiovisual_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatAudioVisual'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['MatAVPiedra'])

        # Adding model 'RepGrafPiedra'
        db.create_table('anarapp_repgrafpiedra', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('numPiezas', self.gf('django.db.models.fields.IntegerField')()),
            ('instituto', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('persona', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['RepGrafPiedra'])

        # Adding model 'FotoPiedra'
        db.create_table('anarapp_fotopiedra', (
            ('foto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Foto'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['FotoPiedra'])

        # Removing M2M table for field fotografia on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_fotografia')

        # Removing M2M table for field materialesApoyo on 'Yacimiento'
        db.delete_table('anarapp_yacimiento_materialesApoyo')

        # Deleting field 'Grabacion.videos'
        db.delete_column('anarapp_grabacion', 'videos')

        # Deleting field 'MatAudioVisual.matapoyopiedra_ptr'
        db.delete_column('anarapp_mataudiovisual', 'matapoyopiedra_ptr_id')

        # Adding field 'MatAudioVisual.materialapoyo_ptr'
        db.add_column('anarapp_mataudiovisual', 'materialapoyo_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'VideoPiedra.grabacion_ptr'
        db.delete_column('anarapp_videopiedra', 'grabacion_ptr_id')

        # Adding field 'VideoPiedra.video_ptr'
        db.add_column('anarapp_videopiedra', 'video_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.Video'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'PeliculaPiedra.grabacion_ptr'
        db.delete_column('anarapp_peliculapiedra', 'grabacion_ptr_id')

        # Adding field 'PeliculaPiedra.pelicula_ptr'
        db.add_column('anarapp_peliculapiedra', 'pelicula_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.Pelicula'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'FotoBibPiedra.esDigital'
        db.delete_column('anarapp_fotobibpiedra', 'esDigital')

        # Deleting field 'FotoBibPiedra.esDiapositiva'
        db.delete_column('anarapp_fotobibpiedra', 'esDiapositiva')

        # Deleting field 'FotoBibPiedra.esFotografia'
        db.delete_column('anarapp_fotobibpiedra', 'esFotografia')

        # Deleting field 'FotoBibPiedra.descripcion'
        db.delete_column('anarapp_fotobibpiedra', 'descripcion')

        # Deleting field 'FotoBibPiedra.tipoMapa'
        db.delete_column('anarapp_fotobibpiedra', 'tipoMapa')

        # Deleting field 'FotoBibPiedra.esBlancoYNegro'
        db.delete_column('anarapp_fotobibpiedra', 'esBlancoYNegro')

        # Deleting field 'FotoBibPiedra.escolor'
        db.delete_column('anarapp_fotobibpiedra', 'escolor')

        # Deleting field 'FotoBibPiedra.matapoyopiedra_ptr'
        db.delete_column('anarapp_fotobibpiedra', 'matapoyopiedra_ptr_id')

        # Deleting field 'FotoBibPiedra.esPapel'
        db.delete_column('anarapp_fotobibpiedra', 'esPapel')

        # Deleting field 'FotoBibPiedra.esNegativo'
        db.delete_column('anarapp_fotobibpiedra', 'esNegativo')

        # Adding field 'FotoBibPiedra.fotobibliografia_ptr'
        db.add_column('anarapp_fotobibpiedra', 'fotobibliografia_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.FotoBibliografia'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.piedra'
        db.add_column('anarapp_fotobibpiedra', 'piedra',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['anarapp.Piedra']),
                      keep_default=False)

        # Deleting field 'PaginaWEB.piedra'
        db.delete_column('anarapp_paginaweb', 'piedra_id')

        # Deleting field 'BibPiedra.autor'
        db.delete_column('anarapp_bibpiedra', 'autor')

        # Deleting field 'BibPiedra.institucion'
        db.delete_column('anarapp_bibpiedra', 'institucion')

        # Deleting field 'BibPiedra.conDibujo'
        db.delete_column('anarapp_bibpiedra', 'conDibujo')

        # Deleting field 'BibPiedra.matapoyopiedra_ptr'
        db.delete_column('anarapp_bibpiedra', 'matapoyopiedra_ptr_id')

        # Deleting field 'BibPiedra.codigo'
        db.delete_column('anarapp_bibpiedra', 'codigo')

        # Deleting field 'BibPiedra.titulo'
        db.delete_column('anarapp_bibpiedra', 'titulo')

        # Deleting field 'BibPiedra.ano'
        db.delete_column('anarapp_bibpiedra', 'ano')

        # Adding field 'BibPiedra.bibliografia_ptr'
        db.add_column('anarapp_bibpiedra', 'bibliografia_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.Bibliografia'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'BibPiedra.piedra'
        db.add_column('anarapp_bibpiedra', 'piedra',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['anarapp.Piedra']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'EscalaRedPiedra'
        db.create_table('anarapp_escalaredpiedra', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EscalaRedPiedra'])

        # Adding model 'FotoDigital'
        db.create_table('anarapp_fotodigital', (
            ('matapoyopiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatApoyoPiedra'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['FotoDigital'])

        # Adding model 'EscalaNatPiedra'
        db.create_table('anarapp_escalanatpiedra', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EscalaNatPiedra'])

        # Adding model 'Fotografia'
        db.create_table('anarapp_fotografia', (
            ('tipoFotografia', self.gf('django.db.models.fields.IntegerField')()),
            ('numMarcaNegativo', self.gf('django.db.models.fields.IntegerField')()),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fotografia', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('fotografo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numCopiaAnar', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('esDeAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numRollo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Fotografia'])

        # Adding model 'ReproGraf'
        db.create_table('anarapp_reprograf', (
            ('matapoyopiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatApoyoPiedra'], unique=True, primary_key=True)),
            ('numPiezas', self.gf('django.db.models.fields.IntegerField')()),
            ('instituto', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('persona', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['ReproGraf'])

        # Adding model 'MatApoyoPiedra'
        db.create_table('anarapp_matapoyopiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['MatApoyoPiedra'])

        # Adding model 'ImagenReproGraf'
        db.create_table('anarapp_imagenreprograf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reproduccionGrafica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.ReproGraf'])),
        ))
        db.send_create_signal('anarapp', ['ImagenReproGraf'])

        # Adding model 'RecursoMultimedia'
        db.create_table('anarapp_recursomultimedia', (
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['RecursoMultimedia'])

        # Deleting model 'MultimediaPiedra'
        db.delete_table('anarapp_multimediapiedra')

        # Deleting model 'Multimedia'
        db.delete_table('anarapp_multimedia')

        # Deleting model 'EscRedPiedra'
        db.delete_table('anarapp_escredpiedra')

        # Deleting model 'FotoBibliografia'
        db.delete_table('anarapp_fotobibliografia')

        # Deleting model 'Bibliografia'
        db.delete_table('anarapp_bibliografia')

        # Deleting model 'Foto'
        db.delete_table('anarapp_foto')

        # Deleting model 'EscNatPiedra'
        db.delete_table('anarapp_escnatpiedra')

        # Deleting model 'PaginaWebPiedra'
        db.delete_table('anarapp_paginawebpiedra')

        # Deleting model 'MatAVPiedra'
        db.delete_table('anarapp_matavpiedra')

        # Deleting model 'RepGrafPiedra'
        db.delete_table('anarapp_repgrafpiedra')

        # Deleting model 'FotoPiedra'
        db.delete_table('anarapp_fotopiedra')

        # Adding M2M table for field fotografia on 'Yacimiento'
        db.create_table('anarapp_yacimiento_fotografia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('fotografia', models.ForeignKey(orm['anarapp.fotografia'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_fotografia', ['yacimiento_id', 'fotografia_id'])

        # Adding M2M table for field materialesApoyo on 'Yacimiento'
        db.create_table('anarapp_yacimiento_materialesApoyo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yacimiento', models.ForeignKey(orm['anarapp.yacimiento'], null=False)),
            ('materialapoyo', models.ForeignKey(orm['anarapp.materialapoyo'], null=False))
        ))
        db.create_unique('anarapp_yacimiento_materialesApoyo', ['yacimiento_id', 'materialapoyo_id'])

        # Adding field 'Grabacion.videos'
        db.add_column('anarapp_grabacion', 'videos',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=40),
                      keep_default=False)

        # Adding field 'MatAudioVisual.matapoyopiedra_ptr'
        db.add_column('anarapp_mataudiovisual', 'matapoyopiedra_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.MatApoyoPiedra'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'MatAudioVisual.materialapoyo_ptr'
        db.delete_column('anarapp_mataudiovisual', 'materialapoyo_ptr_id')

        # Adding field 'VideoPiedra.grabacion_ptr'
        db.add_column('anarapp_videopiedra', 'grabacion_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.Grabacion'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'VideoPiedra.video_ptr'
        db.delete_column('anarapp_videopiedra', 'video_ptr_id')

        # Adding field 'PeliculaPiedra.grabacion_ptr'
        db.add_column('anarapp_peliculapiedra', 'grabacion_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.Grabacion'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'PeliculaPiedra.pelicula_ptr'
        db.delete_column('anarapp_peliculapiedra', 'pelicula_ptr_id')

        # Adding field 'FotoBibPiedra.esDigital'
        db.add_column('anarapp_fotobibpiedra', 'esDigital',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.esDiapositiva'
        db.add_column('anarapp_fotobibpiedra', 'esDiapositiva',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.esFotografia'
        db.add_column('anarapp_fotobibpiedra', 'esFotografia',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.descripcion'
        db.add_column('anarapp_fotobibpiedra', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.tipoMapa'
        db.add_column('anarapp_fotobibpiedra', 'tipoMapa',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.esBlancoYNegro'
        db.add_column('anarapp_fotobibpiedra', 'esBlancoYNegro',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.escolor'
        db.add_column('anarapp_fotobibpiedra', 'escolor',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.matapoyopiedra_ptr'
        db.add_column('anarapp_fotobibpiedra', 'matapoyopiedra_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.MatApoyoPiedra'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.esPapel'
        db.add_column('anarapp_fotobibpiedra', 'esPapel',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FotoBibPiedra.esNegativo'
        db.add_column('anarapp_fotobibpiedra', 'esNegativo',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'FotoBibPiedra.fotobibliografia_ptr'
        db.delete_column('anarapp_fotobibpiedra', 'fotobibliografia_ptr_id')

        # Deleting field 'FotoBibPiedra.piedra'
        db.delete_column('anarapp_fotobibpiedra', 'piedra_id')

        # Adding field 'PaginaWEB.piedra'
        db.add_column('anarapp_paginaweb', 'piedra',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['anarapp.Piedra']),
                      keep_default=False)

        # Adding field 'BibPiedra.autor'
        db.add_column('anarapp_bibpiedra', 'autor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BibPiedra.institucion'
        db.add_column('anarapp_bibpiedra', 'institucion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BibPiedra.conDibujo'
        db.add_column('anarapp_bibpiedra', 'conDibujo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BibPiedra.matapoyopiedra_ptr'
        db.add_column('anarapp_bibpiedra', 'matapoyopiedra_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['anarapp.MatApoyoPiedra'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'BibPiedra.codigo'
        db.add_column('anarapp_bibpiedra', 'codigo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BibPiedra.titulo'
        db.add_column('anarapp_bibpiedra', 'titulo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BibPiedra.ano'
        db.add_column('anarapp_bibpiedra', 'ano',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'BibPiedra.bibliografia_ptr'
        db.delete_column('anarapp_bibpiedra', 'bibliografia_ptr_id')

        # Deleting field 'BibPiedra.piedra'
        db.delete_column('anarapp_bibpiedra', 'piedra_id')


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
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'conDibujo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'anarapp.bibpiedra': {
            'Meta': {'object_name': 'BibPiedra', '_ormbases': ['anarapp.Bibliografia']},
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
        'anarapp.escnatpiedra': {
            'Meta': {'object_name': 'EscNatPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.escredpiedra': {
            'Meta': {'object_name': 'EscRedPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.esquemaporcara': {
            'Meta': {'object_name': 'EsquemaPorCara'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
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
        'anarapp.figurasportipo': {
            'Meta': {'object_name': 'FigurasPorTipo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.foto': {
            'Meta': {'object_name': 'Foto', '_ormbases': ['anarapp.MaterialApoyo']},
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
        'anarapp.fotobibliografia': {
            'Meta': {'object_name': 'FotoBibliografia', '_ormbases': ['anarapp.MaterialApoyo']},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'esBlancoYNegro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDiapositiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDigital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esFotografia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPapel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escolor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoMapa': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotobibpiedra': {
            'Meta': {'object_name': 'FotoBibPiedra', '_ormbases': ['anarapp.FotoBibliografia']},
            'fotobibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.FotoBibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.fotopiedra': {
            'Meta': {'object_name': 'FotoPiedra', '_ormbases': ['anarapp.Foto']},
            'foto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Foto']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
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
        'anarapp.impresiondemanos': {
            'Meta': {'object_name': 'ImpresionDeManos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.infofoto': {
            'Meta': {'object_name': 'InfoFoto'},
            'esDeAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fotografo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'negativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numCopiaAnar': ('django.db.models.fields.IntegerField', [], {}),
            'numFoto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numMarcaNegativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numReferencia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numRollo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
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
        'anarapp.manifestaciones': {
            'Meta': {'object_name': 'Manifestaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'tieneAmoladores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.manifestacionesasociadas': {
            'Meta': {'object_name': 'ManifestacionesAsociadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifestacionAsociada': ('django.db.models.fields.IntegerField', [], {}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.mataudiovisual': {
            'Meta': {'object_name': 'MatAudioVisual', '_ormbases': ['anarapp.MaterialApoyo']},
            'formato': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.matavpiedra': {
            'Meta': {'object_name': 'MatAVPiedra', '_ormbases': ['anarapp.MatAudioVisual']},
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
        'anarapp.multimedia': {
            'Meta': {'object_name': 'Multimedia', '_ormbases': ['anarapp.MaterialApoyo']},
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.multimediapiedra': {
            'Meta': {'object_name': 'MultimediaPiedra', '_ormbases': ['anarapp.MaterialApoyo']},
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
            'Meta': {'object_name': 'PaginaWeb', '_ormbases': ['anarapp.MaterialApoyo']},
            'direccionURL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.paginawebpiedra': {
            'Meta': {'object_name': 'PaginaWebPiedra', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.pelicula': {
            'Meta': {'object_name': 'Pelicula', '_ormbases': ['anarapp.Grabacion']},
            'grabacion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Grabacion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.peliculapiedra': {
            'Meta': {'object_name': 'PeliculaPiedra', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
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
        'anarapp.repgrafpiedra': {
            'Meta': {'object_name': 'RepGrafPiedra', '_ormbases': ['anarapp.MaterialApoyo']},
            'instituto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'materialapoyo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MaterialApoyo']", 'unique': 'True', 'primary_key': 'True'}),
            'numPiezas': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
        'anarapp.tratfoto': {
            'Meta': {'object_name': 'TratFoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limpiezaCon': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'otrosTratamientos': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'programaVersion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'rellenoSurcos': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tratamientoDigital': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.ubicacioncaras': {
            'Meta': {'object_name': 'UbicacionCaras'},
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
            'Meta': {'object_name': 'VideoPiedra', '_ormbases': ['anarapp.Video']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.yacimiento': {
            'Meta': {'object_name': 'Yacimiento'},
            'altura': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'datum': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'destruccionPotencialSitio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.DestPotencialSitio']", 'symmetrical': 'False', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'estadoConservacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.EstadoConservacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'fauna': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'flora': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'hidrologia': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.Hidrologia']", 'symmetrical': 'False', 'blank': 'True'}),
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
            'manifestacionesAsociadas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.ManifestacionesAsociadas']", 'symmetrical': 'False', 'blank': 'True'}),
            'materiales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.Material']", 'symmetrical': 'False', 'blank': 'True'}),
            'mecanismosObtencionInformacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.MecObtInformacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numPiedrasYacimientoColocadas': ('django.db.models.fields.IntegerField', [], {}),
            'numPiedrasYacimientoGrabadas': ('django.db.models.fields.IntegerField', [], {}),
            'numPiedrasYacimientoOriginal': ('django.db.models.fields.IntegerField', [], {}),
            'numPiedrasYacimientoPintadas': ('django.db.models.fields.IntegerField', [], {}),
            'numeroPlano': ('django.db.models.fields.IntegerField', [], {}),
            'observacionesDestruccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'observacionesExposicion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'orientacionYacimiento': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.OrientacionYacimiento']", 'symmetrical': 'False', 'blank': 'True'}),
            'otrasNotas': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'otrosConstitucionYacimiento': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'otrosValoresSitio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'superficie': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'tenenciaDeLatierra': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TenenciaDeLaTierra']", 'symmetrical': 'False', 'blank': 'True'}),
            'texturaSuelo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TexturaSuelo']", 'symmetrical': 'False', 'blank': 'True'}),
            'tiempoDestruccion': ('django.db.models.fields.IntegerField', [], {}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {}),
            'tipoExposicion': ('django.db.models.fields.IntegerField', [], {}),
            'tipoSitio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.TipoYacimiento']", 'symmetrical': 'False', 'blank': 'True'}),
            'ubicacionYacimiento': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.UbicacionYacimiento']", 'symmetrical': 'False', 'blank': 'True'}),
            'usoDelSuelo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anarapp.UsoActualDelSuelo']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['anarapp']