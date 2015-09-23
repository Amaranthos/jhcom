from django.conf.urls import include, url, patterns
from django.conf import settings

urlpatterns = [
	url(r'^$', 'home.views.home', name='home'),
	url(r'^games/$', 'home.views.games', name='games'),
	url(r'^games/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'home.views.game', name='game'),
	url(r'^apps/$', 'home.views.apps', name='apps'),
	url(r'^apps/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'home.views.app', name='app'),
	url(r'^tools/$', 'home.views.tools', name='tools'),
	url(r'^tools/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'home.views.tool', name='tool'),
	url(r'^libraries/$', 'home.views.libraries', name='libraries'),
	url(r'^libraries/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'home.views.library', name='library'),
	url(r'^web/$', 'home.views.web', name='web'),
	url(r'^art/$', 'home.views.art', name='art'),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))