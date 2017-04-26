import tempfile

from .base import *

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

for logger in LOGGING['loggers'].values():
    logger['handlers'] = ['console']

AUTH_PASSWORD_VALIDATORS = []

MEDIA_ROOT = tempfile.gettempdir()

try:
    from .local import *
except ImportError:
    pass
