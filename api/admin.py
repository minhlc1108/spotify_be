from django.contrib import admin
from api.models import Artist, Album, Genre, Track, Queue
from api.models.user import User
from api.models import Playlist
# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "bio",
        "gender",
        "created_at",
    )  # Hiển thị các trường bạn muốn trong danh sách
    search_fields = ("name", "bio")
    list_filter = ("gender",)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "public",
        "created_at",
        "updated_at",
        "owner",  # Assuming you want to display the owner of the playlist
    )
    search_fields = ("title", "description")
    list_filter = ("public",)

class QueueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",  # Assuming you want to display the user associated with the queue
        "current_track",  # Assuming you want to display the current track
        "created_at",
    )
    search_fields = ("user__username",)  # Enable search by username of the user


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Queue, QueueAdmin)
