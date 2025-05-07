from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from api.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    LogoutSerializer,
)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        access_age = int(jwt_settings.ACCESS_TOKEN_LIFETIME.total_seconds())
        refresh_age = int(jwt_settings.REFRESH_TOKEN_LIFETIME.total_seconds())
        resp = Response(
            {
                "access": access_token,
                "refresh": refresh_token,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_201_CREATED,
        )
        resp.set_cookie(
            "accessToken",
            access_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=access_age,
        )
        resp.set_cookie(
            "refreshToken",
            refresh_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=refresh_age,
        )

        return resp

    def perform_create(self, serializer):
        return serializer.save()


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        access_age = int(jwt_settings.ACCESS_TOKEN_LIFETIME.total_seconds())
        refresh_age = int(jwt_settings.REFRESH_TOKEN_LIFETIME.total_seconds())

        resp = Response(
            {
                "access": access_token,
                "refresh": refresh_token,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )

        resp.set_cookie(
            "accessToken",
            access_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=access_age,
        )
        resp.set_cookie(
            "refreshToken",
            refresh_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=refresh_age,
        )

        return resp


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get("refreshToken")
        if not refresh_token:
            return Response(
                {"detail": "Refresh token missing"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Truyền refresh_token vào serializer
        serializer = LogoutSerializer(data={}, token=refresh_token)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Xóa cookie
        response = Response(
            {"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT
        )
        response.delete_cookie("accessToken")
        response.delete_cookie("refreshToken")

        return response


class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Lấy refresh token từ cookie
        refresh_token = request.COOKIES.get("refreshToken")
        if not refresh_token:
            return Response(
                {"message": "Không tìm thấy refresh token trong cookie."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Gửi refresh token để nhận access token mới
        serializer = self.get_serializer(data={"refresh": refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except InvalidToken:
            return Response(
                {"message": "Refresh token không hợp lệ hoặc đã hết hạn."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Trả về access token mới
        resp = Response(
            {
                "access": serializer.validated_data.get("access"),
                "message": "Làm mới access token thành công.",
            },
            status=status.HTTP_200_OK,
        )

        max_age = int(jwt_settings.ACCESS_TOKEN_LIFETIME.total_seconds())
        resp.set_cookie(
            "accessToken",
            serializer.validated_data.get("access"),
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=max_age,
        )
        return resp
