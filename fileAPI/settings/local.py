from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

MINIO_URL = 'play.minio.io:9000'
MINIO_ACCESS_KEY = 'Q3AM3UQ867SPQQA43P2F'
MINIO_SECRET_KEY = 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'

MINIO_BUCKET_NAME = ''