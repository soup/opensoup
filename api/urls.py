from django.conf.urls import patterns, include, url
from piston.resource import Resource
from api.handlers import PostHandler, AssetHandler

post_handler = Resource(PostHandler)
asset_handler = Resource(AssetHandler)

urlpatterns = patterns('',
	url(r'^posts/(?P<post_id>[^/]+)/', post_handler),
	url(r'^posts/$', post_handler),

	url(r'^assets/(?P<asset_id>[^/]+)/', asset_handler),
	url(r'^assets/$', asset_handler),
)
