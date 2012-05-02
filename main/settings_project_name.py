# -*- coding: utf-8 -*-
"""
Production settings for {{ project_name|title }} Django project.
"""
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('{{ project_name|title }} Webmaster', 'webmaster@localhost'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}',               # Or path to database file if using sqlite3.
        'USER': '{{ project_name }}',               # Not used with sqlite3.
        'PASSWORD': '{% for r in ''|center:20 %}{{ secret_key|safe|random }}{% endfor %}', # Not used with sqlite3.
        'HOST': 'localhost',                # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                         # Set to empty string for default. Not used with sqlite3.
        'SCHEMA': '{{ project_name }}',             # Can be used with PostgreSQL.
    }
}

SECRET_KEY = '{{ secret_key|safe }}'

EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = '{{ project_name|title }} Webmaster <webmaster@localhost>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

