from django.contrib import admin
from .models import Game

# modele


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'is_featured', 'is_active', 'created_at')
	list_filter = ('is_featured', 'is_active', 'created_at')
	search_fields = ('title', 'slug', 'short_description')
	prepopulated_fields = {'slug': ('title',)}
	list_editable = ('is_featured', 'is_active')
