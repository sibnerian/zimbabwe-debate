from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    url(r'^sponsors/', 'sponsors'),
    url(r'^members/', 'members'),
    url(r'^about/', 'about'),
)
