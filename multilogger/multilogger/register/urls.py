from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.choose_register, name='choose'),
    url(r'^(?P<uuid>[0-9a-f]+)$', views.register_detail, name='signup'),
)
