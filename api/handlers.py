from piston.handler import BaseHandler
from tumblelog.models import Post

class PostHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = Post

	def read(self, request, post_id = None):
		if post_id:
			return Post.objects.filter(id = post_id)
		
		return Post.objects.all()