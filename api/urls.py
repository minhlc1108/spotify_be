from django.urls import path
from api.views import (
    ArtistListView,
    ArtistDetailView,
    GenreListView,
    GenreDetailView,
    AlbumListView,
    AlbumDetailView,
    TrackListView,
    TrackDetailView,
)

urlpatterns = [
    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("artists/<uuid:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("genres/", GenreListView.as_view(), name="artist-list"),
    path("genres/<uuid:pk>/", GenreDetailView.as_view(), name="artist-detail"),
    path("albums/", AlbumListView.as_view(), name="artist-list"),
    path("albums/<uuid:pk>/", AlbumDetailView.as_view(), name="artist-detail"),
    path("tracks/", TrackListView.as_view(), name="artist-list"),
    path("tracks/<uuid:pk>/", TrackDetailView.as_view(), name="artist-detail"),
]
