from __future__ import unicode_literals

from django.db import models

class App(models.Model):
    title = models.CharField(max_length=128)
    appid = models.CharField(max_length=128, unique=True)
    rating_info = models.CharField(max_length=128)
    devname = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    installs = models.CharField(max_length=128)
    current_version = models.CharField(max_length=128)
    reqs_android = models.CharField(max_length=128)
    updated = models.CharField(max_length=128)
    src = models.URLField(max_length=1000, default="none")

    def __str__(self):
        return self.title