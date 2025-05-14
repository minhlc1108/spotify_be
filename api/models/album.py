from django.db import models
from django.utils import timezone
import uuid


class Album(models.Model):
    ALBUM_TYPES = (
        ("ALBUM", "Album"),
        ("SINGLE", "Single"),
        ("EP", "EP"),
    )
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=255)
    album_type = models.CharField(max_length=10, choices=ALBUM_TYPES, default="SINGLE")
    artists = models.ManyToManyField("Artist", related_name="albums")
    cover_image = models.ImageField(upload_to="albums/", blank=True, null=True)
    release_date = models.DateField(default=timezone.now)

    def __str__(self):
        first_artist = self.artists.first()
        artist_name = first_artist.name if first_artist else "Unknown Artist"
        return f"{self.title} - {artist_name}"

    class Meta:
        ordering = ["release_date"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["release_date"]),
        ]
