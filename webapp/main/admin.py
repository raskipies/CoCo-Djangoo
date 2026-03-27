from django.contrib import admin
from .models import Game, Purchase

# modele


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'is_featured', 'is_default_library', 'is_active', 'created_at')
	list_filter = ('is_featured', 'is_default_library', 'is_active', 'created_at')
	search_fields = ('title', 'slug', 'short_description')
	prepopulated_fields = {'slug': ('title',)}
	list_editable = ('is_featured', 'is_default_library', 'is_active')
	fieldsets = (
		('Dane Gry', {
			'fields': ('title', 'slug', 'short_description', 'price', 'image')
		}),
		('Status', {
			'fields': ('is_featured', 'is_default_library', 'is_active')
		}),
	)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
	list_display = ('user', 'game', 'purchased_at')
	list_filter = ('purchased_at', 'user')
	search_fields = ('user__username', 'game__title')
	readonly_fields = ('purchased_at',)

