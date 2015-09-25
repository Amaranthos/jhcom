from django.core.urlresolvers import reverse
from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from django.utils.text import slugify

import factory

from .models import Blog, Category, Tag

# 	88888888888                                                 88                       
# 	88                              ,d                          ""                       
# 	88                              88                                                   
# 	88aaaaa ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba, 88  ,adPPYba, ,adPPYba,  
# 	88""""" ""     `Y8 a8"     ""   88   a8"     "8a 88P'   "Y8 88 a8P_____88 I8[    ""  
# 	88      ,adPPPPP88 8b           88   8b       d8 88         88 8PP"""""""  `"Y8ba,   
# 	88      88,    ,88 "8a,   ,aa   88,  "8a,   ,a8" 88         88 "8b,   ,aa aa    ]8I  
# 	88      `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'  88         88  `"Ybbd8"' `"YbbdP"'  

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

# 	88888888ba  88                            888888888888                          
# 	88      "8b 88                                 88                        ,d     
# 	88      ,8P 88                                 88                        88     
# 	88aaaaaa8P' 88  ,adPPYba,   ,adPPYb,d8         88  ,adPPYba, ,adPPYba, MM88MMM  
# 	88""""""8b, 88 a8"     "8a a8"    `Y88         88 a8P_____88 I8[    ""   88     
# 	88      `8b 88 8b       d8 8b       88         88 8PP"""""""  `"Y8ba,    88     
# 	88      a8P 88 "8a,   ,a8" "8a,   ,d88         88 "8b,   ,aa aa    ]8I   88,    
# 	88888888P"  88  `"YbbdP"'   `"YbbdP"Y8         88  `"Ybbd8"' `"YbbdP"'   "Y888  
# 	                            aa,    ,88                                          
# 	                             "Y8bbdP"                                           

class BlogTest(TestCase):
	def test_CreatePost(self):
		
		post = PostFactory()
		tag = TagFactory()

		post.tags.add(tag)
		
		posts = Blog.objects.all()
		self.assertEqual(len(posts),1)
		self.assertEqual(posts[0], post)

		self.assertEqual(posts[0].title, "Test Post")
		self.assertEqual(posts[0].slug, "test-post")
		self.assertEqual(posts[0].body, "Test content")
		self.assertEqual(posts[0].posted.year, post.posted.year)
		self.assertEqual(posts[0].posted.month, post.posted.month)
		self.assertEqual(posts[0].posted.day, post.posted.day)
		self.assertEqual(posts[0].category.title, 'Test Category')
		self.assertEqual(posts[0].category.slug, 'test-category')

		tags = posts[0].tags.all()
		self.assertEqual(len(tags), 1)
		self.assertEqual(tags[0], tag)
		self.assertEqual(tags[0].title, tag.title)
		self.assertEqual(tags[0].slug, tag.slug)

# 	  ,ad8888ba,                                                                                 888888888888                          
# 	 d8"'    `"8b              ,d                                                                     88                        ,d     
# 	d8'                        88                                                                     88                        88     
# 	88            ,adPPYYba, MM88MMM ,adPPYba,  ,adPPYb,d8  ,adPPYba,  8b,dPPYba, 8b       d8         88  ,adPPYba, ,adPPYba, MM88MMM  
# 	88            ""     `Y8   88   a8P_____88 a8"    `Y88 a8"     "8a 88P'   "Y8 `8b     d8'         88 a8P_____88 I8[    ""   88     
# 	Y8,           ,adPPPPP88   88   8PP""""""" 8b       88 8b       d8 88          `8b   d8'          88 8PP"""""""  `"Y8ba,    88     
# 	 Y8a.    .a8P 88,    ,88   88,  "8b,   ,aa "8a,   ,d88 "8a,   ,a8" 88           `8b,d8'           88 "8b,   ,aa aa    ]8I   88,    
# 	  `"Y8888Y"'  `"8bbdP"Y8   "Y888 `"Ybbd8"'  `"YbbdP"Y8  `"YbbdP"'  88             Y88'            88  `"Ybbd8"' `"YbbdP"'   "Y888  
# 	                                            aa,    ,88                            d8'                                              
# 	                                             "Y8bbdP"                            d8'                                               

class CategoryTest(TestCase):
	def test_CreateCategory(self):

		category = CategoryFactory()

		categories = Category.objects.all()
		self.assertEqual(len(categories),1)
		self.assertEqual(category, categories[0])
		self.assertEqual(categories[0].title, "Test Category")
		self.assertEqual(categories[0].slug, "test-category")

