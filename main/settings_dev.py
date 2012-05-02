# -*- coding: utf-8 -*-
"""
Development settings for {{ project_name|title }} Django project.
"""
from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('{{ project_name|title }} Webmaster', 'webmaster@localhost'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, '{{ project_name }}_dev.db'), # Or path to database file if using sqlite3.
        'USER': '',                         # Not used with sqlite3.
        'PASSWORD': '',                     # Not used with sqlite3.
        'HOST': '',                         # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                         # Set to empty string for default. Not used with sqlite3.
        'SCHEMA': '',                       # Can be used with PostgreSQL.
    }
}

SECRET_KEY = '{{ secret_key|safe }}'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

