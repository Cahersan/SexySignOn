from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from formulator.models import Form
from multilogger.users.models import User

from .models import Profile
from .models import Register
from .conf import settings


class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

def register_detail(request, uuid):

    reg = Register.objects.get(uuid=uuid)
    formulatorForm = Form.objects.get(name=reg.form.name).form_class_factory()
    
    import ipdb; ipdb.set_trace()
    
    if request.method == 'POST': # If the form has been submitted...
        userForm = UserRegisterForm(request.POST)
        profileForm = formulatorForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            email = userForm.cleaned_data['email']
            password = userForm.cleaned_data['password']
            User.objects.create_user(email, password)

            return HttpResponse('You are successfully registered. Thanks.')
    else:
        userForm = UserRegisterForm()
        profileForm = formulatorForm() # An unbound form

    return render(request, 'register/register_form.html', {
        'user_form': userForm,
        'profile_form': profileForm,
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

