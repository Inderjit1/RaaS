"""
Django settings for robotrainer project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(find_dotenv())



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w*aurx90op#v4j#70oh!%hlqxhfhu4a%jaf^a!6*$kzyiqcf33'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CRISPY_TEMPLATE_PACK = 'bootstrap4'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'django_jsonforms',
    'crispy_forms'
    # 'django_saml2_auth'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'robotrainer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'backend', 'templates', 'backend')],
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

WSGI_APPLICATION = 'robotrainer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_IDENTIFIER'),
        'USER': os.environ.get('MYSQL_USERNAME'),
        'PASSWORD': os.environ.get('MYSQL_PWD'),
        'HOST': os.environ.get('MYSQL_HOST'),
        'PORT': 3306
    }
}


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

# SAML2_AUTH = {
#     'METADATA_AUTO_CONF_URL':'https://dev-46668607.okta.com/app/dev-46668607_raas_1/exk5caf4r7hA2DHDr5d7/sso/saml/metadata',
#     'DEFAULT_NEXT_URL': '/backend/',
#     'CREATE_USER': 'False',
#     # Create a new Django user when a new user logs in. In our case we do
#     # not create new.
#     # 'NEW_USER_PROFILE': {
#     # 'USER_GROUPS': [], # The default group name when a new user logs in
#     # 'ACTIVE_STATUS': True, # The default active status for new users
#     # 'STAFF_STATUS': True, # The staff status for new users
#     # 'SUPERUSER_STATUS': False, # The superuser status for new users
#     # },
#     # the value of keys below should be same as on the okta setting
#     'ATTRIBUTES_MAP': {
#         'FirstName': 'FirstName',
#         'LastName' : 'LastName',
#         'Email'    : 'Email'
#     },
#     # triggers can be used to perform various task. Before_login is triggered right when the saml
#     # response comes form idp
#     'TRIGGER': {
#     # # 'CREATE_USER': 'path.to.your.new.user.hook.method',
#         'BEFORE_LOGIN': 'Sample-Project_dashboard.views.my_view',
#     },
#     'ASSERTION_URL': 'http://localhost:8000', # Custom URL to validate incoming SAML requests against
#     'ENTITY_ID': 'http://localhost:8000/saml2_auth/acs/', # Populates the Issuer element in authn request
#     'NAME_ID_FORMAT': "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress", # Sets the Format property of authn NameIDPolicy element
# }


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
