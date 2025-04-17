from django.contrib import admin
from api.models import Artist, Album, Genre, Track

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


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
