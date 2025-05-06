from rest_framework import generics
from api.models import Album
from api.serializers import AlbumSerializer, AlbumDetailSerializer


# List view - Hiển thị tất cả các Album
class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# Detail view - Hiển thị chi tiết của một Album
class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
