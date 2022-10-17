from django.urls import path

from . import views as ReviewViews

urlpatterns = [
    path(
        "movies/<int:movie_id>/reviews/",
        ReviewViews.MovieReviewView.as_view(),
    ),
    path(
        "movies/<int:movie_id>/reviews/<int:review_id>",
        ReviewViews.MovieDetailReviewView.as_view(),
    ),
]
