from rest_framework import serializers
from api.models import Track
from api.validators import validate_audio, validate_image
from .nested_serializer import SimpleArtistSerializer, SimpleAlbumSerializer


class TrackSerializer(serializers.ModelSerializer):
    artists = SimpleArtistSerializer(many=True, read_only=True)
    album = SimpleAlbumSerializer(read_only=True)

    class Meta:
        model = Track
        fields = [
            "id",
            "title",
            "duration",
            "artists",
            "lyrics",
            "audio_file",
            "album",
            "genres",
            "cover_image",
            "release_date",
        ]

    def validate_cover_image(self, value):
        validate_image(value)
        return value

    def validate_audio_file(self, value):
        validate_audio(value)
        return value
