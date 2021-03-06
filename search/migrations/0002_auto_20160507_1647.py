# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='current_version',
            field=models.CharField(default='none', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='installs',
            field=models.CharField(default='none', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='reqs_android',
            field=models.CharField(default='none', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='size',
            field=models.CharField(default='none', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='updated',
            field=models.CharField(default='none', max_length=128),
            preserve_default=False,
        ),
    ]
