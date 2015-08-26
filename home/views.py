from django.shortcuts import render
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
	return render(request, "home/game.html", {})

def apps(request):
	list = App.objects.order_by("title")
	return render(request, "home/apps.html", {
			"list" : list,
		})

def app(request, id):
	return render(request, "home/app.html", {})

def tools(request):
	list = Tool.objects.order_by("title")
	return render(request, "home/tools.html", {
			"list" : list,
		})

def libraries(request):
	list = Library.objects.order_by("title")
	return render(request, "home/libraries.html", {
			"list" : list,
		})

def web(request):
	list = Site.objects.order_by("title")
	return render(request, "home/web.html", {
			"list" : list,
		})

def art(request):
	return render(request, "home/art.html", {})