
from api.validators import validate_image
from rest_framework import serializers
from api.models.play_state import PlayState
from api.serializers.track_serializer import TrackSerializer  # Nhớ import đúng

class PlayStateSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = PlayState
        fields = [
            "current_track",
            "is_playing",
            "progress",
            "is_shuffle",
            "is_looping",
            "volume",
            "context_id",
            "context_type",
            "position_in_context",
            "last_updated",
        ]
