from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from django.utils.text import slugify

from .models import Game, App, Tool, Library, Site, Art, Tutorial, Contributor, Link

class AdminTest(LiveServerTestCase):
	fixtures = ['users.json']

	def setUp(self):
		self.client = Client()

	def test_Login(self):
		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)
		
		self.assertTrue(b"Log in" in response.content)

		self.client.login(username='josh', password='123')

		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)

		self.assertTrue(b"Log out" in response.content)

	def test_Logout(self):
		self.client.login(username='josh', password='123')

		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)

		self.assertTrue(b"Log out" in response.content)

		self.client.logout()

		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)

		self.assertTrue(b"Log in" in response.content)

class GameTest(TestCase):
	def test_CreateGame(self):
		
		game = Game()
		game.title = "Test Game"
		game.slug = slugify(game.title)
		game.video = "#"
		game.description = "Desc text."

		game.posted = timezone.now()
		
		game.save()

		games = Game.objects.all()
		self.assertEquals(len(games),1)
		self.assertEquals(games[0], game)

		self.assertEquals(games[0].title, "Test Game")
		self.assertEquals(games[0].slug, "test-game")
		self.assertEquals(games[0].video, "#")
		self.assertEquals(games[0].description, "Desc text.")
		self.assertEquals(games[0].posted.year, game.posted.year)
		self.assertEquals(games[0].posted.month, game.posted.month)
		self.assertEquals(games[0].posted.day, game.posted.day)

class AppTest(TestCase):
	def test_CreateApp(self):
		
		app = App()
		app.title = "Test App"
		app.slug = slugify(app.title)
		app.video = "#"
		app.description = "Desc text."

		app.posted = timezone.now()
		
		app.save()

		apps = App.objects.all()
		self.assertEquals(len(apps),1)
		self.assertEquals(apps[0], app)

		self.assertEquals(apps[0].title, "Test App")
		self.assertEquals(apps[0].slug, "test-app")
		self.assertEquals(apps[0].video, "#")
		self.assertEquals(apps[0].description, "Desc text.")
		self.assertEquals(apps[0].posted.year, app.posted.year)
		self.assertEquals(apps[0].posted.month, app.posted.month)
		self.assertEquals(apps[0].posted.day, app.posted.day)

class ToolTest(TestCase):
	def test_CreateTool(self):
		
		tool = Tool()
		tool.title = "Test Tool"
		tool.slug = slugify(tool.title)
		tool.video = "#"
		tool.description = "Desc text."

		tool.posted = timezone.now()
		
		tool.save()

		tools = Tool.objects.all()
		self.assertEquals(len(tools),1)
		self.assertEquals(tools[0], tool)

		self.assertEquals(tools[0].title, "Test Tool")
		self.assertEquals(tools[0].slug, "test-tool")
		self.assertEquals(tools[0].video, "#")
		self.assertEquals(tools[0].description, "Desc text.")
		self.assertEquals(tools[0].posted.year, tool.posted.year)
		self.assertEquals(tools[0].posted.month, tool.posted.month)
		self.assertEquals(tools[0].posted.day, tool.posted.day)

class LibraryTest(TestCase):
	def test_CreateLibrary(self):
		
		library = Library()
		library.title = "Test Library"
		library.slug = slugify(library.title)
		library.description = "Desc text."

		library.posted = timezone.now()
		
		library.save()

		libraries = Library.objects.all()
		self.assertEquals(len(libraries),1)
		self.assertEquals(libraries[0], library)

		self.assertEquals(libraries[0].title, "Test Library")
		self.assertEquals(libraries[0].slug, "test-library")
		self.assertEquals(libraries[0].description, "Desc text.")
		self.assertEquals(libraries[0].posted.year, library.posted.year)
		self.assertEquals(libraries[0].posted.month, library.posted.month)
		self.assertEquals(libraries[0].posted.day, library.posted.day)

class SiteTest(TestCase):
	def test_CreateSite(self):
		
		site = Site()
		site.title = "Test Site"

		site.save()

		sites = Site.objects.all()
		self.assertEquals(len(sites),1)
		self.assertEquals(sites[0], site)

		self.assertEquals(sites[0].title, "Test Site")

class ArtTest(TestCase):
	def test_CreateArt(self):

		art = Art()
		art.title = "Test Art"

		art.save()
		artwork = Art.objects.all()
		self.assertEquals(len(artwork),1)
		self.assertEquals(artwork[0], art)
		self.assertEquals(artwork[0].title, "Test Art")

class TutorialTest(TestCase):
	def test_CreateTutorial(self):
		
		tutorial = Tutorial()
		tutorial.title = "Test Tutorial"
		tutorial.slug = slugify(tutorial.title)

		tutorial.save()

		tutorials = Tutorial.objects.all()
		self.assertEquals(len(tutorials),1)
		self.assertEquals(tutorials[0], tutorial)

		self.assertEquals(tutorials[0].title, "Test Tutorial")
		self.assertEquals(tutorials[0].slug, "test-tutorial")

class ContributorTest(TestCase):
	def test_CreateContributor(self):
		
		contributor = Contributor()
		contributor.name = "Test Contributor"

		contributor.save()

		contributors = Contributor.objects.all()
		self.assertEquals(len(contributors),1)
		self.assertEquals(contributors[0], contributor)

		self.assertEquals(contributors[0].name, "Test Contributor")

class LinkTest(TestCase):
	def test_CreateLink(self):
		
		link = Link()
		link.name = "Test Link"

		link.save()

		links = Link.objects.all()
		self.assertEquals(len(links),1)
		self.assertEquals(links[0], link)

		self.assertEquals(links[0].name, "Test Link")
