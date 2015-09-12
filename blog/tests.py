from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from django.utils.text import slugify

import factory

from .models import Blog, Category, Tag

class CategoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category	

	title = "Test Category"
	slug = slugify(title)

class TagFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Tag

	title = 'Test Tag'
	slug = slugify(title)

class PostFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Blog

	title = 'Test Post'
	slug = slugify(title)
	body = "Test content"
	posted = timezone.now()
	category = factory.SubFactory(CategoryFactory)

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
		category = CategoryFactory()
		tag = TagFactory()

		self.client.login(username="josh", password="123")

		response = self.client.get('/admin/blog/blog/add/', follow=True)
		self.assertEqual(response.status_code, 200)

		category = CategoryFactory()
		tag = TagFactory()

		response = self.client.post('/admin/blog/blog/add/', {
				'title': 'Test Post',
				'slug' : 'test-post',
				'body' : 'Test content',
				'posted' : '2015-09-07',
				'category' : str(category.pk),
				'tags' : str(tag.pk)
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('added successfully' in response.content.decode('utf-8'))

		posts = Blog.objects.all()
		self.assertEqual(len(posts), 1)


class BlogTest(TestCase):
	def test_CreatePost(self):
		
		post = PostFactory()
		tag = TagFactory()

		post.tags.add(tag)
		
		posts = Blog.objects.all()
		self.assertEquals(len(posts),1)
		self.assertEquals(posts[0], post)

		self.assertEquals(posts[0].title, "Test Post")
		self.assertEquals(posts[0].slug, "test-post")
		self.assertEquals(posts[0].body, "Test content")
		self.assertEquals(posts[0].posted.year, post.posted.year)
		self.assertEquals(posts[0].posted.month, post.posted.month)
		self.assertEquals(posts[0].posted.day, post.posted.day)
		self.assertEquals(posts[0].category.title, 'Test Category')
		self.assertEquals(posts[0].category.slug, 'test-category')

		tags = posts[0].tags.all()
		self.assertEquals(len(tags), 1)
		self.assertEquals(tags[0], tag)
		self.assertEquals(tags[0].title, tag.title)
		self.assertEquals(tags[0].slug, tag.slug)

class CategoryTest(TestCase):
	def test_CreateCategory(self):

		category = CategoryFactory()

		categories = Category.objects.all()
		self.assertEquals(len(categories),1)
		self.assertEquals(categories[0].title, "Test Category")
		self.assertEquals(categories[0].slug, "test-category")