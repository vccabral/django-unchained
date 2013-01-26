# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SourceControl'
        db.create_table('workingapps_sourcecontrol', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workingapps', ['SourceControl'])

        # Adding model 'Framework'
        db.create_table('workingapps_framework', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workingapps', ['Framework'])

        # Adding model 'Database'
        db.create_table('workingapps_database', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workingapps', ['Database'])

        # Adding field 'Project.admin'
        db.add_column('workingapps_project', 'admin',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Project.database'
        db.add_column('workingapps_project', 'database',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['workingapps.Database']),
                      keep_default=False)

        # Adding field 'Project.framework'
        db.add_column('workingapps_project', 'framework',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['workingapps.Framework']),
                      keep_default=False)

        # Adding field 'Project.source_control'
        db.add_column('workingapps_project', 'source_control',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['workingapps.SourceControl']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SourceControl'
        db.delete_table('workingapps_sourcecontrol')

        # Deleting model 'Framework'
        db.delete_table('workingapps_framework')

        # Deleting model 'Database'
        db.delete_table('workingapps_database')

        # Deleting field 'Project.admin'
        db.delete_column('workingapps_project', 'admin_id')

        # Deleting field 'Project.database'
        db.delete_column('workingapps_project', 'database_id')

        # Deleting field 'Project.framework'
        db.delete_column('workingapps_project', 'framework_id')

        # Deleting field 'Project.source_control'
        db.delete_column('workingapps_project', 'source_control_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workingapps.database': {
            'Meta': {'object_name': 'Database'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workingapps.framework': {
            'Meta': {'object_name': 'Framework'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workingapps.project': {
            'Meta': {'object_name': 'Project'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.Database']"}),
            'framework': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.Framework']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'source_control': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.SourceControl']"})
        },
        'workingapps.sourcecontrol': {
            'Meta': {'object_name': 'SourceControl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['workingapps']