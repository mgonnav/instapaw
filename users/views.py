"""Users views."""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

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
        context['posts'] = Post.objects.filter(
            user=user).order_by('-created_on')
        return context


class SignupView(FormView):
    """Signup view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """Update user view."""

    template_name = 'users/update.html'
    model = User
    form_class = UserForm
    context_object_name = 'other_user'

    def get_object(self):
        """Return user."""
        return self.request.user

    def get_success_url(self):
        """Return to user's detail page."""
        context = {'username': self.request.user.username}
        return reverse_lazy('users:detail', kwargs=context)


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


@login_required
def logout_view(request):
    """Log out view."""
    logout(request)
    return redirect('users:login')
