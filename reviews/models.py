from django.db import models
from traitlets import default
from django.core.validators import MaxValueValidator, MinValueValidator


class RecomendationChoices(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ]
    )
    review = models.TextField()
    spoilers = models.BooleanField(null=True, default=False)
    recomendation = models.CharField(
        max_length=50,
        null=True,
        choices=RecomendationChoices.choices,
        default=RecomendationChoices.DEFAULT,
    )

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    critic = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
