from django.conf import settings
from django.conf.urls import include, url

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from punchline.core import admin
from punchline.music.views import PunchlineViewSet

router = DefaultRouter()
router.register(r'music-punchlines', PunchlineViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='Punchline API docs'))
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
