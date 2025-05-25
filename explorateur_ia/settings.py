from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'explorateur-secret'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'base',
    'raisonnement',
    'nlp',
    'vision',
    'connaissance',
    'planning',
    'robotique',
    'ml',
]

MIDDLEWARE = ['django.middleware.common.CommonMiddleware']

ROOT_URLCONF = 'explorateur_ia.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {},
}]

WSGI_APPLICATION = 'explorateur_ia.wsgi.application'
STATIC_URL = '/static/'