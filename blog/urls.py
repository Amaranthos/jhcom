from django.conf.urls import include, url, patterns
from django.conf import settings

urlpatterns = [
	url(r'^$', 'blog.views.blog', name='blog'),
	url(r'^category/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.category', name='blog-category'),
	url(r'^tag/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.tag', name='blog-tag'),
	url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0-9])/$', 'blog.views.dates', name='blog-date'),
	url(r'^(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.post', name='blog-post'),
]