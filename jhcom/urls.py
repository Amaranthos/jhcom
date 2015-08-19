from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'home.views.home', name='home'),
	url(r'^games/', 'home.views.games', name='games'),
    url(r'^admin/', include(admin.site.urls)),
]
