"""Posts views."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import PostForm


@login_required
def list_posts(request):
    posts = Post.objects.order_by('-created_on').all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/feed.html', context)

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('feed')
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)
