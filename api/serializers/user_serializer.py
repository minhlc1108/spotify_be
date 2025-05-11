from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="Username đã tồn tại.")
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="Email đã tồn tại.")
        ]
    )
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "re_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError({"password": "Hai mật khẩu không khớp."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("re_password")
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # Chứa email hoặc username
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        identifier = attrs.get("identifier")
        password = attrs["password"]

        # Thử tìm theo email trước
        user = None
        if "@" in identifier:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError("User không tồn tại")
        else:
            user = authenticate(username=identifier, password=password)

        if not user:
            raise serializers.ValidationError(
                "Tài khoản hoặc mật khẩu không chính xác."
            )

        attrs["user"] = user
        return attrs


class LogoutSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop("token", None)
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        if not self.token:
            raise serializers.ValidationError("Token is required.")

        try:
            # Chỉ gọi blacklisting khi token hợp lệ
            refresh_token = RefreshToken(self.token)
            refresh_token.blacklist()  # Đảm bảo token này được đưa vào blacklist
        except Exception as e:
            raise serializers.ValidationError(f"Invalid or expired token: {str(e)}")
