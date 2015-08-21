from django.contrib import admin

from .models import Game

class GameAdmin(admin.ModelAdmin):

	class Meta:
		model = Game

admin.site.register(Game, GameAdmin)