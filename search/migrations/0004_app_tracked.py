# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_app_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='tracked',
            field=models.BooleanField(default=False),
        ),
    ]