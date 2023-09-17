from django.urls import path

from . import views

# URL conf
urlpatterns = [
    # TODO make doctor available ????
    path('get-profs/', views.get_professionals),
    path('<str:user_key>/book/<int:prof_id>/', views.book_appointment),
    path('<str:user_key>/pay/<int:appointment_id>/', views.pay_appointment),
    path('<str:user_key>/chat/', views.all_chats),
    path('<str:user_key>/chat/<int:prof_id>/', views.chat),
    path('<str:user_key>/chat/<int:prof_id>/', views.chat),
]
