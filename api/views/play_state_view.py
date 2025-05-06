from rest_framework import status, permissions, generics
from rest_framework.response import Response
from api.models import PlayState, Track
from api.serializers import PlayStateSerializer
class PlayStateUpdateView(generics.UpdateAPIView):
    serializer_class = PlayStateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        play_state, _ = PlayState.objects.get_or_create(user=user)

        # Cập nhật track nếu có
        track_id = data.get("current_track")
        if track_id:
            try:
                play_state.current_track = Track.objects.get(id=track_id)
            except Track.DoesNotExist:
                return Response({"error": "Track not found"}, status=404)

        # Nếu người dùng gửi trạng thái chơi
        if "is_playing" in data:
            play_state.is_playing = data["is_playing"]

            # Nếu là pause, lưu lại progress nếu có
            if not data["is_playing"] and "progress" in data:
                play_state.progress = data["progress"]

        # Các field khác
        for field in ["is_looping", "is_shuffle", "volume", "context_id", "context_type", "position_in_context", "progress"]:
            if field in data:
                setattr(play_state, field, data[field])

        play_state.save()
        return Response(PlayStateSerializer(play_state).data, status=status.HTTP_200_OK)

