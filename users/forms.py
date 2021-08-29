from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):
    """User form."""
    class Meta:
        model = User
        fields = [
            'username', 'email', 'website', 'biography', 'phone_number',
            'profile_picture', 'first_name', 'last_name'
        ]
