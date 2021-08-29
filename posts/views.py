"""Posts views."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Post

from .forms import PostForm


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = '-created_on'
    #  paginate_by = 2
    context_object_name = 'posts'


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'posts/create.html', context)
