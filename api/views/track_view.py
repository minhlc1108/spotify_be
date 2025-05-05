from rest_framework import generics
from api.models import Track
from api.serializers import TrackSerializer, TrackDetailSerializer


# List view - Hiển thị tất cả các Track
class TrackListView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


# Detail view - Hiển thị chi tiết của một Track
class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackDetailSerializer
