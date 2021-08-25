"""Posts models."""

from django.db import models

from users.models import User


class Post(models.Model):
    """Post model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='posts/pictures')

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns title and the owner's username."""
        return f'{self.title} by @{self.user.username}'
