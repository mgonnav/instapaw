"""instapaw URLs Configuration."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', posts_views.list_posts, name='feed'),

    path('accounts/login/', users_views.login_view, name='login'),
    path('accounts/logout/', users_views.logout_view, name='logout'),
    path('accounts/signup/', users_views.signup, name='signup'),
    path('accounts/edit/', users_views.edit_profile, name='edit_profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
