from django.urls import path

from . import views

# URL conf
urlpatterns = [
    path('get-posts/', views.get_posts),
    path('get-comments/<int:post_id>', views.get_comments),
    path('<str:user_key>/create-post/', views.create_post),
    path('<str:user_key>/delete-post/<int:post_id>', views.delete_post),
    path('<str:user_key>/create-comment/<int:post_id>', views.add_comment),
    path('<str:user_key>/delete-comment/<int:post_id>/<int:comment_id>', views.delete_comment),
    path('<str:user_key>/upvote-post/<int:post_id>', views.upvote_post),
    path('<str:user_key>/downvote-post/<int:post_id>', views.downvote_post),
]
