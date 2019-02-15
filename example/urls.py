from django.urls import path
from example.views import user_list, log_in, log_out, sign_up


urlpatterns = [
    path(r'', user_list, name='user_list'),
    path(r'log_in/', log_in, name='log_in'),
    path(r'log_out/', log_out, name='log_out'),
    path(r'sign_up/', sign_up, name='sign_up'),
]