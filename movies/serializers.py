from rest_framework import serializers
from .models import Ratings, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        choices=Ratings.choices,
        default=Ratings.GENERAL_AUDIENCES,
    )
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie) -> str:
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: MovieOrder) -> str:
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder) -> str:
        return obj.user.email

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
