from django.urls import path

from . import views as MovieViews

urlpatterns = [
    path("movies/", MovieViews.MovieView.as_view()),
    path(
        "movies/<int:movie_id>/",
        MovieViews.MovieDetailView.as_view(),
    ),
]
