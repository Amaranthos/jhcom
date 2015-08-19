from django.shortcuts import render

def home(request):
	return render(request, "home/home.html", {})

def games(request):
	return render(request, "home/games.html", {})