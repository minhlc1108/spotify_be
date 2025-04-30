from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


class PlayState(models.Model):
    CONTEXT_TYPE_CHOICES = [
        ("playlist", "Playlist"),
        ("album", "Album"),
        ("artist", "Artist"),
        ("liked", "Liked Songs"),
    ]

    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="play_state"
    )
    current_track = models.ForeignKey(
        "Track", on_delete=models.SET_NULL, blank=True, null=True
    )
    progress = models.PositiveIntegerField(default=0)
    is_playing = models.BooleanField(default=False)
    is_shuffle = models.BooleanField(default=False)
    is_looping = models.BooleanField(default=False)
    volume = models.PositiveIntegerField(
        default=70, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    context_id = models.UUIDField(default=uuid.uuid4, editable=False)
    context_type = models.CharField(
        max_length=20,
        choices=CONTEXT_TYPE_CHOICES,
        null=True,
        blank=True,
    )
    position_in_context = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["-last_updated"]),
        ]
