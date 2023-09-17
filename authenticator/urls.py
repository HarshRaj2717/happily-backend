from django.urls import path

from . import views

# URL conf
urlpatterns = [
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('<str:user_key>/verify-psychologist/', views.verify_psychologist),
    path('<str:user_key>/verify-psychiatrist/', views.verify_psychiatrist),
    path('<str:user_key>/verify-ngo/', views.verify_ngo),
]
