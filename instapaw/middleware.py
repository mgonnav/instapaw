"""Instapaw middlewares."""

from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure that every user that is interacting with the platform has
    their profile picture and biography.
    """
    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Validation to be executed on each request before
        the view is called."""

        user = request.user
        if not user.is_anonymous:
            if not user.profile_picture or not user.biography:
                exempt_urls = map(reverse, ['edit_profile', 'logout'])
                if request.path not in exempt_urls:
                    return redirect('edit_profile')

        response = self.get_response(request)
        return response
