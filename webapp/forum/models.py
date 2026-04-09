from django.db import models
from django.contrib.auth.models import User

# Community - posty
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Jeśli usunie się użytkownika to usunie automatycznie wszystkie jego posty
    content = models.TextField()
    image = models.FileField(upload_to='forum_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author.username}: {self.content[:50]}'

    def likes_count(self):
        return self.likes.count()

    def comments_count(self):
        return self.comments.count()

    def user_liked(self, user):
        if not user.is_authenticated:
            return False
        return self.likes.filter(user=user).exists()


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} likes post {self.post.id}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author.username} on post {self.post.id}: {self.content[:50]}'
