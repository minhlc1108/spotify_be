from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from api.models.album import Album
from api.models.artist import Artist
from api.models.track import Track
from api.serializers.album_serializer import AlbumSerializer
from api.serializers.artist_serializer import ArtistSerializer
from api.serializers.track_serializer import TrackSerializer


class SearchView(APIView):
    def get(self, request):
        query = request.GET.get("q", "")

        artists = Artist.objects.filter(name__icontains=query)
        albums = Album.objects.filter(title__icontains=query)
        tracks = Track.objects.filter(title__icontains=query)

        return Response(
            {
                "artists": ArtistSerializer(artists, many=True).data,
                "albums": AlbumSerializer(albums, many=True).data,
                "tracks": TrackSerializer(tracks, many=True).data,
            }
        )
