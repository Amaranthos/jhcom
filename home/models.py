from django.db import models

class Game(models.Model):
	title = models.CharField(max_length=20)
	video = models.URLField()

	def __str__(self):
		return title;