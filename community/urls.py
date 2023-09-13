from django.urls import path

from . import views

# URL conf
urlpatterns = [
    path('get-posts/', views.get_posts),
    path('create-post/', views.create_post),
]
