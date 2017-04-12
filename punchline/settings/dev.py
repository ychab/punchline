from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

for logger in LOGGING['loggers'].values():
    logger['handlers'] = ['console']

AUTH_PASSWORD_VALIDATORS = []

try:
    from .local import *
except ImportError:
    pass
