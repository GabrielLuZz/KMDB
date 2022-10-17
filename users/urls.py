from django.urls import path
from rest_framework.authtoken import views as AuthViews

from . import views as UsersViews

urlpatterns = [
    path(
        "users/",
        UsersViews.UsersGetView.as_view(),
    ),
    path(
        "users/<int:user_id>/",
        UsersViews.UserGetView.as_view(),
    ),
    path(
        "users/register/",
        UsersViews.UserRegisterView.as_view(),
    ),
    path(
        "users/login/",
        AuthViews.obtain_auth_token,
    ),
]
