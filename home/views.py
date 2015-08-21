from django.shortcuts import render
from django.http import HttpResponse

from .models import Game

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
	return render(request, "home/apps.html", {})

def tools(request):
	return render(request, "home/tools.html", {})

def libraries(request):
	return render(request, "home/libraries.html", {})

def web(request):
	return render(request, "home/web.html", {})

def art(request):
	return render(request, "home/art.html", {})