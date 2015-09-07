from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from .models import Blog, Category

class BlogTest(TestCase):
	def test_CreatePost(self):
		
		post = Blog()
		post.title = "Test Post"
		post.slug = slugify(post.title)
		post.body = "Test body text."
		post.posted = timezone.now()
		
		post.save()

		posts = Blog.objects.all()
		self.assertEquals(len(posts),1)
		self.assertEquals(posts[0], post)

		self.assertEquals(posts[0].title, "Test Post")
		self.assertEquals(posts[0].slug, "test-post")
		self.assertEquals(posts[0].body, "Test body text.")
		self.assertEquals(posts[0].posted.year, post.posted.year)
		self.assertEquals(posts[0].posted.month, post.posted.month)
		self.assertEquals(posts[0].posted.day, post.posted.day)

class CategoryTest(TestCase):
	def test_CreateCategory(self):

		category = Category()
		category.title = "Example"
		category.slug = slugify(category.title)

		category.save()

		categories = Category.objects.all()
		self.assertEquals(len(categories),1)
		self.assertEquals(categories[0].title, "Example")
		self.assertEquals(categories[0].slug, "example")