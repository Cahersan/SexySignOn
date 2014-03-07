# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.utils.encoding import python_2_unicode_compatible

#from djorm_expressions.models import ExpressionManager    
from djorm_pguuid.fields import UUIDField 

#@python_2_unicode_compatible
class User(AbstractUser):
    
    uuid = UUIDField(auto_add=True, db_index=True)
    #objects = ExpressionManager()

    def __unicode__(self):
        return self.username

class Application(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

class Url(models.Model):
    url = models.URLField()
    
class Site(models.Model):
    urls = models.ForeignKey(Url)
 
    def __unicode__(self):
        return self.name

