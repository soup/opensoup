from piston.handler import BaseHandler
from tumblelog.models import Post, Asset

class PostHandler(BaseHandler):
	allowed_methods = ('GET',)
	exclude = ('_state')
	model = Post

	def read(self, request, post_id, count = 1):
		return Post.objects.filter(id__lt = post_id).order_by('-id')[:count]

class AssetHandler(BaseHandler):
	allowed_methods = ('GET',)
	exclude = ('_state')
	model = Asset

	def read(self, request, asset_id = None):
		if asset_id:
			return Asset.objects.filter(id = asset_id)
		
		return Asset.objects.all()