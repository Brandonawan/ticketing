from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_ticket", views.create_ticket, name="create_ticket"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("get_client_info/", views.get_client_info, name="get_client_info"),
]