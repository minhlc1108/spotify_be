from rest_framework import serializers
from api.models import Artist, Track, Album


class SimpleArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name", "image"]


class SimpleAlbumSerializer(serializers.ModelSerializer):
    artists = SimpleArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["id", "title", "album_type", "artists", "cover_image"]


class SimpleTrackSerializer(serializers.ModelSerializer):
    artists = SimpleArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = [
            "id",
            "title",
            "duration",
            "artists",
            "audio_file",
            "video_file",
            "album",
            "cover_image",
            "genres",
            "play_count",
        ]
