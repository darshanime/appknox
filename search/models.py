from __future__ import unicode_literals

from django.db import models

class App(models.Model):
    title = models.CharField(max_length=128)
    appid = models.CharField(max_length=128, unique=True)
    rating_info = models.CharField(max_length=128)
    devname = models.CharField(max_length=128)

# Create your models here.
