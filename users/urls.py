"""Users URLs."""

from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('update/', views.UpdateUserView.as_view(), name='update'),
    path('<str:username>/', views.UserDetailView.as_view(template_name='users/detail.html'), name='detail'),
]
