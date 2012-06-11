from django.conf.urls import patterns, include, url
from tumblelog.views import *

urlpatterns = patterns('',
	url(r'^everyone/$', everyone),
)
