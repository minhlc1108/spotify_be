from django.db import models
import uuid
from django.core.exceptions import ValidationError


class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="playlists"
    )
    description = models.TextField(blank=True)
    tracks = models.ManyToManyField(
        "Track", through="PlaylistTrack", related_name="tracks_playlists"
    )
    cover_image = models.ImageField(upload_to="playlists/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.owner.first().display_name}"

    class Meta:
        db_table = "playlist"
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["created_at"]),
        ]

    def add_track(self, track, user, position=None):
        """
        Thêm track vào vị trí cụ thể
        - position=None: Thêm vào cuối
        """
        if position is None:
            position = self.tracks.count() + 1

        # Dịch chuyển các track hiện có
        PlaylistTrack.objects.filter(playlist=self, order__gte=position).update(
            order=models.F("order") + 1
        )

        return PlaylistTrack.objects.create(
            playlist=self, track=track, order=position, added_by=user
        )

    # def reorder_tracks(self, new_order):
    #     """
    #     Sắp xếp lại thứ tự bài hát
    #     :param new_order: List các ID track theo thứ tự mới
    #     """
    #     current_mapping = {pt.track_id: pt.order for pt in self.playlisttrack_set.all()}

    #     with transaction.atomic():
    #         for new_index, track_id in enumerate(new_order, start=1):
    #             PlaylistTrack.objects.filter(playlist=self, track_id=track_id).update(
    #                 order=new_index
    #             )


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    track = models.ForeignKey("Track", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0, help_text="Position in playlist (1-based index)"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["playlist", "order"], name="unique_order_per_playlist"
            )
        ]

    def clean(self):
        # Validate order >= 1
        if self.order < 1:
            raise ValidationError("Order must be at least 1")

        # Check track duration limit (optional)
        max_duration = 10 * 60  # 10 minutes
        if self.track.duration > max_duration:
            raise ValidationError("Track exceeds maximum allowed duration")

    def save(self, *args, **kwargs):
        # Auto-increment order if not provided
        if not self.order:
            max_order = (
                PlaylistTrack.objects.filter(playlist=self.playlist).aggregate(
                    models.Max("order")
                )["order__max"]
                or 0
            )
            self.order = max_order + 1
        super().save(*args, **kwargs)
