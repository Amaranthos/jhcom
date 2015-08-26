from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'blog.views.blog', name='blog'),
	url(r'^category/(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.category', name='blog-category'),
	url(r'^(?P<id>[0-9]+)/(?P<slug>[-\w\d]+)/$', 'blog.views.post', name='blog-post'),
]