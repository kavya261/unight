"""
Django settings for the Unight project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECRET_KEY = 'django-insecure-y6on4&^y1+^c$5_h4eh-i2fz-c6jmagos9$5b!o!%8=08s#!tm'

SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-y6on4&^y1+^c$5_h4eh-i2fz-c6jmagos9$5b!o!%8=08s#!tm')
DEBUG = 'RENDER' not in os.environ
# DEBUG = True

SESSION_COOKIE_HTTPONLY = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_SPOTIFY_SCOPE = ['user-read-email', 'user-library-read']

# ALLOWED_HOSTS = ['*']

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

SITE_ID = 1
# ACCOUNT_EMAIL_VERIFICATION = "none"
# LOGIN_REDIRECT_URL = "http://127.0.0.1:8000/"
LOGIN_REDIRECT_URL = "http://127.0.0.1:8000/signin"

# ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'


# ACCOUNT_LOGOUT_ON_GET = True
# Application definition
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.spotify.SpotifyOAuth2',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'channels',
    'core',
    'room',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.eventbrite',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.shopify',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.apple',
    'whitenoise.runserver_nostatic',
    # 'allauth.socialaccount.providers.tiktok',
    # 'allauth.socialaccount.providers.opensea',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'Unight.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

SOCIAL_AUTH_SPOTIFY_KEY = 'dcab84e68aa048e3ab5129c8bc52d755'
SOCIAL_AUTH_SPOTIFY_SECRET = '25e40674ad15416ca32a8827286158ec'

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': 'e4b2af6b571efd9e03c1',
            'secret': '8f2d3a41e26f25ebd59df4bb42c4d6e436c5083a',
            'key': ''
        }
    },
    'facebook': {
        'APP': {
            'client_id': '733109821422303',
            'secret': 'd8ddd93e6b9ebec48faa3c34b963f16e',
            'key': ''
        }
    },
    'instagram': {
        'APP': {
            'client_id': '1312196812972649',
            'secret': 'c18e25473b8ac7a63e4daf0ce749d153',
            'key': ''
        }
    },
    'ebay': {
        'APP': {
            'client_id': 'kaveripa-unight-PRD-d5206ac65-b205be68',
            'secret': 'c18e25473b8ac7a63e4daf0ce749d153',
            'key': ''
        }
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'shopify': {
        'IS_EMBEDDED': True,
    },
    "apple": {
        "APP": {

            "client_id": "com.unight.test",

            "secret": "23Y6K4DWKQ",

            "key": "3WNW5YSZ3N",

            "certificate_key": """-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgOhbuxd9tTN7RE1AN
S7q/mjZI2XdLZho6tlvgayayFZOgCgYIKoZIzj0DAQehRANCAASENaI1rQaRFo6p
odXX9IPFo8RfSG49tryxd0RGYwjAnl9Kzzu6/F7Sxyef8I5AaQBYBIPqQWQHdYYA
nIYSY3ne
-----END PRIVATE KEY-----"""
        }
    },
}

ASGI_APPLICATION = 'Unight.asgi.application'
WSGI_APPLICATION = 'Unight.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': dj_database_url.parse(config('DATABASES'))
# }

# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'unightdb',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': '127.0.0.1',
#         'PORT': 5432,
#    }
# }

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgresql://unightdb:12345@localhost:5432/unight',
        conn_max_age=600
    )
}
# DATABASES = {
#     'default': dj_database_url.config(
#         # Feel free to alter this value to suit your needs.
#         default='postgresql://unightdb:12345@localhost:5433/Unight',
#         conn_max_age=600
#     )
# }
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
