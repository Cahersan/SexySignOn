from django.conf import settings  # noqa
from appconf import AppConf  # noqa

from formulator.models import Form 

# We want to get all the forms created by formulator

class RegisterConf(AppConf):

    FORMS = [(form.name, '%s.%s:%s' % (Form.__module__, Form.__name__, form.name)) for form in Form.objects.all()]
