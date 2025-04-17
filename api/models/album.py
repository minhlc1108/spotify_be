from django.db import models
import uuid


class Album(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField("Genre", related_name="albums_genres")
    artists = models.ManyToManyField("Artist", related_name="albums_artists")
    cover_image = models.ImageField(upload_to="albums/", blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.artists.first().name}"

    class Meta:
        db_table = "album"
        ordering = ["release_date"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["release_date"]),
        ]
