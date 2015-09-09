from django.db import models
from django.db.models import permalink
from django.contrib.sites.models import Site



class Blog(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)
	body = models.TextField()
	posted = models.DateField(auto_now_add=True)
	category = models.ManyToManyField('blog.Category')
	
	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('blog-post', None, {'slug':self.slug, 'id':self.id,})

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
		ordering = ["-posted"]


class Category(models.Model):
	title = models.CharField(max_length = 50, db_index=True)
	slug = models.SlugField(max_length=50, db_index=True)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('blog-category', None, {'slug':self.slug, 'id':self.id,})

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"
		ordering = ["title"]