
from api.validators import validate_image
from rest_framework import serializers
from api.models.play_state import PlayState
from api.serializers.track_serializer import TrackSerializer  # Nhớ import đúng

class PlayStateSerializer(serializers.ModelSerializer):
    currentTrack = TrackSerializer(source="current_track", read_only=True)
    isPlaying = serializers.BooleanField(source="is_playing")
    isShuffle = serializers.BooleanField(source="is_shuffle")
    isLooping = serializers.BooleanField(source="is_looping")
    positionInContext = serializers.IntegerField(source="position_in_context")
    contextType = serializers.CharField(source="context_type", allow_null=True)
    contextId = serializers.UUIDField(source="context_id")
    lastUpdated = serializers.DateTimeField(source="last_updated", read_only=True)

    class Meta:
        model = PlayState
        fields = [
            "currentTrack",
            "isPlaying",
            "progress",
            "isShuffle",
            "isLooping",
            "volume",
            "contextId",
            "contextType",
            "positionInContext",
            "lastUpdated",
        ]
