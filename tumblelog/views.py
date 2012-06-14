# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from tumblelog.models import Post, ImagePost, Blog, Asset
from django.template.context import RequestContext
from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class AssetForm(ModelForm):
	class Meta:
		model = Asset
		fields = ('directory', 'num', 'diskfile')

def everyone(request):
	"Shows everyone's posts"

	posts = ImagePost.objects.all().order_by('-id')[:20]
	context = {
			'posts': posts,
			'title': _('Everyone'),
			'site_url': settings.SITE_URL,
			'uploadform': AssetForm(),
			'subtitle': _(u'See what everyone\'s posting – Go on, try scrolling all the way down :)')
		}
	return render_to_response('tumblelog/postlist.html', context_instance=RequestContext(request, context))

@login_required
def friends(request):
	"Shows your friend's posts"

	following = request.user.get_profile().following.values('id')
	posts = ImagePost.objects.filter(blog__in = following).order_by('-id')[:20]
	context = {
			'posts': posts,
			'title': _('My friends'),
			'site_url': settings.SITE_URL,
			'uploadform': AssetForm(),
			'subtitle': _(u'Stuff your friends posted')
		}
	return render_to_response('tumblelog/postlist.html', context_instance=RequestContext(request, context))


def user_soup(request, blogname):
	blog = get_object_or_404(Blog, name = blogname)
	posts = ImagePost.objects.filter(blog = blog).order_by('-id')[:20]

	context = {
			'posts': posts,
			'title': blog.title,
			'site_url': settings.SITE_URL,
			'favicon': settings.MEDIA_URL + blog.avatar.url(),
			'uploadform': AssetForm(),
			'subtitle': _(u'Description description description.')
		}
	return render_to_response('tumblelog/postlist.html', context_instance=RequestContext(request, context))


def index(request):
	# Check if this is a user soup
	split_host = request.get_host().split('.')
	if(len(split_host) > len(settings.SITE_URL.split('.'))):
		return user_soup(request, split_host[0])

	# If the user's authenticated and this is not a user soup, redirect to /friends/.
	if request.user.is_authenticated():
		return redirect('/friends/')

	# Else, display standard index page
	return HttpResponse('You are not logged in. <a href="/everyone/">Everyone</a>')

def signup(request):
	if request.user.is_authenticated():
		return redirect('/friends/')

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/friends/")
	else:
		form = UserCreationForm()
		return render_to_response("signup.html", context_instance = RequestContext(request, {
			'form': form,
			'title': 'Create an account',
			'subtitle': 'Hooray! A new user!'
		}))

def upload(request):
	if not request.method == 'POST':
		return HttpResponse('Nothing posted.')

	form = AssetForm(request.POST, request.FILES)
	if not form.is_valid():
		return HttpResponse('Invalid data.')

	asset = form.save()

	# Le hack
	ImagePost(blog = Blog.objects.filter(owner = request.user)[0], asset = asset).save()
	return HttpResponse('Success')

