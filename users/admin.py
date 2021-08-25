"""User admin classes."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('pk', 'username', 'phone_number', 'website',
                    'profile_picture', 'is_active', 'is_staff')
    list_display_links = ('pk', 'username')
    list_editable = ('phone_number', 'website', 'profile_picture')

    fieldsets = (
        (_('Login info'), {
            'fields': ('username', 'email', 'password')
        }),
        (_('Profile'), {
            'fields': (
                ('first_name', 'last_name'),
                ('phone_number', 'website'), 
                'biography',
                'profile_picture'
            )
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': (
                ('last_login', 'date_joined'),
            )
        }),
        (_('Metadata'), {
            'fields': ('last_modified',)
        })
    )

    add_fieldsets = (
        (_('Login info'), {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
        (_('Profile'), {
            'fields': (
                ('first_name', 'last_name'),
                ('phone_number', 'website'),
                'biography',
                'profile_picture'
            )
        }),
    )

    readonly_fields = ('last_login', 'date_joined', 'last_modified')

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
