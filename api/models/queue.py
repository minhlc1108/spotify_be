from django.db import models


class Queue(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="queue")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def queue_tracks(self):
        return self.tracks.order_by("position")


class QueueTrack(models.Model):
    SOURCE_CHOICES = [
        ("queue", "User Queue"),
        ("context", "Playlist/Album/Artist"),
    ]
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE, related_name="tracks")
    track = models.ForeignKey("Track", on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["position"]
        unique_together = ("queue", "position", "source")
