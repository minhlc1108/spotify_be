from rest_framework import serializers
from api.models import Artist, Track, Album, Library, Playlist


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
            "cover_image",
            "audio_file",
            "video_file",
        ]


class SimpleLibrarySerializer(serializers.ModelSerializer):
    liked_tracks = SimpleTrackSerializer(many=True, read_only=True)
    saved_albums = SimpleAlbumSerializer(many=True, read_only=True)
    followed_artists = SimpleArtistSerializer(many=True, read_only=True)
    # saved_playlists = SimplePlaylistSerializer(many=True, read_only=True)

    class Meta:
        model = Library
        fields = [
            'user',
            'liked_tracks',
            'saved_albums',
            'followed_artists',
            'saved_playlists',
        ]


class SimplePlaylistSerializer(serializers.ModelSerializer):
    tracks = SimpleTrackSerializer(many=True, read_only=True)

    class Meta:

        model = Playlist
        fields = ['title', 'cover_image', 'tracks']