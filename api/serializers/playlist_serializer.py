from rest_framework import serializers
from api.models import Playlist
from .nested_serializer import SimpleTrackSerializer
from api.validators import validate_image


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

    def validate_image(self, value):
        validate_image(value)
        return value


class PlaylistDetailSerializer(serializers.ModelSerializer):
    tracks = SimpleTrackSerializer(many=True, read_only=True)
   
    class Meta:
        model = Playlist
        fields = "__all__"

    def validate_image(self, value):
        validate_image(value)
        return value
