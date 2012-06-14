# coding: utf-8
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import random
import os

class Blog(models.Model):
	owner = models.ForeignKey(User, verbose_name = _('Owner'))
	name = models.SlugField()
	title = models.CharField(max_length = 250)
	avatar = models.ForeignKey('Asset')

	__unicode__ = lambda self: '{0} ({1})'.format(self.title, self.name)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	following = models.ManyToManyField(Blog, related_name='following', blank = True)

	__unicode__ = lambda self: self.user.username

# Automatically create a new user profile when a new user is added
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

# An asset in the file system (i.e. image, video, …)
class Asset(models.Model):
	# Recycle the old soup.io URL scheme
	random_part = models.CharField(max_length = 4, blank = True)
	directory = models.IntegerField()
	num = models.IntegerField()
	extension = models.CharField(max_length = 4, blank = True, editable = False)

	url = lambda self: '{0}/{1}_{2}.{3}'.format(self.directory, self.num, self.random_part, self.extension)
	diskfile = models.ImageField(upload_to = lambda self, filename: self.url())

	def save(self):
		if not self.random_part:
			# Generate a random number, convert it to it's hexadecimal form
			# (without the 0x). The :0>4 in the format string means it always
			# should have at least 4 chars. If it doesn't, it'll add zeroes on
			# the left side.
			self.random_part = '{0:0>4}'.format(hex(random.randrange(0, 0xffff))[2:])

		if not self.extension:
			self.extension = self.diskfile.path.split('.')[-1]

		super(Asset, self).save()

	def delete(self):
		if os.path.exists(self.diskfile.path):
			os.remove(self.diskfile.path)

		super(Asset, self).delete()

	__unicode__ = url

# Post types
class Post(models.Model):
	blog = models.ForeignKey(Blog)
	url = models.SlugField(blank = True)
	reposted_via = models.ForeignKey('self', related_name = 'post_reposted_via', blank = True, null = True)
	origin = models.ForeignKey('self', related_name = 'post_origin', blank = True, null = True)
	
	__unicode__ = lambda self: 'Post {0} @ {1}'.format(self.url if self.url else self.id, self.blog.name)

class ImagePost(Post):
	asset = models.ForeignKey(Asset)