from django.contrib import admin

from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'posted']
	# prepopulated_fields = {'slug' : ('title',)}
	class Meta:
		model = Blog

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title']
	# prepopulated_fields = {'slug' : ('title',)}
	class Meta:
		model = Category		

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)