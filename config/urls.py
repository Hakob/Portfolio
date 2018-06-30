from django.contrib import admin
from django.conf.urls import include, url, patterns
from django.conf import settings

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^', include('apps.portfolio.urls'))
]
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
