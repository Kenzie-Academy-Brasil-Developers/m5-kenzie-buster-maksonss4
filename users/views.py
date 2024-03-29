from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrAdmin


class UsersView(APIView):
    def get(self, req: Request) -> Response:
        accounts = User.objects.all()
        serializer = UserSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(
            User,
            id=user_id,
        )

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, req: Request, user_id: int) -> Response:
        user_obj = get_object_or_404(User, pk=user_id)

        self.check_object_permissions(req, user_obj)

        serializer = UserSerializer(user_obj)

        return Response(serializer.data, status.HTTP_200_OK)
