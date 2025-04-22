from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    REQUIRED_FIELDS = ["email"]  # bắt buộc khi tạo superuser
    USERNAME_FIELD = "username"  # dùng username cho superuser

    def __str__(self):
        return self.username
