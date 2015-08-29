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
	contributors = models.ManyToManyField('home.Contributor', blank=True)
	links = models.ManyToManyField('home.Link', blank=True)
	posted = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('game', None, {'slug':self.slug, 'id':self.id,})

	class Meta:
		verbose_name = "Game"
		verbose_name_plural = "Games"

class App(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor', blank=True)
	links = models.ManyToManyField('home.Link', blank=True)
	posted = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('app', None, {'slug':self.slug, 'id':self.id,})

	class Meta:
		verbose_name = "App"
		verbose_name_plural = "Apps"

class Tool(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor', blank=True)
	links = models.ManyToManyField('home.Link', blank=True)
	posted = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('tool', None, {'slug':self.slug, 'id':self.id,})

	class Meta:
		verbose_name = "Tool"
		verbose_name_plural = "Tools"

class Library(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	thumbnail = models.CharField(max_length=40)
	description = models.TextField()
	contributors = models.ManyToManyField('home.Contributor', blank=True)
	links = models.ManyToManyField('home.Link', blank=True)
	posted = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title;

	@permalink
	def get_absolute_url(self):
		return ('library', None, {'slug':self.slug, 'id':self.id,})

	class Meta:
		verbose_name = "Library"
		verbose_name_plural = "Libraries"


class Site(models.Model):
	title = models.CharField(max_length=50, unique=True)
	thumbnail = models.CharField(max_length=40)
	link = models.URLField()

	def __str__(self):
		return self.title;

	class Meta:
		verbose_name = "Site"
		verbose_name_plural = "Sites"

class Art(models.Model):
	title = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.title;

	class Meta:
		verbose_name = "Art"
		verbose_name_plural = "Art"

class Tutorial(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, default=title)
	posted = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title;

	class Meta:
		verbose_name = "Tutorial"
		verbose_name_plural = "Tutorials"

class Contributor(models.Model):
	name = models.CharField(max_length=50, unique=True)
	link = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Contributor"
		verbose_name_plural = "Contributors"

class Link(models.Model):
	name = models.CharField(max_length=50, unique=True)
	link = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Link"
		verbose_name_plural = "Links"