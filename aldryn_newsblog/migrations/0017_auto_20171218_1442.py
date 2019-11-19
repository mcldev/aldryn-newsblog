# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0016_auto_20171218_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogarchiveplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsblogarticlesearchplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsblogauthorsplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsblogcategoriesplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsblogfeaturedarticlesplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsbloglatestarticlesplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsblogtagsplugin',
            name='render_template_choice',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
