from .base import *

DEBUG = False

ALLOWED_HOSTS = ['hci.pythonanywhere.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
