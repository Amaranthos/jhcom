from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'', include('home.urls')),
	url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^resume/$', 'home.views.flatpage', {'url': '/resume/'}, name='resume')
     url(r'', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))