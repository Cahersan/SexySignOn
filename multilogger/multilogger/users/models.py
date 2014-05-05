# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager, AbstractUser)
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

#from djorm_expressions.models import ExpressionManager    
from djorm_pguuid.fields import UUIDField 

#class AbstractUser(AbstractBaseUser, PermissionsMixin):
#    """
#    An abstract base class implementing a fully featured User model with
#    admin-compliant permissions.
#
#    Password and email are required. Other fields are optional.
#    """
#    email = models.EmailField(_('email address'), blank=True)
#    is_staff = models.BooleanField(_('staff status'), default=False,
#        help_text=_('Designates whether the user can log into this admin '
#                    'site.'))
#    is_active = models.BooleanField(_('active'), default=True,
#        help_text=_('Designates whether this user should be treated as '
#                    'active. Unselect this instead of deleting accounts.'))
#    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#
#    objects = UserManager()
#
#    USERNAME_FIELD = 'username' #Must stay here because of validation
#    REQUIRED_FIELDS = ['email']
#
#    class Meta:
#        verbose_name = _('user')
#        verbose_name_plural = _('users')
#        abstract = True
#
#    def email_user(self, subject, message, from_email=None, **kwargs):
#        """
#        Sends an email to this User.
#        """
#        send_mail(subject, message, from_email, [self.email], **kwargs)

class AbstractBaseModel(models.Model):
    uuid = UUIDField(auto_add=True, db_index=True)
    #objects = ExpressionManager()

    class Meta:
        abstract = True
        
@python_2_unicode_compatible
class App(AbstractBaseModel):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

@python_2_unicode_compatible
class Site(AbstractBaseModel):
    name = models.CharField(max_length=100)
    apps = models.ManyToManyField(App)
    allow_user_registration = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class User(AbstractBaseModel, AbstractUser):
    
    site = models.ForeignKey(Site)

    def __str__(self):
        return self.username

@python_2_unicode_compatible
class Url(AbstractBaseModel):
    url = models.URLField()
    site = models.ForeignKey(Site, blank=True)

    def __str__(self):
        return self.url


