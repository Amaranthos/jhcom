from pagedown.widgets import AdminPagedownWidget
from django.db import models
from django.contrib import admin

from .models import Game, App, Tool, Library, Website, Contributor, Link

class GameAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	prepopulated_fields = {'slug' : ('title',)}
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget },
	}
	class Meta:
		model = Game

class AppAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	prepopulated_fields = {'slug' : ('title',)}
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget },
	}
	class Meta:
		model = App

class ToolAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	prepopulated_fields = {'slug' : ('title',)}
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget },
	}
	class Meta:
		model = Tool

class LibraryAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	prepopulated_fields = {'slug' : ('title',)}
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget },
	}
	class Meta:
		model = Library

class WebsiteAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	class Meta:
		model = Website

class ContributorAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Contributor

class LinkAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Link

admin.site.register(Game, GameAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Link, LinkAdmin)