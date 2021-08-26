"""instapaw URLs Configuration."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.list_posts, name='feed'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
