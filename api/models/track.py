from django.db import models
from django.utils import timezone
import uuid


class Track(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=255)
    lyrics = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="tracks/image/", blank=True, null=True)
    audio_file = models.FileField(upload_to="tracks/audio/")
    video_file = models.FileField(upload_to="tracks/video/", blank=True, null=True)
    album = models.ForeignKey(
        "Album", on_delete=models.SET_NULL, null=True, blank=True, related_name="tracks"
    )
    artists = models.ManyToManyField("Artist", related_name="tracks")
    genres = models.ManyToManyField("Genre", related_name="tracks")
    play_count = models.PositiveBigIntegerField(default=0)
    duration = models.PositiveBigIntegerField(default=0)
    release_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.artists.first().name}"

    class Meta:
        db_table = "track"
        ordering = ["release_date"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["play_count"]),
            models.Index(fields=["release_date"]),
        ]
