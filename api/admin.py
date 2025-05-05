from django.contrib import admin
from api.models import Artist, Album, Genre, Track, Library
from api.models.user import User

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
class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
    )  # Hiển thị các trường bạn muốn trong danh sách
    search_fields = ("user","")


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Library,LibraryAdmin)
