# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'FailedAccessAttempt', fields ['username']
        db.create_index('cerberos_failedaccessattempt', ['username'])

        # Adding index on 'FailedAccessAttempt', fields ['ip_address']
        db.create_index('cerberos_failedaccessattempt', ['ip_address'])


    def backwards(self, orm):
        # Removing index on 'FailedAccessAttempt', fields ['ip_address']
        db.delete_index('cerberos_failedaccessattempt', ['ip_address'])

        # Removing index on 'FailedAccessAttempt', fields ['username']
        db.delete_index('cerberos_failedaccessattempt', ['username'])


    models = {
        'cerberos.failedaccessattempt': {
            'Meta': {'object_name': 'FailedAccessAttempt'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'failed_logins': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'get_data': ('django.db.models.fields.TextField', [], {}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_data': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cerberos']