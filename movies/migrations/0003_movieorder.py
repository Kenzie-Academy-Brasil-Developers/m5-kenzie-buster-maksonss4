# Generated by Django 4.1.4 on 2022-12-13 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0002_alter_movie_rating"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buyed_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.FloatField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movie_orders",
                        to="movies.movie",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_movies_orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]