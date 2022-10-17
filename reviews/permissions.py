from rest_framework import permissions
from rest_framework.views import Request, View

from reviews.models import Review


class ReviewViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and (
            request.user.is_critic or request.user.is_superuser
        ):
            return True

    def has_object_permission(
        self, request: Request, view: View, review: Review
    ) -> bool:
        if request.user == review.critic or request.user.is_superuser:
            return True
