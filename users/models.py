"""Users models."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model."""
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='users/pictures',
                                        blank=True,
                                        null=True)

    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the username."""
        return self.username
