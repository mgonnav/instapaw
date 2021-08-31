"""Posts forms module."""

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Posts model form."""
    class Meta:
        """Form settings."""
        model = Post
        fields = ['user', 'title', 'picture']
