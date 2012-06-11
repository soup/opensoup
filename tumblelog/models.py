# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
import random

class Blog(models.Model):
	owner = models.ForeignKey(User)
	name = models.SlugField()
	title = models.CharField(max_length = 250)
	avatar = models.ForeignKey('Asset')

	__unicode__ = lambda self: '{0} ({1})'.format(self.title, self.name)

# An asset in the file system (i.e. image, video, …)
class Asset(models.Model):
	# Recycle the old soup.io URL scheme
	random_part = models.CharField(max_length = 4, blank = True)
	directory = models.IntegerField()
	num = models.IntegerField()
	extension = models.CharField(max_length = 4)

	url = lambda self: '{0}/{1}_{2}.{3}'.format(self.directory, self.num, self.random_part, self.extension)
	diskfile = models.ImageField(upload_to = lambda self, filename: self.url())

	def save(self):
		if not self.random_part:
			# Generate a random number, convert it to it's hexadecimal form
			# (without the 0x). The :0>4 in the format string means it always
			# should have at least 4 chars. If it doesn't, it'll add zeroes on
			# the left side.
			self.random_part = '{0:0>4}'.format(hex(random.randrange(0, 0xffff))[2:])

		super(Asset, self).save()

	__unicode__ = url

# Post types
class Post(models.Model):
	blog = models.ForeignKey(Blog)
	url = models.SlugField(blank = True)
	
	__unicode__ = lambda self: self.url

class ImagePost(Post):
	asset = models.ForeignKey(Asset)