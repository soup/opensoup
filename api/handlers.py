from piston.handler import BaseHandler
from tumblelog.models import Post, Asset

class PostHandler(BaseHandler):
	allowed_methods = ('GET',)
	exclude = ('_state')
	model = Post

	def read(self, request, post_id = None):
		if post_id:
			return Post.objects.filter(id = post_id)

		return Post.objects.all()

class AssetHandler(BaseHandler):
	allowed_methods = ('GET',)
	exclude = ('_state')
	model = Asset

	def read(self, request, asset_id = None):
		if asset_id:
			return Asset.objects.filter(id = asset_id)
		
		return Asset.objects.all()