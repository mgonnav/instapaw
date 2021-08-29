from django import forms

from .models import User


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(min_length=6,
                               max_length=70,
                               widget=forms.PasswordInput())
    password_confirmation = forms.CharField(min_length=6,
                                            max_length=70,
                                            widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.EmailField()

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in taken.')

        return username

    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()

        if email_taken:
            raise forms.ValidationError('Email is already in use.')

        return email

    def clean_password_confirmation(self):
        """Check passwords match."""
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if not password_confirmation:
            raise forms.ValidationError('You must confirm your password.')
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return password_confirmation

    def save(self):
        """Create user."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        user.save()


class UserForm(forms.ModelForm):
    """User form."""
    class Meta:
        model = User
        fields = [
            'username', 'email', 'website', 'biography', 'phone_number',
            'profile_picture', 'first_name', 'last_name'
        ]
