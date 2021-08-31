"""Posts views."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm
from .models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = '-created_on'
    paginate_by = 2
    context_object_name = 'posts'


class ShowPostView(LoginRequiredMixin, DetailView):
    """Return the details of a specific post."""

    template_name = 'posts/post.html'
    model = Post
    slug_field = 'pk'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post view."""

    template_name = 'posts/create.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
