# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

#from djorm_expressions.models import ExpressionManager    
from djorm_pguuid.fields import UUIDField 

class AbstractBaseModel(models.Model):
    uuid = UUIDField(auto_add=True, db_index=True, primary_key=True, unique=True)
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
class Url(AbstractBaseModel):
    url = models.URLField()
    site = models.ForeignKey(Site, blank=True)

    def __str__(self):
        return self.url

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff,
                                  is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, AbstractBaseModel):
    """
    A user based on the django.contrib.auth AbstractUser which suits 
    our needs. It's a full featured User model with admin-compliant 
    permissions.
    """
    email = models.EmailField(_('email address'), blank=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    site = models.ForeignKey(Site, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'uuid' #Must stay here because of validation
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

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


