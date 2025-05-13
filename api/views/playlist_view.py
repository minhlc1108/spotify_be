from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Max
from django.db import transaction
import logging
from api.models import Playlist, Track, PlaylistTrack
from api.serializers import PlaylistSerializer, PlaylistDetailSerializer

logger = logging.getLogger(__name__)

# List view - Hiển thị tất cả các Playlist
class PlaylistListView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


# Detail view - Hiển thị chi tiết của một Playlist
class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistDetailSerializer

    def post(self, request, *args, **kwargs):
        try:
            logger.debug(f"Request data: {request.data}")
            playlist = self.get_object()
            
            # Try both camelCase and snake_case
            track_id = request.data.get('trackId') or request.data.get('track_id')
            
            logger.debug(f"Track ID from request: {track_id}")
            
            if not track_id:
                logger.error("No trackId or track_id provided in request")
                return Response({'error': 'trackId is required'}, status=status.HTTP_400_BAD_REQUEST)
                
            try:
                track = Track.objects.get(id=track_id)
                logger.debug(f"Found track: {track}")
            except Track.DoesNotExist:
                logger.error(f"Track with ID {track_id} not found")
                return Response({'error': 'Track not found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Check if track is already in playlist
            if PlaylistTrack.objects.filter(playlist=playlist, track=track).exists():
                logger.warning(f"Track {track_id} already exists in playlist {playlist.id}")
                return Response({'error': 'Track already in playlist'}, status=status.HTTP_400_BAD_REQUEST)
            
            with transaction.atomic():
                # Get the next order number
                max_order = PlaylistTrack.objects.filter(playlist=playlist).aggregate(Max('order'))['order__max']
                next_order = 1 if max_order is None else max_order + 1
                logger.debug(f"Next order number: {next_order}")
                
                # Create the PlaylistTrack entry
                playlist_track = PlaylistTrack.objects.create(
                    playlist=playlist,
                    track=track,
                    order=next_order,
                    added_by=request.user if request.user.is_authenticated else None
                )
                logger.debug(f"Created PlaylistTrack: {playlist_track}")
            
            return Response(status=status.HTTP_201_CREATED)
            
        except Exception as e:
            logger.error(f"Error adding track to playlist: {str(e)}")
            return Response(
                {'error': 'An error occurred while adding the track to the playlist'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )