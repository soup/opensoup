# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from tumblelog.models import Post, ImagePost
from django.template.context import RequestContext
from django.conf import settings

def everyone(request):
	"Shows everyone's posts"

	posts = ImagePost.objects.all().order_by('-id')[:20]
	context = {
			'posts': posts,
			'title': _('Everyone'),
			'subtitle': _(u'See what everyone\'s posting – Go on, try scrolling all the way down :)')
		}
	return render_to_response('tumblelog/postlist.html', context_instance=RequestContext(request, context))

@login_required
def friends(request):
	"Shows your friend's posts"

	following = request.user.get_profile().following.values('id')
	posts = ImagePost.objects.filter(blog__owner__in = following).order_by('-id')[:20]
	context = {
			'posts': posts,
			'title': _('My friends'),
			'subtitle': _(u'Stuff your friends posted')
		}
	return render_to_response('tumblelog/postlist.html', context_instance=RequestContext(request, context))


def index(request):
	# Check if this is a user soup
	split_host = request.get_host().split('.')
	if(len(split_host) > len(settings.SITE_URL.split('.'))):
		return HttpResponse('User soup of {0}'.format(split_host[0]))

	# If the user's authenticated and this is not a user soup, redirect to /friends/.
	if request.user.is_authenticated():
		return redirect('/friends/')

	# Else, display standard index page
	return HttpResponse('You are not logged in. <a href="/everyone/">Everyone</a>')