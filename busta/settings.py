import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('aynu','brox2319@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'busta',
        'USER': 'nmuser',
        'PASSWORD': 'nmuser',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__),os.path.pardir))

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT,'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '=@r^$0xf#g@kc3hf7+ev8z+p8@7m*&amp;+_om97p92argks70v7f$'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'busta.urls'

WSGI_APPLICATION = 'busta.wsgi.application'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT,'templates'),)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'core'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
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
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}

try:
    from settings_local import *
except ImportError:
    pass