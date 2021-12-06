from django.contrib.auth import views as auth_views #import this

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('explore', views.explore, name="explore"),
    path('upload', views.upload, name="upload"),
    path('delete/<int:post_id>/', views.posts_delete, name='delete_post'),
    path('profile/<str:username>/', views.user, name='User-profile'),
]