from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
        max_length=20,
    )
    email = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
        max_length=127,
    )
    birthdate = serializers.DateField(
        allow_null=True,
        default=None,
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    password = serializers.CharField(
        write_only=True,
        max_length=50,
    )

    # recipes = RecipeSerializer(
    #     many=True,
    #     read_only=True,
    # )

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
