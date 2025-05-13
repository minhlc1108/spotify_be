from .artist_serializer import ArtistSerializer, ArtistDetailSerializer
from .genre_serializer import GenreSerializer
from .album_serializer import AlbumSerializer, AlbumDetailSerializer
from .play_state_serializer import PlayStateSerializer, PlayStateUpdateSerializer
from .track_serializer import TrackSerializer, TrackDetailSerializer
from .playlist_serializer import PlaylistSerializer, PlaylistDetailSerializer
from .user_serializer import (
    UserLoginSerializer,
    UserRegisterSerializer,
    LogoutSerializer,
)
