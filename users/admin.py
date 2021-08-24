"""User admin classes."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('pk', 'username', 'phone_number', 'website',
                    'profile_picture')
    list_display_links = ('pk', 'username')
    list_editable = ('phone_number', 'website', 'profile_picture')

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'website', 'biography',
                       'phone_number', 'profile_picture')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = ((None, {
        'fields': ('username', 'email', 'password1', 'password2', 'website',
                   'biography', 'phone_number', 'profile_picture')
    }), )

    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
        'phone_number',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'date_joined',
        'last_modified',
    )


admin.site.register(User, UserAdmin)
