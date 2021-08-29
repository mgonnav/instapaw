"""Users views."""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Models
from users.models import User

# Froms
from .forms import UserForm


@login_required
def edit_profile(request):
    """Edit a user's profile view."""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user

            user.username = data['username']
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.website = data['website']
            user.biography = data['biography']
            user.phone_number = data['phone_number']
            user.profile_picture = data['profile_picture']

            user.save()
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

        user = User.objects.create_user(username=username,
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
