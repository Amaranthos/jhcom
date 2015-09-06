from django.conf.urls import include, url, patterns
from django.conf import settings

urlpatterns = [
	url(r'^$', 'blog.views.blog', name='blog'),
	url(r'^category/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.category', name='blog-category'),
	url(r'^(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.post', name='blog-post'),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))