"""
Django settings for richs_app project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

try:
    from .local_settings import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Turn on true if you run it for production. 
# Several application handles commands by PRODUCTION values.
# i.e. Developer does not have Amazon MWS Keys so should not call MWS API whenever local development. 
# Note1: it was appended 2019.07 so more old things never use it except updated. 
# Note2: PRODUCTION should be same as (not DEBUG).  
PRODUCTION = False

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'rest_framework',
    'accounts',
    'top',
    'home',
    'yahoo',
    'mercari',
    'settings_amazon',
    'asyncworker',
    'admintools',
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

ROOT_URLCONF = 'richs_app.urls'

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

WSGI_APPLICATION = 'richs_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'richs',
        'USER': LOCAL_DATABASE['user'],
        'PASSWORD': LOCAL_DATABASE['password'],
        'HOST': LOCAL_DATABASE['host'],
        'PORT': LOCAL_DATABASE['port'],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'CONN_MAX_AGE': 0, # 0 means Never use DB connection cache. 
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 
STATIC_ROOT = os.path.join(BASE_DIR, "collectstatic/")

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# For AsyncWorker Settings (Redis)
ASYNC_WORKER = {
    'WAIT_DEFAULT_SECONDS': 1,                # ??????wait?????????????????????????????????
    'TASK_RECOMMENDED_MAXIMUM_SECONDS': 5,    # Worker???1??????????????????????????????????????????
    'TASK_RECOMMENDED_MAXIMUM_IMPORT_SECONDS': 60,    # Worker????????????????????????1??????????????????????????????????????????
    'MAXIMUM_SEQUENCE': -1,                   # job??????????????????????????????????????? (?????????????????????)
    'JOB_DEFAULT_TIMEOUT': 7200,              # 1???????????????????????????????????? (???????????????1??????)
    'REDIS': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB_FOR_DATA': 0,
        'DB_FOR_QUEUE': 0,
    },

    'QUEUE_NAME': 'default',
    'IMPORT_QUEUE_NAME': 'import_queue',
    'INVCHK_YAHOO_QUEUE_NAME': 'invchk_yahoo',     # Yahoo ???????????????????????????
    'INVRES_YAHOO_QUEUE_NAME': 'invres_yahoo',     # Yahoo ?????????????????????
    'INVCHK_MERCARI_QUEUE_NAME': 'invchk_mercari', # Mercari ???????????????????????????
    'INVRES_MERCARI_QUEUE_NAME': 'invres_mercari', # Mercari ?????????????????????
    'INV_QUEUE_ENOUGH_JOB_COUNT': 20,              # ??????????????????????????????????????????
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# ?????????RICHS?????????????????????????????????
TIME= 60*60
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
SESSION_SAVE_EVERY_REQUEST = True # 1??????????????????????????????????????????????????????
SESSION_EXPIRE_AT_BROWSER_CLOSE= True
SESSION_COOKIE_AGE = TIME
SESSION_IDLE_TIMEOUT = TIME



#?????????????????????
MY_MESSAGE_SUCCESS = '??????'
MY_MESSAGE_FAILED = '??????'
MY_MESSAGE_SAVE_SUCCESS = '??????????????????????????????'
MY_MESSAGE_SAVE_FAILED = '??????????????????????????????'
MY_MESSAGE_FORM_INVALID = '???????????????????????????'

# ??????????????????
RICHS_FOLDER_CSV_TEMPLATE='/var/www/richs/csv_template'
RICHS_FOLDER_CSV_OUTPUT='/var/www/richs_public/output'
RICHS_FOLDER_IMAGE='/var/www/richs_public/images'
RICHS_FOLDER_IMAGE_TMP='/var/www/richs_public/tmp'
RICHS_FOLDER_TMP='/var/www/richs_public/tmp'

# URL_PATH??????
RICHS_URL_IMAGE='/item_image'

# MWS????????????
RICHS_AWS_ACCESS_KEY = 'AKIAEXAMPLE'
RICHS_AWS_SECRET_KEY = 'EXAMPLE'
RICHS_AWS_REGION = 'JP'
RICHS_AWS_MARKETPLACE_ID = 'A1VEXAMPLE'

# ????????????????????????
RICHS_PROTOCOL='https'
RICHS_FQDN='srv1.merucarich.com'

# ?????????????????????
RICHS_PAGE_SIZE=50

# Yahoo?????????????????????
YAHOO_RIDE_SEARCH_CONFIG = {
    'MINIMUM_TITLE_LENGTH': 0,        # ?????????????????????????????? (default: 0)
    'MINIMUM_PROFIT': 0.3,            # ???????????????: (Amazon?????? - Yahoo??????) / Amazon??????, (default: 0.0) 
    'MAXIMUM_FULFILLMENT': 6,         # ?????????????????? (default: 6)
    'IGNORE_DELIVERY_FROM': ['??????'], # ???????????????????????? (default: [])
    'SKIP_JUDGE_ITEM': 1000,          # URL???????????????????????????????????????????????????
    'SKIP_JUDGE_LOWER_ITEM': 10,      # URL???????????????????????????????????????????????????????????????????????????????????????
}

# Merucari?????????????????????
MERCARI_RIDE_SEARCH_CONFIG = {
    'MINIMUM_TITLE_LENGTH': 0,        # ?????????????????????????????? (default: 0)
    'MINIMUM_PROFIT': 0.0,            # ???????????????: (Amazon?????? - Mercari??????) / Amazon??????, (default: 0.0) 
    'MAXIMUM_FULFILLMENT': 6,         # ?????????????????? (default: 6)
    'IGNORE_DELIVERY_FROM': [],       # ???????????????????????? (default: [])
    'SKIP_JUDGE_ITEM': 1000,          # URL???????????????????????????????????????????????????
    'SKIP_JUDGE_LOWER_ITEM': 10,      # URL???????????????????????????????????????????????????????????????????????????????????????
}

# ????????????????????????IP????????????
RIDE_SEARCH_EXTRA_IP_ADDRESSES = []

# ???????????????????????? (default: 3)
ITEM_RESTORE_DAYS = 3

# FJC Member ??????
FJC_MEMBER_CONFIG = {
    'TOKEN': '22efb8e4adf345c98115f89533d424c2',  # API??????????????????
    'EXPIRE_DAYS': 3,                             # ?????????????????????
    'URLS': [                                     # ????????????????????????
        'http://localhost:8000/system/api/fjcmember',
    ], 
}

# Amazon 503 ?????????????????????
AMAZON_ERROR_RETRY_SETTINGS = {
    'MAX_TRIAL': 60,                  # ?????????????????? (default: 60)
    'TRIAL_WAIT_SECONDS': 5,          # ???????????????????????????????????? (default: 5)
    'TRIAL_WAIT_COUNT': 12,           # ?????????????????? (default: 12)
}

# ?????????????????????????????????????????????
BACKGROUND_JOBS_CONFIG = {
    'RESTART_JOB_NEEDED': 15,       # ?????????????????????????????????????????????
    'SHUTDOWN_JOB_NEEDED': 30,      # ???????????????????????????????????????????????????
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'production': {
            'format': '\t'.join([
                "time:%(asctime)s",
                "level:%(levelname)s",
                "module:%(module)s",
                "process:%(process)d",
                "thread:%(thread)d",
                "path:%(pathname)s",
                "line:%(lineno)d",
                "message:%(message)s",
            ])
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'light': {
            'format': '%(message)s'
        }
    },
    'handlers': {
        # logging.handlers.RotationgFileHandler ????????????????????????????????????????????????
        # ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        # ??????????????????????????????????????? 
        # ????????????????????????????????????????????????????????? logrotate.d ???????????????
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',  #???????????????????????????
            'formatter': 'production',
        },
        'InventoryYahoo': {
            'class': 'logging.FileHandler',
            'filename': 'logs/inventory-yahoo.log',  #???????????????????????????
            'formatter': 'simple',
        },
        'InventoryMercari': {
            'class': 'logging.FileHandler',
            'filename': 'logs/inventory-mercari.log',  #???????????????????????????
            'formatter': 'simple',
        },
        'UpdateAmazonFeed': {
            'class': 'logging.FileHandler',
            'filename': 'logs/update-amazon-feed.log',  #???????????????????????????
            'formatter': 'simple',
        },
        'Batch': {
            'class': 'logging.FileHandler',
            'filename': 'logs/batches.log',
            'formatter': 'simple',
        },
        'rq': {
            'class': 'logging.FileHandler',
            'filename': 'logs/rq.log',  #???????????????????????????
            'formatter': 'production',
        },
        'rq.scheduler': {
            'class': 'logging.FileHandler',
            'filename': 'logs/rq-scheduler.log',  #???????????????????????????
            'formatter': 'simple',
        },
        'temporary': {
            'class': 'logging.FileHandler',
            'filename': 'logs/temporary.log',  #???????????????????????????
            'formatter': 'production',
        },
        'record': {
            'level': 'DEBUG', 
            'class': 'logging.FileHandler',
            'filename': 'logs/record.log',  #???????????????????????????
            'formatter': 'light',
        }, 
    },
    'loggers': {
        # ????????????????????????
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django?????????????????????
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Debug???????????????
        'richs_utils.TemporaryLogger': {
            'handlers': ['temporary'],
            'level': 'INFO',
            'propagate': False,
        },
        # ?????????????????????
        'richs_utils.RecordLogger': {
            'handlers': ['record'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # ???????????????????????????
        'richs_utils.InventoryYahoo': {
            'handlers': ['InventoryYahoo'],
            'level': 'INFO',
            'propagate': False,
        },
        'richs_utils.InventoryMercari': {
            'handlers': ['InventoryMercari'],
            'level': 'INFO',
            'propagate': False,
        },
        'richs_utils.UpdateAmazonFeed': {
            'handlers': ['UpdateAmazonFeed'],
            'level': 'INFO',
            'propagate': False,
        },
        'accounts.management.commands.check_background_jobs': {
            'handlers': ['Batch'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'accounts.management.commands.delete_old_items': {
            'handlers': ['Batch'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'accounts.management.commands.validate_mws_tokens': {
            'handlers': ['Batch'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # rq ?????????????????????
        'rq': {
            'handlers': ['rq'],
            'level': 'INFO',
            'propagate': False,
        },
        'rq.scheduler': {
            'handlers': ['rq.scheduler'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
