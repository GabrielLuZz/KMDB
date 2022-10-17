from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        if request.user.is_critic and request.user == user.id:
            return True
