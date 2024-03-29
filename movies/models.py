from django.db import models


class Ratings(models.TextChoices):
    GENERAL_AUDIENCES = "G"
    PARENTAL_GUIDANCE_SUGGESTED = "PG"
    PARENTS_STRONGLY_CAUTIONED = "PG-13"
    RESTRICTED = "R"
    ADULTS_ONLY = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10,
        null=True,
        default=None,
    )
    rating = models.CharField(
        max_length=20,
        choices=Ratings.choices,
        default=Ratings.GENERAL_AUDIENCES,
    )
    synopsis = models.TextField(
        null=True,
        default=None,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_orders",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movies_orders",
    )

    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
