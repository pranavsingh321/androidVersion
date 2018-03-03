# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Application(models.Model):
    application = models.CharField(null=True,max_length=200)
    package_name = models.CharField(null=True,max_length=50)
    package_version_code = models.CharField(null=True,max_length=50)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "{}".format(self.package_name)