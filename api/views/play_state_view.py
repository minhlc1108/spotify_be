from rest_framework import status, permissions
from rest_framework.response import Response
from api.models import PlayState, Track
from api.serializers import PlayStateSerializer
from rest_framework.views import APIView


class PlayStateView(APIView):
    serializer_class = PlayStateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        play_state, created = PlayState.objects.get_or_create(user=user)
        if created:
            # Chỉ set mặc định nếu vừa tạo mới
            play_state.save()

        serializer = PlayStateSerializer(play_state)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        play_state, _ = PlayState.objects.get_or_create(user=user)

        track_id = data.get("current_track")
        is_playing = data.get("is_playing")

        # Gắn cờ nếu bài hát thay đổi
        track_changed = False

        if track_id:
            try:
                new_track = Track.objects.get(id=track_id)
                if play_state.current_track != new_track:
                    play_state.current_track = new_track
                    track_changed = True
            except Track.DoesNotExist:
                return Response({"error": "Track not found"}, status=404)

        if "is_playing" in data:
            play_state.is_playing = is_playing

            # Nếu chuyển sang trạng thái đang phát và bài hát mới -> tăng play_count
            if is_playing and track_changed:
                play_state.current_track.play_count += 1
                play_state.current_track.save()

            # Nếu pause, lưu lại progress nếu có
            elif not is_playing and "progress" in data:
                play_state.progress = data["progress"]

        # Các field khác
        for field in [
            "is_looping",
            "is_shuffle",
            "volume",
            "context_id",
            "context_type",
            "position_in_context",
            "progress",
        ]:
            if field in data:
                setattr(play_state, field, data[field])

        play_state.save()
        return Response(PlayStateSerializer(play_state).data, status=status.HTTP_200_OK)
