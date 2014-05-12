# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

#from djorm_expressions.models import ExpressionManager    
from djorm_pguuid.fields import UUIDField 

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

class User(AbstractBaseUser, PermissionsMixin, AbstractBaseModel):
    """
    A user based on the django.contrib.auth AbstractUser which suits 
    our needs. It's a full featured User model with admin-compliant 
    permissions.
    """
    email = models.EmailField(_('email address'), blank=False, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    site = models.ForeignKey(Site)

    objects = UserManager()

    USERNAME_FIELD = 'email' #Must stay here because of validation
    REQUIRED_FIELDS = ['uuid']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email
 
    def get_full_name(self):
        "Returns the short name for the user too!"
        return self.get_short_name()
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

@python_2_unicode_compatible
class Url(AbstractBaseModel):
    url = models.URLField()
    site = models.ForeignKey(Site, blank=True)

    def __str__(self):
        return self.url


