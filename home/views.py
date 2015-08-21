from django.shortcuts import render

def home(request):
	return render(request, "home/home.html", {})

def games(request):
	return render(request, "home/games.html", {})

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