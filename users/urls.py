"""Users URLs."""

from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.UserDetailView.as_view(template_name='users/detail.html'), name='detail'),
]
