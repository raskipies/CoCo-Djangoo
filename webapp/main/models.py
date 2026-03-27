from django.db import models
from django.contrib.auth.models import User

# modele, wersja beta, do zmienay przez Patrycje, przyklad pól dla gry



class Game(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=220, unique=True)
	short_description = models.TextField(max_length=500)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='games/', blank=True, null=True)
	is_featured = models.BooleanField(default=False)
	is_default_library = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title


class Purchase(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	purchased_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'game')
		ordering = ['-purchased_at']

	def __str__(self):
		return f"{self.user.username} - {self.game.title}"
