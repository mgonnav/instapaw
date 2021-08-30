"""Posts views."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

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
