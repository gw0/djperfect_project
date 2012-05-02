# -*- coding: utf-8 -*-
"""
Common settings for {{ project_name|title }} Django project.

.. seealso::
    http://docs.djangoproject.com/en/1.4/ref/settings/
"""


### Common configuration
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('{{ project_name|title }} Webmaster', 'webmaster@localhost'),
)
MANAGERS = ADMINS

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #    'NAME': '{{ project_name }}',               # Or path to database file if using sqlite3.
    #    'USER': '{{ project_name }}',               # Not used with sqlite3.
    #    'PASSWORD': 'SecretRandomPassword', # Not used with sqlite3.
    #    'HOST': 'localhost',                # Set to empty string for localhost. Not used with sqlite3.
    #    'PORT': '',                         # Set to empty string for default. Not used with sqlite3.
    #    'SCHEMA': '{{ project_name }}',             # Can be used with PostgreSQL.
    #}
}

SITE_ID = 1

# Unique secret key for safe cryptography (don't share it with anybody)
SECRET_KEY = 'SecretRandomKeyOverridenByLocalSettings'


### Python paths used by Django
WSGI_APPLICATION = 'main.wsgi.application'
ROOT_URLCONF = 'main.urls'


### Local time zone (under Windows it must be set to your system time zone)
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Chicago'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


### Internationalization and localization
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True


### Static files collected from apps' "static/" and STATICFILES_DIRS directories
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
    # Always use absolute paths with forward slashes, not relative paths.
)


### Media files uploaded by users
MEDIA_ROOT = ''
MEDIA_URL = ''


### Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Always use absolute paths with forward slashes, not relative paths.
)


### Middlewares
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


### Apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Comment out to disable the Django admin interface (also check urls.py):
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# App ...
#...


### Logging (eg. send error emails to site admins when DEBUG=False)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Import environment specific settings excluded from version control
try:
    import sys
    if not any( k.startswith('main.settings_')  for k in sys.modules.keys() ):
        from main.settings_local import *
except ImportError:
    try:
        from main.settings_{{ project_name }} import *
    except ImportError:
        pass
