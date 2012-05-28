# -*- coding: utf-8 -*-
"""
URL dispatcher config for {{ project_name|title }} Django project.
"""
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = []

if settings.DEBUG:
    # Special directives that should be handled by production web server
    #urlpatterns += staticfiles_urlpatterns()  # already by default
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('',
        url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL+'img/favicon.ico'}),
        url(r'^apple-touch-icon\.png$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL+'img/apple-touch-icon.png'}),
        url(r'^robots\.txt$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL+'robots.txt'}),
    )

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
