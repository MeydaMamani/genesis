from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'BD_GENESIS_V2',
        'USER': 'sa',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

DATABASE_CONNECTION_POOLING = False

STATIC_URL = '/static/'