from rest_framework import serializers
from api.models import Album
from .nested_serializer import SimpleArtistSerializer, SimpleTrackSerializer
from api.validators import validate_image


class AlbumSerializer(serializers.ModelSerializer):
    artists = SimpleArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = "__all__"

    def validate_cover_image(self, value):
        validate_image(value)
        return value


class AlbumDetailSerializer(serializers.ModelSerializer):
    artists = SimpleArtistSerializer(many=True, read_only=True)
    tracks = SimpleTrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "album_type",
            "artists",
            "tracks",
            "cover_image",
            "release_date",
        ]

    def validate_cover_image(self, value):
        validate_image(value)
        return value
