from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from tumblelog.models import Post, ImagePost
from django.template.context import RequestContext

def everyone(request):
	"Shows everyone's posts"

	posts = ImagePost.objects.all().order_by('-id')[:20]
	return render_to_response('tumblelog/everyone.html', context_instance=RequestContext(request, {'posts': posts}))

@login_required
def friends(requests):
	pass
