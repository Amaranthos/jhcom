from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Game, App, Tool, Library, Site

def home(request):
	return render(request, "home/home.html", {})

def games(request):
	return render(request, "home/games.html", {
			"list" : Game.objects.all(),
		})

def game(request, id, slug):
	game = get_object_or_404(Game, pk=id)
	return render(request, "home/game.html", {'item' : game})

def apps(request):
	return render(request, "home/apps.html", {
			"list" : App.objects.all(),
		})

def app(request, id, slug):
	app = get_object_or_404(App, pk=id)
	return render(request, "home/app.html", {'item' : app})

def tools(request):
	return render(request, "home/tools.html", {
			"list" : Tool.objects.all(),
		})

def tool(request, id, slug):
	tool = get_object_or_404(Tool, pk=id)
	return render(request, "home/tool.html", {'item' : tool})

def libraries(request):
	return render(request, "home/libraries.html", {
			"list" : Library.objects.all(),
		})

def library(request, id, slug):
	library = get_object_or_404(Library, pk=id)
	return render(request, "home/library.html", {'item' : library})

def web(request):
	return render(request, "home/web.html", {
			"list" : Site.objects.all(),
		})

def art(request):
	return render(request, "home/art.html", {})
	