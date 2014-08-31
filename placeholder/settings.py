import os
import sys

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

SECRET_KEY = 'braooejay62ub78j-_w%7fsq4+0#mqjmjh19firbtitavc^7(j'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

ROOT_URLCONF = 'placeholder.urls'

WSGI_APPLICATION = 'placeholder.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
