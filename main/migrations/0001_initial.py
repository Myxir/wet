# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Vet'
        db.create_table('main_vet', (
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('www', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 21, 48, 43, 429516))),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=45)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('clinic_adress', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('clinic_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('main', ['Vet'])

        # Adding model 'Client'
        db.create_table('main_client', (
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('vet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Vet'])),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 21, 48, 43, 430147))),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=45, blank=True)),
        ))
        db.send_create_signal('main', ['Client'])

        # Adding model 'Animal'
        db.create_table('main_animal', (
            ('race', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('date_born', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('photo', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('next_event_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('species', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Client'])),
            ('next_event', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('prognose', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 21, 48, 43, 430780))),
            ('history', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('main', ['Animal'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Vet'
        db.delete_table('main_vet')

        # Deleting model 'Client'
        db.delete_table('main_client')

        # Deleting model 'Animal'
        db.delete_table('main_animal')
    
    
    models = {
        'main.animal': {
            'Meta': {'object_name': 'Animal'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 21, 48, 43, 430780)'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Client']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'date_born': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_event': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'next_event_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'prognose': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'main.client': {
            'Meta': {'object_name': 'Client'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 21, 48, 43, 430147)'}),
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'vet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Vet']"})
        },
        'main.vet': {
            'Meta': {'object_name': 'Vet'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 21, 48, 43, 429516)'}),
            'clinic_adress': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'clinic_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'www': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        }
    }
    
    complete_apps = ['main']
