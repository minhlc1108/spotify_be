from django.db import models


class Library(models.Model):
    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, primary_key=True, related_name="library"
    )
    # Favourite
    liked_tracks = models.ManyToManyField("Track", related_name="liked_by_user")
    saved_albums = models.ManyToManyField(
        "Album", blank=True, related_name="album_saved_by_users"
    )
    followed_artists = models.ManyToManyField(
        "Artist", blank=True, related_name="followers"
    )
    saved_playlists = models.ManyToManyField(
        "Playlist", blank=True, related_name="playlist_saved_by_users"
    )

    class Meta:
        db_table = "library"
