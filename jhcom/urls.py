from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'home.views.home', name='home'),
	url(r'^blog/$', 'blog.views.blog', name='blog'),
	url(r'^games/$', 'home.views.games', name='games'),
	url(r'^games/(?P<id>[0-9]+)/$', 'home.views.game', name='game'),
	url(r'^apps/$', 'home.views.apps', name='apps'),
	url(r'^apps/(?P<id>[0-9]+)/$', 'home.views.app', name='app'),
	url(r'^tools/$', 'home.views.tools', name='tools'),
	url(r'^tools/(?P<id>[0-9]+)/$', 'home.views.tool', name='tool'),
	url(r'^libraries/$', 'home.views.libraries', name='libraries'),
	url(r'^libraries/(?P<id>[0-9]+)/$', 'home.views.library', name='library'),
	url(r'^web/$', 'home.views.web', name='web'),
	url(r'^art/$', 'home.views.art', name='art'),
    url(r'^admin/', include(admin.site.urls)),
]
