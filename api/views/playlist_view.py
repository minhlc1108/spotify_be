from rest_framework import generics
from api.models import Playlist
from api.serializers import PlaylistSerializer, PlaylistDetailSerializer


# List view - Hiển thị tất cả các Playlist
class PlaylistListView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


# Detail view - Hiển thị chi tiết của một Playlist
class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistDetailSerializer