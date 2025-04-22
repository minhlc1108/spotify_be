from django.db import models


class PlayHistory(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="play_history"
    )
    track = models.ForeignKey(
        "Track", on_delete=models.CASCADE, related_name="play_histories"
    )
    played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "play_history"
        ordering = ["-played_at"]
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["track"]),
            models.Index(fields=["-played_at"]),
        ]

    def __str__(self):
        return (
            f"{self.track.title} played by {self.user.display_name} at {self.played_at}"
        )
