"""Users views."""

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, FormView, UpdateView

from posts.models import Post

# Decorators
from .decorators import login_excluded
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


@method_decorator(login_excluded('posts:feed'), name='dispatch')
class SignupView(FormView):
    """Signup view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    redirect_authenticated_user = True

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


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    pass
