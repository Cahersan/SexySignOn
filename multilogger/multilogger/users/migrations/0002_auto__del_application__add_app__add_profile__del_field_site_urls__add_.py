# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Application'
        db.delete_table('users_application')

        # Removing M2M table for field users on 'Application'
        db.delete_table(db.shorten_name('users_application_users'))

        # Adding model 'Profile'
        db.create_table('users_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('djorm_pguuid.fields.UUIDField')(db_index=True, auto_add=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Site'])),
        ))
        db.send_create_signal('users', ['Profile'])

        # Adding M2M table for field apps on 'Profile'
        m2m_table_name = db.shorten_name('users_profile_apps')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['users.profile'], null=False)),
            ('app', models.ForeignKey(orm['users.app'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'app_id'])

        # Adding model 'App'
        db.create_table('users_app', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('djorm_pguuid.fields.UUIDField')(db_index=True, auto_add=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('users', ['App'])

        # Adding field 'Url.uuid'
        db.add_column('users_url', 'uuid',
                      self.gf('djorm_pguuid.fields.UUIDField')(default='89b1283d-c32e-4b8a-a9e3-a699445fdd4d', db_index=True, auto_add=True),
                      keep_default=False)

        # Adding field 'Url.site'
        db.add_column('users_url', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1231, to=orm['users.Site'], blank=True),
                      keep_default=False)

        # Deleting field 'Site.urls'
        db.delete_column('users_site', 'urls_id')

        # Adding field 'Site.uuid'
        db.add_column('users_site', 'uuid',
                      self.gf('djorm_pguuid.fields.UUIDField')(default='89b1283d-c32e-4b8a-a9e3-a699445fdd4d', db_index=True, auto_add=True),
                      keep_default=False)

        # Adding M2M table for field apps on 'Site'
        m2m_table_name = db.shorten_name('users_site_apps')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('site', models.ForeignKey(orm['users.site'], null=False)),
            ('app', models.ForeignKey(orm['users.app'], null=False))
        ))
        db.create_unique(m2m_table_name, ['site_id', 'app_id'])


    def backwards(self, orm):
        # Adding model 'Application'
        db.create_table('users_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('users', ['Application'])

        # Adding M2M table for field users on 'Application'
        m2m_table_name = db.shorten_name('users_application_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['users.application'], null=False)),
            ('user', models.ForeignKey(orm['users.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'user_id'])

        # Deleting model 'Profile'
        db.delete_table('users_profile')

        # Removing M2M table for field apps on 'Profile'
        db.delete_table(db.shorten_name('users_profile_apps'))

        # Deleting model 'App'
        db.delete_table('users_app')

        # Deleting field 'Url.uuid'
        db.delete_column('users_url', 'uuid')

        # Deleting field 'Url.site'
        db.delete_column('users_url', 'site_id')


        # User chose to not deal with backwards NULL issues for 'Site.urls'
        raise RuntimeError("Cannot reverse this migration. 'Site.urls' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Site.urls'
        db.add_column('users_site', 'urls',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Url']),
                      keep_default=False)

        # Deleting field 'Site.uuid'
        db.delete_column('users_site', 'uuid')

        # Removing M2M table for field apps on 'Site'
        db.delete_table(db.shorten_name('users_site_apps'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'users.app': {
            'Meta': {'object_name': 'App'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uuid': ('djorm_pguuid.fields.UUIDField', [], {'db_index': 'True', 'auto_add': 'True'})
        },
        'users.profile': {
            'Meta': {'object_name': 'Profile'},
            'apps': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['users.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"}),
            'uuid': ('djorm_pguuid.fields.UUIDField', [], {'db_index': 'True', 'auto_add': 'True'})
        },
        'users.site': {
            'Meta': {'object_name': 'Site'},
            'apps': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['users.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uuid': ('djorm_pguuid.fields.UUIDField', [], {'db_index': 'True', 'auto_add': 'True'})
        },
        'users.url': {
            'Meta': {'object_name': 'Url'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Site']", 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'uuid': ('djorm_pguuid.fields.UUIDField', [], {'db_index': 'True', 'auto_add': 'True'})
        },
        'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'uuid': ('djorm_pguuid.fields.UUIDField', [], {'db_index': 'True', 'auto_add': 'True'})
        }
    }

    complete_apps = ['users']