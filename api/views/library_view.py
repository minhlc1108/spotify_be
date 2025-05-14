from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from api.models import Library, Track, Album, Artist, Playlist
from api.serializers import LibrarySerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class LibraryView(generics.RetrieveUpdateDestroyAPIView):


    serializer_class = LibrarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, request, *args, **kwargs):
        user = request.user
        try:
            return Library.objects.get(user=user)
        except Library.DoesNotExist:
            raise Http404("Library của người dùng chưa được tạo.")

    def get(self, request, *args, **kwargs):
        """
        Xử lý yêu cầu GET, trả về thư viện của người dùng.
        """
        library = self.get_object(request)
        serializer = LibrarySerializer(library)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Xử lý yêu cầu POST, thêm các đối tượng vào thư viện của người dùng.
        Các tham số `item_type` và `item_id` sẽ được lấy từ request body hoặc query parameters.
        """
        user = request.user
        item_type = request.data.get('type')
        item_id = request.data.get('id')

        try:
            library = Library.objects.get(user=user)

            # Thêm các đối tượng vào thư viện
            if item_type == 'track':
                obj = Track.objects.get(id=item_id)
                library.liked_tracks.add(obj)
            elif item_type == 'album':
                obj = Album.objects.get(id=item_id)
                library.saved_albums.add(obj)
            elif item_type == 'artist':
                obj = Artist.objects.get(id=item_id)
                library.followed_artists.add(obj)
            elif item_type == 'playlist':
                obj = Playlist.objects.get(id=item_id)
                library.saved_playlists.add(obj)
            else:
                return Response({"error": "Loại không hợp lệ"}, status=400)

            return Response({"message": f"Đã thêm {item_type} vào thư viện."})

        except Library.DoesNotExist:
            raise Http404("Library của người dùng chưa được tạo.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Xử lý yêu cầu DELETE, xóa đối tượng khỏi thư viện của người dùng.
        """
        user = request.user
        item_type = request.data.get('type')
        item_id = request.data.get('id')

        try:
            library = Library.objects.get(user=user)

            # Xóa đối tượng khỏi thư viện
            if item_type == 'track':
                obj = Track.objects.get(id=item_id)
                library.liked_tracks.remove(obj)
            elif item_type == 'album':
                obj = Album.objects.get(id=item_id)
                library.saved_albums.remove(obj)
            elif item_type == 'artist':
                obj = Artist.objects.get(id=item_id)
                library.followed_artists.remove(obj)
            elif item_type == 'playlist':
                obj = Playlist.objects.get(id=item_id)
                library.saved_playlists.remove(obj)
            else:
                return Response({"error": "Loại không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": f"Đã xóa {item_type} khỏi thư viện."}, status=status.HTTP_200_OK)

        except Library.DoesNotExist:
            raise Http404("Library của người dùng chưa được tạo.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
