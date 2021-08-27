"""Users views."""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#Exceptions
from django.db.utils import IntegrityError
from django.shortcuts import redirect, render

# Models
from users.models import User


@login_required
def edit_profile(request):
    """Edit a user's profile view."""
    return render(request, 'users/edit_profile.html')


def login_view(request):
    """Login view."""
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',
                          {'error': 'Invalid credentials.'})

    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'users/signup.html',
                          {'error': 'Passwords do not match.'})

        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html',
                          {'error': 'That username is already taken.'})

        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            return render(request, 'users/signup.html',
                          {'error': 'That email is already taken.'})

        user = User.objects.createuser(username=username,
                                       email=email,
                                       password=password1)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Log out view."""
    logout(request)
    return redirect('login')