# 	888888888888                      888888888888                          
# 	     88                                88                        ,d     
# 	     88                                88                        88     
# 	     88 ,adPPYYba,  ,adPPYb,d8         88  ,adPPYba, ,adPPYba, MM88MMM  
# 	     88 ""     `Y8 a8"    `Y88         88 a8P_____88 I8[    ""   88     
# 	     88 ,adPPPPP88 8b       88         88 8PP"""""""  `"Y8ba,    88     
# 	     88 88,    ,88 "8a,   ,d88         88 "8b,   ,aa aa    ]8I   88,    
# 	     88 `"8bbdP"Y8  `"YbbdP"Y8         88  `"Ybbd8"' `"YbbdP"'   "Y888  
# 	                    aa,    ,88                                          
# 	                     "Y8bbdP"                                           

class TagTest(TestCase):
	def test_CreateTag(self):
		tag = TagFactory()

		tags = Tag.objects.all()
		self.assertEqual(len(tags), 1)
		self.assertEqual(tag, tags[0])
		self.assertEqual(tags[0].title, "Test Tag")
		self.assertEqual(tags[0].slug, "test-tag")

# 	       db                88                    88                888888888888                                    
# 	      d88b               88                    ""                     88                        ,d               
# 	     d8'`8b              88                                           88                        88               
# 	    d8'  `8b     ,adPPYb,88 88,dPYba,,adPYba,  88 8b,dPPYba,          88  ,adPPYba, ,adPPYba, MM88MMM ,adPPYba,  
# 	   d8YaaaaY8b   a8"    `Y88 88P'   "88"    "8a 88 88P'   `"8a         88 a8P_____88 I8[    ""   88    I8[    ""  
# 	  d8""""""""8b  8b       88 88      88      88 88 88       88         88 8PP"""""""  `"Y8ba,    88     `"Y8ba,   
# 	 d8'        `8b "8a,   ,d88 88      88      88 88 88       88         88 "8b,   ,aa aa    ]8I   88,   aa    ]8I  
# 	d8'          `8b `"8bbdP"Y8 88      88      88 88 88       88         88  `"Ybbd8"' `"YbbdP"'   "Y888 `"YbbdP"'  

