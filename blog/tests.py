from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from django.utils.text import slugify

from .models import Blog, Category, Tag

import factory.django

class CategoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category
		django_get_or_create = {
			'title',
			'slug'
		}

		name = 'Test Category'
		slug = slugify(name)

class TagFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Tag
		django_get_or_create = {
			'title',
			'slug'
		}

		name = 'Test Tag'
		slug = slugify(name)

class BaseAcceptanceTest(LiveServerTestCase):
	def setUp(self):
		self.client = Client()

class AdminTest(BaseAcceptanceTest):
	fixtures = ['users.json']

	def test_Login(self):
		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)		
		self.assertTrue('Log in' in response.content.decode('utf-8'))

		self.client.login(username='josh', password='123')

		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTrue('Log out' in response.content.decode('utf-8'))

	def test_Logout(self):
		self.client.login(username='josh', password='123')

		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTrue('Log out' in response.content.decode('utf-8'))

		self.client.logout()

		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTrue('Log in' in response.content.decode('utf-8'))

	def test_CreatePost(self):
		self.client.login(username="josh", password="123")

		response = self.client.get('/admin/blog/blog/add', follow=True)
		self.assertEquals(response.status_code, 200)

		category = CategoryFactory()
		tag = TagFactory()

		response = self.client.post('/admin/blog/blog/add', {
				'title': 'Test',
				'slug' : 'test',
				'body' : 'Example body',
				'posted' : '2015-09-07',
				'category' : str(category.pk),
				'tags' : str(tag.pk)
			}, follow=True)

		self.assertEquals(response.status_code, 200)
		self.assertTrue('added successfully' in response.content.decode('utf-8'))

		posts = Blog.objects.all()
		self.assertEquals(len(posts), 1)


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