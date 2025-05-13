from rest_framework import serializers
from api.models import Library
from .nested_serializer import SimpleArtistSerializer, SimpleAlbumSerializer,SimpleTrackSerializer, SimplePlaylistSerializer


class LibrarySerializer(serializers.ModelSerializer):
    liked_tracks = SimpleTrackSerializer(many=True, read_only=True)
    saved_albums = SimpleAlbumSerializer(many=True, read_only=True)
    followed_artists = SimpleArtistSerializer(many=True, read_only=True)
    saved_playlists = SimplePlaylistSerializer(many=True, read_only=True)

    class Meta:
        model = Library
        fields = [
            "liked_tracks",
            "saved_albums",
            "followed_artists",
            "saved_playlists",
        ]