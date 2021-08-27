"""instapaw URLs Configuration."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # posts views
    path('', posts_views.list_posts, name='feed'),

    # users views
    path('accounts/', include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
