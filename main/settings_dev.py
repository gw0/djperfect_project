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

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

# App debug_toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

