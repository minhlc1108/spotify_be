from django.db import models


class PlayState(models.Model):

    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="play_state"
    )
    current_track = models.ForeignKey("Track", on_delete=models.SET_NULL, null=True)
    progress = models.PositiveIntegerField(default=0)
    is_playing = models.BooleanField(default=False)
    is_shuffle = models.BooleanField(default=False)
    is_looping = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["-last_updated"]),
        ]
