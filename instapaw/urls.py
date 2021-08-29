"""instapaw URLs Configuration."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # posts views
    path('', include(('posts.urls', 'posts'), namespace='posts')),

    # users views
    path('accounts/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
