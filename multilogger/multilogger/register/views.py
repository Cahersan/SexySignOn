from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from formulator.models import Form

from .models import Register
from .conf import settings


class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    repeat_password = forms.CharField()

def register_detail(request, uuid):

    reg = Register.objects.get(uuid=uuid)
    formulatorForm = Form.objects.get(name=reg.form.name).form_class_factory()
    
    if request.method == 'POST': # If the form has been submitted...
        form = formulatorForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponse('You are successfully registered. Thanks.')
    else:
        form = formulatorForm() # An unbound form

    return render(request, 'register/register_form.html', {
        'user_form': UserRegisterForm(),
        'register_form': form,
    })

def choose_register(request):
    host = request.get_host()
    registers = Register.objects.filter(url=host, choosable=True, active=True)
    
    if registers.count()==0:
        return HttpResponse('Registration is not available!')
    elif registers.count()==1:
        return HttpResponseRedirect('/signup/' + registers[0].uuid.hex)
    else:
        return render(request, 'register/choose_register.html', {
            'registers': registers,
        })

