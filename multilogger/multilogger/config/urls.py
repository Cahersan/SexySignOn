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
from multilogger.api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='pages/landing.html'),
        name="landing"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    #url(r'^users/', include("multilogger.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^signup/', include('multilogger.register.urls', namespace='register')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', 'django.contrib.auth.views.login', {
            'template_name': 'pages/login.html',
            }),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
