# -*- coding: utf-8 -*-
"""
Common settings for {{ project_name|title }} Django project.

.. seealso::
    http://docs.djangoproject.com/en/1.4/ref/settings/
"""

# Settings helpers
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
def path_prepare(*args):
    path = os.path.join(*args)
    if not os.path.exists(path):
        os.makedirs(path)
    return path
_ = lambda s: s


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
#SECRET_KEY = 'SecretRandomKeyOverridenByLocalSettings'


### Email configuration
EMAIL_SUBJECT_PREFIX = '[{{ project_name|title }}] '
#EMAIL_HOST = 'localhost'
#DEFAULT_FROM_EMAIL = '{{ project_name|title }} Webmaster <webmaster@localhost>'
#SERVER_EMAIL = DEFAULT_FROM_EMAIL


### Python paths and sane fixes for default Django settings
WSGI_APPLICATION = 'main.wsgi.application'
ROOT_URLCONF = 'main.urls'
#FORMAT_MODULE_PATH = 'main.formats'

FORCE_SCRIPT_NAME = ''
URL_VALIDATOR_USER_AGENT = 'Django'
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/'
LOGOUT_URL = '/admin/logout/'


### Local time zone (under Windows it must be set to your system time zone)
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


### Internationalization and localization
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True


### Static files collected from apps' "static/" and STATICFILES_DIRS directories
STATIC_ROOT = path_prepare(PROJECT_ROOT, 'www', 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
    # Always use absolute paths with forward slashes, not relative paths.
    path_prepare(PROJECT_ROOT, 'main', 'static'),
)


### Media files uploaded by users
MEDIA_ROOT = path_prepare(PROJECT_ROOT, 'www', 'media')
MEDIA_URL = '/media/'


### Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Always use absolute paths with forward slashes, not relative paths.
    path_prepare(PROJECT_ROOT, 'main', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    #'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
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
    # Official Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Comment out to disable the Django admin interface (also check urls.py):
    'django.contrib.admin',
    'django.contrib.admindocs',
    # Other useful official Django apps (check their documentation):
    #'django.contrib.comments',
    #'django.contrib.sitemaps',

    # General third-party apps
    # Uncomment to enable the database migration layer:
    #'south',
    # Uncomment to enable flexible asset management (JS, CSS, LESS, SASS...):
    #'django_assets',
    # Other useful third-party apps (for debugging and alternative logging):
    #'debug_toolbar',
    #'sentry',
    #'sentry.client',

    # Add other third-party apps here

    # Add your apps here
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
