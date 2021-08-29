"""Users views."""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView

from posts.models import Post

# Forms
from .forms import SignupForm, UserForm
# Models
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'viewed_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created_on')
        return context


@login_required
def edit_profile(request):
    """Edit a user's profile view."""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:edit_profile')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)


def login_view(request):
    """Login view."""
    if request.user.is_authenticated:
        return redirect('posts:feed')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html',
                          {'error': 'Invalid credentials.'})

    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.user.is_authenticated:
        return redirect('posts:feed')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)


@login_required
def logout_view(request):
    """Log out view."""
    logout(request)
    return redirect('users:login')
