from django.urls import path

from . import views

# URL conf
urlpatterns = [
    path('', views.scales),
    path('gidyq-aa-female/', views.gidyq_aa_female),
    path('gidyq-aa-male/', views.gidyq_aa_male),
]
