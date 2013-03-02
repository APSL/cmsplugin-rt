# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OpenGraphPluginModel'
        db.create_table('cmsplugin_opengraphpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('og_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('og_type', self.gf('django.db.models.fields.CharField')(default='website', max_length=60)),
            ('og_url', self.gf('django.db.models.fields.CharField')(default='http://', max_length=255)),
            ('og_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('fb_app_id', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('og_site_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('og_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('open_graph', ['OpenGraphPluginModel'])


    def backwards(self, orm):
        # Deleting model 'OpenGraphPluginModel'
        db.delete_table('cmsplugin_opengraphpluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'open-graph.opengraphpluginmodel': {
            'Meta': {'object_name': 'OpenGraphPluginModel', 'db_table': "'cmsplugin_opengraphpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'fb_app_id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'og_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'og_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'og_site_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'og_type': ('django.db.models.fields.CharField', [], {'default': "'website'", 'max_length': '60'}),
            'og_url': ('django.db.models.fields.CharField', [], {'default': "'http://'", 'max_length': '255'})
        }
    }

    complete_apps = ['open_graph']
