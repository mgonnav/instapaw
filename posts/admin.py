"""Post admin classes."""

from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'user', 'last_modified')

    search_fields = ('title', 'user__username')


admin.site.register(Post, PostAdmin)
