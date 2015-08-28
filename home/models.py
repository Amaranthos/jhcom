from django.db import models
from django.conf import settings
from django.db.models import permalink

import os

class Game(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor')
	links = models.ManyToManyField('home.Link')

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('game', None, {'slug':self.slug, 'id':self.id,})

class App(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor')
	links = models.ManyToManyField('home.Link')

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('app', None, {'slug':self.slug, 'id':self.id,})

class Tool(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor')
	links = models.ManyToManyField('home.Link')

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('tool', None, {'slug':self.slug, 'id':self.id,})

class Library(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor')
	links = models.ManyToManyField('home.Link')

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('library', None, {'slug':self.slug, 'id':self.id,})


class Site(models.Model):
	title = models.CharField(max_length=50, unique=True)
	thumbnail = models.CharField(max_length=40)
	link = models.URLField()

	def __str__(self):
		return self.title;

class Art(models.Model):
	title = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.title;

class Contributor(models.Model):
	name = models.CharField(max_length=50, unique=True)
	link = models.URLField()

	def __str__(self):
		return self.name

class Link(models.Model):
	name = models.CharField(max_length=50, unique=True)
	link = models.URLField()

	def __str__(self):
		return self.name