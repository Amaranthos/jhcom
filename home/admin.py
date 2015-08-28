from django.contrib import admin

from .models import Game, App, Tool, Library, Site, Contributor, Link

class GameAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	class Meta:
		model = Game

class AppAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	class Meta:
		model = App

class ToolAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	class Meta:
		model = Tool

class LibraryAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	class Meta:
		model = Library

class SiteAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	class Meta:
		model = Site

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
admin.site.register(Site, SiteAdmin)
admin.site.register(Link, LinkAdmin)