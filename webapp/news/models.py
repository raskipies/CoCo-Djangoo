from django.db import models
from django.contrib.auth.models import User
from main.models import Game

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Article title', max_length=100, null=False, blank=False)
    excerpt = models.CharField('Article excerpt', max_length=250, null=False, blank=False)
    body = models.TextField('Article body', null=False, blank=True)
    published_at = models.DateTimeField('Article published at', null=False, blank=False)

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Bug(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bugs')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reported_bugs')
    content = models.TextField()
    image = models.ImageField(upload_to='bugs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bug in {self.game.title} by {self.author.username}"
    


class BugComment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.bug.id}"