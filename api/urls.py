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
    LibraryDetailView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("artists/<uuid:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("genres/", GenreListView.as_view(), name="artist-list"),
    path("genres/<uuid:pk>/", GenreDetailView.as_view(), name="artist-detail"),
    path("albums/", AlbumListView.as_view(), name="artist-list"),
    path("albums/<uuid:pk>/", AlbumDetailView.as_view(), name="artist-detail"),
    path("tracks/", TrackListView.as_view(), name="artist-list"),
    path("tracks/<uuid:pk>/", TrackDetailView.as_view(), name="artist-detail"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/refreshToken/", TokenRefreshView.as_view(), name="refreshToken"),
    # path('library/', LibraryListView.as_view(), name='library-list'),
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
]
