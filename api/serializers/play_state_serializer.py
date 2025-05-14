from api.validators import validate_image
from rest_framework import serializers
from api.models.play_state import PlayState
from api.models.track import Track

from api.serializers.track_serializer import (
    TrackDetailSerializer,
    TrackSerializer,
)  # Nhớ import đúng

from rest_framework import serializers


class PlayStateSerializer(serializers.ModelSerializer):
    current_track = TrackDetailSerializer(read_only=True)

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


class PlayStateUpdateSerializer(serializers.ModelSerializer):
    current_track = serializers.PrimaryKeyRelatedField(
        queryset=Track.objects.all(), required=False, allow_null=True
    )

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
