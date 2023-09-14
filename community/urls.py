from django.urls import path

from . import views

# URL conf
urlpatterns = [
    path('get-posts/', views.get_posts),
    path('get-posts/<int:post_id>', views.get_specific_post),
    path('<str:user_key>/create-post/', views.create_post),
    path('<str:user_key>/upvote-post/<int:post_id>', views.upvote_post),
    path('<str:user_key>/downvote-post/<int:post_id>', views.downvote_post),
]
