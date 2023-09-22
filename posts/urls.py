from django.urls import path
from .views import post_create,feed, post_like


urlpatterns = [
    path('', post_create, name='post_create'),
    path('feed/', feed, name='feed'),
    path('like/', post_like, name='like'),
]