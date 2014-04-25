from django.db import models
from formulator.models import Form

from .conf import settings

class Register(models.Model):
    LANGS = [('EN', 'English'), ('ES', 'Espanol'), ('DE', 'Deutsch')]
    URLS = ('sdv.mysubmit.to')

    url = models.CharField(max_length=100)
    lang = models.CharField(max_length=2, choices=LANGS, default='EN')
    form = models.ForeignKey(Form)

    def __unicode__(self):
        return self.url
