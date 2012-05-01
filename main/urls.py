# -*- coding: utf-8 -*-
"""
URL dispatcher config for {{ project_name|title }} Django project.
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = []

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('',
        url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL+'img/favicon.ico'}),
        url(r'^robots\.txt$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL+'robots.txt'}),
    )

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
