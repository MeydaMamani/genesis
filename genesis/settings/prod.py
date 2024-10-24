from .base import *

DEBUG = True

ALLOWED_HOSTS = ['200.37.187.155']

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'BD_GENESIS2',
        'USER': 'OEIT-MEYDA',
        'PASSWORD': 'M4yit@24',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

DATABASE_CONNECTION_POOLING = False

STATIC_URL = '/static/'