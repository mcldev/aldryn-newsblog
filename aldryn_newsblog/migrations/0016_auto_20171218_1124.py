# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0015_auto_20161208_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured image', blank=True, to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='namespace',
            field=models.CharField(default=None, unique=True, max_length=100, verbose_name='Instance namespace'),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
    ]
