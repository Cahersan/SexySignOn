from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django_hstore import hstore
from formulator.models import Form
from multilogger.users.models import User, App 
from djorm_pguuid.fields import UUIDField 
#from djorm_expressions.models import ExpressionManager    

class AbstractBaseModel(models.Model):
    uuid = UUIDField(auto_add=True, db_index=True)
    #objects = ExpressionManager()

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Register(AbstractBaseModel):
    LANGS = [('EN', 'English'), ('ES', 'Espanol'), ('DE', 'Deutsch')]

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    lang = models.CharField(max_length=2, choices=LANGS, default='EN')
    active = models.BooleanField(default=True)
    choosable = models.BooleanField(default=True)
    begin = models.DateTimeField(_('Registration starts on'))
    end = models.DateTimeField(_('Registration ends on'))
    form = models.ForeignKey(Form)

    def __str__(self):
        return self.name + ' at ' + self.url

@python_2_unicode_compatible
class Profile(AbstractBaseModel):
    user = models.ForeignKey(User)
    apps = models.ManyToManyField(App)
    #data = hstore.DictionaryField()

    def __str__(self):
        return 'User ' + self.user.username + ' in site ' + self.site.name

