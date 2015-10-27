from django.shortcuts import get_object_or_404, render
import datetime

from .models import Blog, Category, Tag
from calendar import month_name

def blog(request):

	posts = Blog.objects.dates('posted', 'month')
	dates = {}

	return render(request, "blog/home.html", {
			'categories' : Category.objects.all(),
			'tags' : Tag.objects.all(),
			'dates' : posts,
			'posts' : Blog.objects.all().order_by('-posted')[:5]
		})

def post(request, id, slug):
	return render(request, "blog/post.html", {'post' : get_object_or_404(Blog, pk=id)})

def dates(request, year, month):
	collection = Blog.objects.filter(posted__year=year, posted__month=month)
	return render(request, "blog/list.html", {
			'title' : month_name[int(month)] + ", " + year,
			'list' : collection,
			'posts' : collection
		})

def category(request, id, slug):
	category = get_object_or_404(Category, pk=id)
	return render(request, "blog/list.html", {
			'title' : category.title,
			'list' : category,
			'posts' : Blog.objects.filter(category=category)
		})

def tag(request, id, slug):
	tag = get_object_or_404(Tag, pk=id)
	return render(request, "blog/list.html", {
			'title' : tag.title,
			'list' : tag,
			'posts' : Blog.objects.filter(tags=tag)
		})