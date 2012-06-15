from django.conf.urls import patterns, include, url
from piston.resource import Resource
from api.handlers import PostHandler

post_handler = Resource(PostHandler)

urlpatterns = patterns('',
	url(r'^posts/(?P<post_id>[^/]+)/', post_handler),
	url(r'^posts/$', post_handler),
)
