from django.urls import path
from . import views

app_mame = 'team'

urlpatterns = [
    path("", views.singin, name="login"),
    path("registration/", views.registration_team, name="registration_team"),
    path("home/", views.home, name="home"),
    path("add_user/", views.add_user, name="add_user"),
    path("logout/", views.log_out, name="log_out"),
    path("home/view_user_clients/<int:id>/", views.view_user_clients, name="view_user_clients"),
]


