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
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        # Cho phép login bằng email hoặc username
        username = attrs.get("username")
        email = attrs.get("email")
        password = attrs["password"]

        if email and not username:
            # tìm user tương ứng email để lấy username
            try:
                u = User.objects.get(email=email)
                username = u.username
            except User.DoesNotExist:
                raise serializers.ValidationError(
                    "User with this email does not exist."
                )
        if not username:
            raise serializers.ValidationError("Please provide username or email.")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        attrs["user"] = user
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            raise serializers.ValidationError("Invalid token")
