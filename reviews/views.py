from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from reviews.models import Review
from rest_framework.authentication import TokenAuthentication
from reviews.permissions import ReviewViewPermission

from reviews.serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination


class MovieReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewViewPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        get_object_or_404(Movie, id=movie_id)

        reviews = Review.objects.filter(movie_id=movie_id)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = Review.objects.filter(
            movie_id=movie.id,
            critic=request.user.id,
        )
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if len(reviews) > 0:
            return Response({"detail": "Review already exists."})

        serializer.save(critic=request.user, movie=movie)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewViewPermission]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete(
        self,
        request: Request,
        movie_id: int,
        review_id: int,
    ) -> Response:
        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        self.check_object_permissions(request, review)

        review.delete()

        return Response(status.HTTP_204_NO_CONTENT)
