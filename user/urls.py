from django.urls import path
from .views import createP_list, login_list

urlpatterns = [
    path("create_profile/", createP_list, name='createP_list'),
    path("login/", login_list, name="login_list"),
]