# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Register'
        db.create_table('register_register', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lang', self.gf('django.db.models.fields.CharField')(default='EN', max_length=2)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formulator.Form'])),
        ))
        db.send_create_signal('register', ['Register'])


    def backwards(self, orm):
        # Deleting model 'Register'
        db.delete_table('register_register')


    models = {
        'formulator.form': {
            'Meta': {'object_name': 'Form'},
            'attrs': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'form_accept_charset': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'form_action': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'form_autocomplete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form_enctype': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'form_id': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"}),
            'form_method': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'}),
            'form_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'form_novalidate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form_target': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'register.register': {
            'Meta': {'object_name': 'Register'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formulator.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'EN'", 'max_length': '2'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['register']