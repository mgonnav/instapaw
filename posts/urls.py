"""Posts URLs module."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create_post'),
    path('posts/<int:post_id>/',
         views.ShowPostView.as_view(),
         name='show_post'),
]
