from rest_framework import serializers
from api.models import Artist
from .nested_serializer import SimpleAlbumSerializer, SimpleTrackSerializer
from api.validators import validate_image


class ArtistSerializer(serializers.ModelSerializer):
    tracks = SimpleTrackSerializer(many=True, read_only=True)
    albums = SimpleAlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["id", "name", "image", "bio", "tracks", "gender", "albums"]

    def validate_image(self, value):
        validate_image(value)
        return value
