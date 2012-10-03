# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FailedAccessAttempt'
        db.create_table('cerberos_failedaccessattempt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('failed_logins', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('get_data', self.gf('django.db.models.fields.TextField')()),
            ('post_data', self.gf('django.db.models.fields.TextField')()),
            ('http_accept', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path_info', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('cerberos', ['FailedAccessAttempt'])


    def backwards(self, orm):
        # Deleting model 'FailedAccessAttempt'
        db.delete_table('cerberos_failedaccessattempt')


    models = {
        'cerberos.failedaccessattempt': {
            'Meta': {'object_name': 'FailedAccessAttempt'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'failed_logins': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'get_data': ('django.db.models.fields.TextField', [], {}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_data': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cerberos']