from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'front', name='front'),
    url(r'^(?P<year>\d{4})$', 'year', name='year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})$', 'month', name='month'),
    url(r'^users/(?P<username>[\w]+)$', 'user', name='user'),
    url(r'^posts/(?P<slug>[\w-]+)$', 'post', name='post'),
    url(r'^categories/(?P<slug>[\w-]+)$', 'category', name='category'),
    url(r'^tags/(?P<slug>[\w-]+)$', 'tag', name='tag'),
)