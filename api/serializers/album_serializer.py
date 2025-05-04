from rest_framework import serializers
from api.models import Album
from api.validators import validate_image


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "album_type",
            "artists",
            "cover_image",
            "release_date",
        ]

    def validate_cover_image(self, value):
        validate_image(value)
        return value
