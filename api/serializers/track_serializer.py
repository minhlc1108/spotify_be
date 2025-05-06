from rest_framework import serializers
from api.models import Track
from api.serializers.genre_serializer import GenreSerializer
from api.validators import validate_audio, validate_image
from .nested_serializer import SimpleArtistSerializer, SimpleAlbumSerializer


class TrackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Track model.
    """

    artists = SimpleArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = "__all__"

    def validate_cover_image(self, value):
        """
        Validate the cover image.
        """
        validate_image(value)
        return value

    def validate_audio_file(self, value):
        """
        Validate the audio file.
        """
        validate_audio(value)
        return value


class TrackDetailSerializer(serializers.ModelSerializer):
    artists = SimpleArtistSerializer(many=True, read_only=True)
    album = SimpleAlbumSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = "__all__"

    def validate_cover_image(self, value):
        validate_image(value)
        return value

    def validate_audio_file(self, value):
        validate_audio(value)
        return value
