from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Boost perf a little
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

INSTALLED_APPS += (
    'punchline.apps.core.tests.dummy',
)


try:
    from .local import *
except ImportError:
    pass
