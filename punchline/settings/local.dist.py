SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# LANGUAGE_CODE = 'fr-fr'

############
# Production
############

ALLOWED_HOSTS = []
ADMINS = ()
# STATIC_ROOT = ''

# If SSL enabled
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True  # Just in case, should be done by webserver instead
