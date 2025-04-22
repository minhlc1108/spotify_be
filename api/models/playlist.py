from django.db import models
import uuid


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
    public = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to="playlists/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.owner.first().display_name}"

    class Meta:
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["created_at"]),
        ]


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey("Track", on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    added_by = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]
        unique_together = ("playlist", "order")
