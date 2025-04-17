from rest_framework import generics
from api.models import Artist
from api.serializers import ArtistSerializer


# List view - Hiển thị tất cả các Artist
class ArtistListView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# Detail view - Hiển thị chi tiết của một Artist
class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
