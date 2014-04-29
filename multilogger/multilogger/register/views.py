from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from formulator.models import Form

from .models import Register
from .conf import settings

#@login_required()
def formView(request):
    host = request.get_host()
    reg = Register.objects.get(url=host)
    register_form = Form.objects.get(name=reg.form.name).form_class_factory()
    
    return render(request, 'register/register_form.html', {
        'register_form': register_form(),
    })
