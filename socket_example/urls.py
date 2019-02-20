from django.urls import path
from socket_example.views import user_list, log_in, log_out, sign_up
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    # path(r'', user_list, name='user_list'),
    path(r'log_in/', log_in, name='log_in'),
    path(r'log_out/', log_out, name='log_out'),
    path(r'sign_up/', sign_up, name='sign_up'),
]
