from rest_framework import generics
from api.models import Genre
from api.serializers import GenreSerializer


# List view - Hiển thị tất cả các Genre
class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Detail view - Hiển thị chi tiết của một Genre
class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
