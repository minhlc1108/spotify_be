from django.contrib import admin
from api.admin_form import AlbumAdminForm, ArtistAdminForm, TrackAdminForm, LibraryAdminForm

from api.models.album import Album
from api.models.artist import Artist
from api.models.genre import Genre
from api.models.library import Library
from api.models.track import Track

from api.models.user import User
from api.models import Playlist
# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    form = ArtistAdminForm
    list_display = (
        "id",
        "name",
        "bio",
        "gender",
        "created_at",
    )  # Hiển thị các trường bạn muốn trong danh sáchg
    search_fields = ("name", "bio")
    list_filter = ("gender",)
class LibraryAdmin(admin.ModelAdmin):
    form = LibraryAdminForm
    list_display = (
        "user",
    )  # Hiển thị các trường bạn muốn trong danh sách
    search_fields = ("user",)


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumAdminForm  # Sử dụng form với validation tùy chỉnh
    list_display = (
        "id",
        "title",
        "release_date",
        "get_artist",
        "album_type",
    )

    def get_artist(self, obj):
        return ", ".join([artist.name for artist in obj.artists.all()])

    get_artist.short_description = "Artists"
    search_fields = ("title",)
    list_filter = ("album_type", "artists")


class TrackAdmin(admin.ModelAdmin):
    form = TrackAdminForm
    list_display = (
        "id",
        "title",
        "album",
        "get_genres",
        "play_count",
    )

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = "Genres"
    search_fields = ("title",)
    list_filter = ("album", "genres")
    readonly_fields = ("duration", "play_count")


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(User)
admin.site.register(Library,LibraryAdmin)
