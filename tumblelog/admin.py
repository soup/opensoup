from tumblelog.models import Blog, Asset, Post, UserProfile
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(Blog)
admin.site.register(Asset)
admin.site.register(Post)