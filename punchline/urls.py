from django.conf import settings
from django.conf.urls import include, url

from punchline.core import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
