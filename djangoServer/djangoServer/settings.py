"""
Django settings for djangoServer project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pt1in9r3se&=6t_zxv-hlcq5t64o&a!v)_w2z%lt+hw$+#oa%h'

# 主要是为了安全，只允许你设置的域名（hosts）访问。
# 如果不加，或者设置为 “*”，那么有可能别人随便把一个域名的解析指向到你的服务器，都能访问
# ALLOWED_HOSTS = [
#     '127.0.0.1',
#     '192.168.0.113',
# ]

ALLOWED_HOSTS = [
    '*'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appname',
    'blogs',
    # 'server',
    'corsheaders',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'djangoServer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# PythonAnywhere = True  # 设为False是为了本地支持
PythonAnywhere = False  # 设为True是为了上线PythonAnywhere支持

if PythonAnywhere is False:
    DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DjangeTest',
            'USER': 'root',
            'PASSWORD': '12345678',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
elif PythonAnywhere is True:
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "Jamesholy2$DjangeTest",
            'USER': 'Jamesholy2',
            'PASSWORD': 'q5075391',
            'HOST': 'Jamesholy2.mysql.pythonanywhere-services.com',
        }
    }
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    # CORS_ORIGIN_WHITELIST = [
    #     'http://localhost:3000',
    #     'http://127.0.0.1:3000',
    #     'http://192.168.0.113:3000',
    # ]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'auth'
]
