from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from api.models import Library, Track, Album, Artist, Playlist
from api.serializers import LibrarySerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# class LibrarySearchView(generics.ListAPIView):
class LibrarySearchView(generics.ListAPIView):
    serializer_class = LibrarySerializer

    def get_queryset(self):
        """
        Tìm kiếm các đối tượng trong thư viện của người dùng dựa trên từ khóa.
        """
        user = User.objects.get(id=1)
        library = Library.objects.get(user=user)

        # Lấy từ khóa tìm kiếm từ query parameters
        query = self.request.query_params.get('query', '')

        # Tìm kiếm trong các trường của thư viện
        liked_tracks = library.liked_tracks.filter(name__icontains=query)
        saved_albums = library.saved_albums.filter(name__icontains=query)
        followed_artists = library.followed_artists.filter(name__icontains=query)
        saved_playlists = library.saved_playlists.filter(name__icontains=query)

        return {
            'liked_tracks': liked_tracks,
            'saved_albums': saved_albums,
            'followed_artists': followed_artists,
            'saved_playlists': saved_playlists,
        }