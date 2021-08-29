"""Users views."""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Forms
from .forms import UserForm, SignupForm


@login_required
def edit_profile(request):
    """Edit a user's profile view."""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'users/edit_profile.html', context)


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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)


@login_required
def logout_view(request):
    """Log out view."""
    logout(request)
    return redirect('login')
