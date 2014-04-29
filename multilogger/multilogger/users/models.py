# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.utils.encoding import python_2_unicode_compatible

#from djorm_expressions.models import ExpressionManager    
from djorm_pguuid.fields import UUIDField 

class UUIDModel(models.Model):
    uuid = UUIDField(auto_add=True, db_index=True)
    #objects = ExpressionManager()

    class Meta:
        abstract = True

#@python_2_unicode_compatible
class User(UUIDModel, AbstractUser):
    
    def __str__(self):
        return self.username

class App(UUIDModel):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Site(UUIDModel):
    name = models.CharField(max_length=100)
    apps = models.ManyToManyField(App)
 
    def __str__(self):
        return self.name

class Url(UUIDModel):
    url = models.URLField()
    site = models.ForeignKey(Site, blank=True)

    def __str__(self):
        return self.url

class Profile(UUIDModel):
    user = models.ForeignKey(User)
    site = models.ForeignKey(Site)
    apps = models.ManyToManyField(App)

    def __str__(self):
        return 'User ' + self.user.username + ' in site ' + self.site.name

