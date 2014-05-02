# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from multilogger.register import views as register_views
from multilogger.api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)

urlpatterns = patterns('',
    url(r'^login/home/$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^login/about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("multilogger.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'^signup/$', register_views.formView, name='register_signup'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', 'django.contrib.auth.views.login', {
            'template_name': 'pages/login.html'
            }),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
