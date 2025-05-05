from rest_framework import generics
from api.models import Library
from api.serializers import LibrarySerializer


# List view - Hiển thị tất cả các Library
class LibraryListView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


# Detail view - Hiển thị chi tiết của một Library
class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
