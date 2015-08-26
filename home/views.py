from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Game, App, Tool, Library, Site

def home(request):
	return render(request, "home/home.html", {})

def games(request):
	list = Game.objects.order_by("title")
	return render(request, "home/games.html", {
			"list" : list,
		})

def game(request, id):
	game = get_object_or_404(Game, pk=id)
	return render(request, "home/game.html", {'item' : game})

def apps(request):
	list = App.objects.order_by("title")
	return render(request, "home/apps.html", {
			"list" : list,
		})

def app(request, id):
	app = get_object_or_404(App, pk=id)
	return render(request, "home/app.html", {'item' : app})

def tools(request):
	list = Tool.objects.order_by("title")
	return render(request, "home/tools.html", {
			"list" : list,
		})

def tool(request, id):
	tool = get_object_or_404(Tool, pk=id)
	return render(request, "home/tool.html", {'item' : tool})

def libraries(request):
	list = Library.objects.order_by("title")
	return render(request, "home/libraries.html", {
			"list" : list,
		})

def library(request, id):
	library = get_object_or_404(Library, pk=id)
	return render(request, "home/library.html", {'item' : library})

def web(request):
	list = Site.objects.order_by("title")
	return render(request, "home/web.html", {
			"list" : list,
		})

def art(request):
	return render(request, "home/art.html", {})