"""Posts views."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post


@login_required
def list_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/feed.html', context)
