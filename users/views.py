from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from users.serializers import UserSerializer

from .models import User

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAdminUser

from .permissions import MyCustomPermission


class UsersGetView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        result_page = self.paginate_queryset(users, request, view=self)
        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class UserGetView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserRegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
