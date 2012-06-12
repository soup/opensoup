# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.reposted_via'
        db.add_column('tumblelog_post', 'reposted_via',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='post_reposted_via', null=True, to=orm['tumblelog.Post']),
                      keep_default=False)

        # Adding field 'Post.origin'
        db.add_column('tumblelog_post', 'origin',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='post_origin', null=True, to=orm['tumblelog.Post']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.reposted_via'
        db.delete_column('tumblelog_post', 'reposted_via_id')

        # Deleting field 'Post.origin'
        db.delete_column('tumblelog_post', 'origin_id')


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
        'tumblelog.asset': {
            'Meta': {'object_name': 'Asset'},
            'directory': ('django.db.models.fields.IntegerField', [], {}),
            'diskfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'random_part': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        'tumblelog.blog': {
            'Meta': {'object_name': 'Blog'},
            'avatar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tumblelog.Asset']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'tumblelog.imagepost': {
            'Meta': {'object_name': 'ImagePost', '_ormbases': ['tumblelog.Post']},
            'asset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tumblelog.Asset']"}),
            'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tumblelog.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        'tumblelog.post': {
            'Meta': {'object_name': 'Post'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tumblelog.Blog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'post_origin'", 'null': 'True', 'to': "orm['tumblelog.Post']"}),
            'reposted_via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'post_reposted_via'", 'null': 'True', 'to': "orm['tumblelog.Post']"}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['tumblelog']