class AdminTest(BaseAcceptanceTest):
	fixtures = ['users.json']

	def test_Login(self):
		response = self.client.get('/admin/', follow=True)
		self.assertEqual(response.status_code, 200)		
		self.assertTrue('Log in' in response.content.decode('utf-8'))

		self.client.login(username='josh', password='123')

		response = self.client.get('/admin/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('Log out' in response.content.decode('utf-8'))

	def test_Logout(self):
		self.client.login(username='josh', password='123')

		response = self.client.get('/admin/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('Log out' in response.content.decode('utf-8'))

		self.client.logout()

		response = self.client.get('/admin/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('Log in' in response.content.decode('utf-8'))

# Categories

	def test_CreateCategory(self):
		self.client.login(username="josh", password="123")

		response = self.client.get('/admin/blog/category/add/', follow=True)
		self.assertEqual(response.status_code, 200)

		response = self.client.post('/admin/blog/category/add/', {
				'title' : 'Test Category',
				'slug' : 'test-category',
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('added successfully' in response.content.decode('utf-8'))

		categories = Category.objects.all()
		self.assertEqual(len(categories),1)

	def test_EditCategory(self):
		category = CategoryFactory()

		self.client.login(username="josh", password="123")

		response = self.client.post('/admin/blog/category/' + str(category.pk)+'/', {
				'title': 'Edited Category',
				'slug': 'edited-category',
			}, follow=True)
		
		self.assertEqual(response.status_code, 200)
		self.assertTrue('changed successfully' in response.content.decode('utf-8'))

		categories = Category.objects.all()
		self.assertEqual(len(categories),1)
		self.assertEqual(categories[0].title, 'Edited Category')
		self.assertEqual(categories[0].slug, 'edited-category')

	def test_DeleteCategory(self):
		category = CategoryFactory()

		categories = Category.objects.all()
		self.assertEqual(len(categories), 1)

		self.client.login(username="josh", password="123")
		
		response = self.client.post('/admin/blog/category/' + str(category.pk)+'/delete/', {
				'post': 'yes',
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('deleted successfully' in response.content.decode('utf-8'))

		categories = Category.objects.all()
		self.assertEqual(len(categories), 0)
		
# Tags

	def test_CreateTag(self):
		self.client.login(username="josh", password="123")

		response = self.client.get('/admin/blog/tag/add', follow=True)
		self.assertEqual(response.status_code, 200)

		response = self.client.post('/admin/blog/tag/add/', {
				'title':'Test Tag',
				'slug' : 'test-tag',
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('added successfully' in response.content.decode('utf-8'))

		tags = Tag.objects.all()
		self.assertEqual(len(tags),1)

	def test_EditTag(self):
		tag = TagFactory()

		self.client.login(username="josh", password="123")

		response = self.client.post('/admin/blog/tag/' + str(tag.pk) + '/', {
				'title': 'Edited Tag',
				'slug': 'edited-tag',
			}, follow=True)
		
		self.assertEqual(response.status_code, 200)
		self.assertTrue('changed successfully' in response.content.decode('utf-8'))

		tags = Tag.objects.all()
		self.assertEqual(len(tags), 1)
		self.assertEqual(tags[0].title, 'Edited Tag')
		self.assertEqual(tags[0].slug, 'edited-tag')

	def test_DeleteTag(self):
		tag = TagFactory()

		tags = Tag.objects.all()
		self.assertEqual(len(tags),1)

		self.client.login(username="josh", password="123")

		response = self.client.post('/admin/blog/tag/' + str(tag.pk) + '/delete/', {
				'post' : 'yes',
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('deleted successfully' in response.content.decode('utf-8'))

		tags = Tag.objects.all()
		self.assertEqual(len(tags), 0)

# Posts

	def test_CreatePost(self):
		category = CategoryFactory()
		tag = TagFactory()

		self.client.login(username="josh", password="123")

		response = self.client.get('/admin/blog/blog/add/', follow=True)
		self.assertEqual(response.status_code, 200)

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

	def test_CreatePostWithoutTag(self):
		category = CategoryFactory()

		self.client.login(username="josh", password="123")

		response = self.client.get('/admin/blog/blog/add/', follow=True)
		self.assertEqual(response.status_code, 200)

		response = self.client.post('/admin/blog/blog/add/', {
				'title' : 'Test Post no tags',
				'slug' : 'test-post-no-tags',
				'body' : 'Test content',
				'posted' : '2015-09-24',
				'category' : str(category.pk),
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('added successfully' in response.content.decode('utf-8'))

		posts = Blog.objects.all()
		self.assertEqual(len(posts), 1)

	def test_EditPost(self):
		post = PostFactory()
		category = CategoryFactory()

		tag = TagFactory()
		post.tags.add(tag)

		self.client.login(username="josh", password="123")

		response = self.client.post('/admin/blog/blog/' + str(post.pk) + '/', {
				'title' : 'Edited Post',
				'slug' : 'edited-post',
				'body' : 'Edited Content',
				'posted' : '2015-09-24',
				'category' : str(category.pk),
				'tags' : str(tag.pk),
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('changed successfully' in response.content.decode('utf-8'))

		posts = Blog.objects.all()
		self.assertEqual(len(posts), 1)
		self.assertEqual(posts[0].title, "Edited Post")
		self.assertEqual(posts[0].body, "Edited Content")

	def test_DeletePost(self):
		post = PostFactory()

		posts = Blog.objects.all()
		self.assertEqual(len(posts), 1)

		self.client.login(username="josh", password="123")

		response = self.client.post('/admin/blog/blog/' + str(post.pk) + '/delete/', {
				'post':'yes',
			}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertTrue('deleted successfully' in response.content.decode('utf-8'))

		posts = Blog.objects.all()
		self.assertEqual(len(posts), 0)

# 	8b           d8 88                                  888888888888                          
# 	`8b         d8' ""                                       88                        ,d     
# 	 `8b       d8'                                           88                        88     
# 	  `8b     d8'   88  ,adPPYba, 8b      db      d8         88  ,adPPYba, ,adPPYba, MM88MMM  
# 	   `8b   d8'    88 a8P_____88 `8b    d88b    d8'         88 a8P_____88 I8[    ""   88     
# 	    `8b d8'     88 8PP"""""""  `8b  d8'`8b  d8'          88 8PP"""""""  `"Y8ba,    88     
# 	     `888'      88 "8b,   ,aa   `8bd8'  `8bd8'           88 "8b,   ,aa aa    ]8I   88,    
# 	      `8'       88  `"Ybbd8"'     YP      YP             88  `"Ybbd8"' `"YbbdP"'   "Y888  

class ViewTest(BaseAcceptanceTest):
	def test_BlogHome(self):
		post = PostFactory(body="Test Content")

		tag = TagFactory(title="Test Tag")
		post.tags.add(tag)

		posts = Blog.objects.all()
		self.assertEqual(len(posts), 1)

		response = self.client.get(reverse('blog'))
		self.assertTrue(response.status_code, 200)

		self.assertTrue(post.title in response.content.decode('utf-8'))
		
