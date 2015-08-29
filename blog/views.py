from django.shortcuts import get_object_or_404,render

from .models import Blog, Category

def blog(request):
	return render(request, "blog/home.html", {
			'categories' : Category.objects.all(),
			'posts' : Blog.objects.all().order_by('posted')[:5]
		})

def post(request, id, slug):
	return render(request, "blog/post.html", {'post' : get_object_or_404(Blog, pk=id)})

def category(request, id, slug):
	category = get_object_or_404(Category, pk=id)
	return render(request, "blog/list.html", {
			'list' : category,
			'posts' : Blog.objects.filter(category=category)
		})