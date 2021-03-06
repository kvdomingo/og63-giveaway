"""
Django settings for giveaway project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import dj_database_url
import urllib
from pathlib import Path
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', '0')))

PYTHON_ENV = os.environ.get('PYTHON_ENV', 'production')

ALLOWED_HOSTS = ['giveaway.kvdstudio.app']

if DEBUG:
    ALLOWED_HOSTS.extend([
        'localhost',
        '127.0.0.1',
        '0.0.0.0',
    ])


# Application definition

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'giveaway.urls'

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGIN_REGEXES = [
    r'https:\/\/.*\.kvdstudio\.app',
]

if DEBUG:
    CORS_ALLOWED_ORIGIN_REGEXES.extend([
        r'http:\/\/localhost:\d{4,}',
        r'http:\/\/127\.0\.0\.1:\d{4,}',
        r'http:\/\/0\.0\.0\.0:\d{4,}',
    ])

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'web' / 'app'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'giveaway.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if PYTHON_ENV == 'development':
    DATABASE_CONFIG = dj_database_url.config()
else:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DATABASE_CONFIG = dj_database_url.parse(DATABASE_URL)
    DATABASE_CONFIG['HOST'] = urllib.parse.unquote(DATABASE_CONFIG['HOST'])

DATABASES = {'default': DATABASE_CONFIG}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [BASE_DIR / 'web' / 'app' / 'static']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DRAW_TOKEN = os.environ.get('DRAW_TOKEN')
