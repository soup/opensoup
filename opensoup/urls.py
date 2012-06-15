from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

if settings.DEBUG:
	urlpatterns = patterns('django.views.static',
		url(r'^static/(?P<path>.*)$',  'serve', {'document_root': '/tmp/opensoup-static/', 'show_indexes': True }),
		url(r'^asset/(?P<path>.*)$',  'serve', {'document_root': '/tmp/opensoup-asset/', 'show_indexes': True }),
	)
else:
	urlpatterns = patterns('')

urlpatterns += patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^api/v1/', include('api.urls')),
	url(r'^i18n/', include('django.conf.urls.i18n')),

 	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
 	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),

 	url(r'', include('tumblelog.urls')),
)