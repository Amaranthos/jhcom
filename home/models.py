from django.db import models
from django.conf import settings

import os

class Game(models.Model):
	title = models.CharField(max_length=20, unique=True)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)

	def __str__(self):
		return self.title;

class App(models.Model):
	title = models.CharField(max_length=20, unique=True)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)

	def __str__(self):
		return self.title;

class Tool(models.Model):
	title = models.CharField(max_length=20, unique=True)
	video = models.URLField()
	thumbnail = models.CharField(max_length=40)

	def __str__(self):
		return self.title;

class Library(models.Model):
	title = models.CharField(max_length=20, unique=True)
	link = models.URLField()
	thumbnail = models.CharField(max_length=40)

	def __str__(self):
		return self.title;

class Site(models.Model):
	title = models.CharField(max_length=20, unique=True)
	thumbnail = models.CharField(max_length=40)

	def __str__(self):
		return self.title;

class Art(models.Model):
	title = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.title;