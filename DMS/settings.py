"""
Django settings for DMS project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-nouq*g&rwq0!df8w@)p*=34l$p(g%+!zf1g@sg_@zns^aa!vx-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEPLOY = not DEBUG ## Turn off debug mode in production

ALLOWED_HOSTS = ['*']
DEFAULT_HASHING_ALGORITHM='sha1'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    ### for user authentication purpose ###
    "captcha",
    'accounts',

    ### our application list ####
    'vfms',
    # 'apptest', 
    'taggit',
     'crispy_forms',
    
    #'django_filebrowser',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DMS.urls"

# adding project_root to simplify migration to another system
PROJECT_ROOT=os.path.abspath(os.path.dirname(__file__))

TEMPKATES_DIR=(os.path.join(PROJECT_ROOT,'../templates'),)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR),'/templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "DMS.context_process.media_path",
                 
            ],
            'builtins': [
              
                'crispy_forms.templatetags.crispy_forms_tags',
            ],
        },
    },
]

WSGI_APPLICATION = "DMS.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        #"NAME": BASE_DIR / "localdms_db",
         "NAME": BASE_DIR / "vfms_db.sqlite3",
    }
}

# database_name = 'vfms_db' 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': database_name,
#         # 'NAME': 'tms_product5',
#         'USER': 'postgres',
#         'PASSWORD': 'cosaimp@2020',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]

## Media files (images) within django

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

## outside django
EXTERNAL_ROOT = os.path.join(BASE_DIR.parent, 'external')
EXTERNAL_URL = '/external/'
print(EXTERNAL_ROOT)

## DRIVE STORAGE for media files

DRIVE_ROOT = os.path.join('E:\COSAI', '/drive/')
#DRIVE_ROOT = os.path.join(BASE_DIR.parent,'/drive/')/uploadvideos/

                        #   'uploadvideos/brindha/mdu/centralcity/video2' )
DRIVE_URL = '/drive/'

UPLOAD_ROOT = os.path.join('E:\COSAI', '/upload/')
UPLOAD_URL = '/upload/'
# UPLOAD_ROOT = os.path.join(BASE_DIR.parent,'/drive/')
# /uploadvideos/

STORE_ROOT = os.path.join('E:\COSAI', '/store/')
STORE_URL = '/store/'

#                         #   'uploadvideos/brindha/mdu/centralcity/video2' )
# DRIVE_URL = '/drive/'

# UPLOAD_DIR = 'upload'
# UPLOAD_ROOT = os.path.join(DRIVE_ROOT, UPLOAD_DIR)
# UPLOAD_URL = os.path.join(DRIVE_URL, UPLOAD_DIR)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"