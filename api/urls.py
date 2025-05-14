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
    LoginView,
    RegisterView,
    LogoutView,
    PlayStateView,
    CookieTokenRefreshView,
    PlaylistListView,
    PlaylistDetailView,
    SearchView,
    LibraryView,
    LibrarySearchView
)

urlpatterns = [
    path("artist/", ArtistListView.as_view(), name="artist-list"),
    path("artist/<uuid:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("genre/", GenreListView.as_view(), name="artist-list"),
    path("genre/<uuid:pk>/", GenreDetailView.as_view(), name="artist-detail"),
    path("album/", AlbumListView.as_view(), name="artist-list"),
    path("album/<uuid:pk>/", AlbumDetailView.as_view(), name="artist-detail"),
    path("track/", TrackListView.as_view(), name="artist-list"),
    path("track/<uuid:pk>/", TrackDetailView.as_view(), name="artist-detail"),
    path("search/", SearchView.as_view(), name="search"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("playstate/", PlayStateView.as_view(), name="playState"),
    path("auth/refreshToken/", CookieTokenRefreshView.as_view(), name="refreshToken"),
    # path('library/', LibraryListView.as_view(), name='library-list'),
    path('library/', LibraryView.as_view(), name='library'),
    path('library-search/', LibrarySearchView.as_view(), name='library-search'),


    path("playlists/", PlaylistListView.as_view(), name="playlist-list"),
    path("playlists/<uuid:pk>/", PlaylistDetailView.as_view(), name="playlist-detail"),
    path("playlists/<uuid:pk>/tracks/", PlaylistDetailView.as_view(), name="playlist-add-track"),
]
