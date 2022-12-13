from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrReadOnly
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class MoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    page_size = 2

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, req)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)

        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(
            Movie,
            pk=movie_id,
        )

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(
            Movie,
            id=movie_id,
        )

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            movie=movie_obj,
            user=req.user,
        )

        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )
