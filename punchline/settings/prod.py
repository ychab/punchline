from .base import *

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
# Disable for django-autocomplete-light create op which use HTTP headers
CSRF_COOKIE_HTTPONLY = False

try:
    from .local import *
except ImportError:
    pass
