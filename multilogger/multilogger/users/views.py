# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserForm, LoginForm

# Import the customized User model
from .models import User


def login_view(request):
    if request.method == 'POST': # If the form has been submitted...
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(
                site__url__url=request.get_host(),
                email=email)
        if not user.exists():
            return HttpResponse('Not a known user.')

        user = authenticate(uuid=user[0].uuid, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('You are now logged in.')
            else:
                return HttpResponse("Disabled user")
        return HttpResponse("Your username and password didn't match")
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {
        'form': form,
    })

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "email"
    slug_url_kwarg = "email"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
            kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                    kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
