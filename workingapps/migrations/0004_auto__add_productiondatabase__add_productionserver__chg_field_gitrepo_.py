# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductionDatabase'
        db.create_table('workingapps_productiondatabase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('workingapps', ['ProductionDatabase'])

        # Adding model 'ProductionServer'
        db.create_table('workingapps_productionserver', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('workingapps', ['ProductionServer'])


        # Changing field 'GitRepo.url'
        db.alter_column('workingapps_gitrepo', 'url', self.gf('django.db.models.fields.CharField')(max_length=500))
        # Adding field 'Project.production_server'
        db.add_column('workingapps_project', 'production_server',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['workingapps.ProductionServer'], blank=True),
                      keep_default=False)

        # Adding field 'Project.production_database'
        db.add_column('workingapps_project', 'production_database',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['workingapps.ProductionDatabase'], blank=True),
                      keep_default=False)


        # Changing field 'JenkinsServer.url'
        db.alter_column('workingapps_jenkinsserver', 'url', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):
        # Deleting model 'ProductionDatabase'
        db.delete_table('workingapps_productiondatabase')

        # Deleting model 'ProductionServer'
        db.delete_table('workingapps_productionserver')


        # Changing field 'GitRepo.url'
        db.alter_column('workingapps_gitrepo', 'url', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Deleting field 'Project.production_server'
        db.delete_column('workingapps_project', 'production_server_id')

        # Deleting field 'Project.production_database'
        db.delete_column('workingapps_project', 'production_database_id')


        # Changing field 'JenkinsServer.url'
        db.alter_column('workingapps_jenkinsserver', 'url', self.gf('django.db.models.fields.CharField')(max_length=100))

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
        'workingapps.gitrepo': {
            'Meta': {'object_name': 'GitRepo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'workingapps.jenkinsserver': {
            'Meta': {'object_name': 'JenkinsServer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'workingapps.productiondatabase': {
            'Meta': {'object_name': 'ProductionDatabase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'workingapps.productionserver': {
            'Meta': {'object_name': 'ProductionServer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'workingapps.project': {
            'Meta': {'object_name': 'Project'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.Database']"}),
            'framework': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.Framework']"}),
            'git_repo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.GitRepo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenkins_server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.JenkinsServer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'production_database': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.ProductionDatabase']", 'blank': 'True'}),
            'production_server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.ProductionServer']", 'blank': 'True'}),
            'source_control': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workingapps.SourceControl']"})
        },
        'workingapps.sourcecontrol': {
            'Meta': {'object_name': 'SourceControl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['workingapps']