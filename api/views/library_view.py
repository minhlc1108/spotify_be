from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from api.models import Library, Track, Album, Artist, Playlist
from api.serializers import LibrarySerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class LibraryView(generics.RetrieveUpdateDestroyAPIView):


    serializer_class = LibrarySerializer

    def get_object(self):
        try:
            user = User.objects.get(id=1)
            return Library.objects.get(user=user)
        except User.DoesNotExist:
            raise Http404("Người dùng không tồn tại.")
        except Library.DoesNotExist:
            raise Http404("Library của người dùng chưa được tạo.")
    def get(self, request, *args, **kwargs):
        """
        Xử lý yêu cầu GET, trả về thư viện của người dùng.
        """
        library = self.get_object()
        serializer = LibrarySerializer(library)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):  # args and kwargs are used implicitly
        """
        Xử lý yêu cầu POST, thêm các đối tượng vào thư viện của người dùng.
        Các tham số `item_type` và `item_id` sẽ được lấy từ request body hoặc query parameters.
        """
        user = User.objects.get(id=1)
        item_type = request.data.get('type')
        item_id = request.data.get('id')

        try:
            # user = User.objects.get(id=self.kwargs['pk'])
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

        except User.DoesNotExist:
            raise Http404("Người dùng không tồn tại.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, *args, **kwargs):
        """
        Xử lý yêu cầu DELETE, xóa đối tượng khỏi thư viện của người dùng.
        """
        item_type = request.data.get('type')
        item_id = request.data.get('id')

        try:
            user = User.objects.get(id=1)
            library = Library.objects.get(user=user)

            # Xóa đối tượng khỏi thư viện
            if item_type == 'track':
                obj = Track.objects.get(id=item_id)
                library.liked_tracks.remove(obj)  # Xóa track khỏi thư viện
            elif item_type == 'album':
                obj = Album.objects.get(id=item_id)
                library.saved_albums.remove(obj)  # Xóa album khỏi thư viện
            elif item_type == 'artist':
                obj = Artist.objects.get(id=item_id)
                library.followed_artists.remove(obj)  # Xóa artist khỏi thư viện
            elif item_type == 'playlist':
                obj = Playlist.objects.get(id=item_id)
                library.saved_playlists.remove(obj)  # Xóa playlist khỏi thư viện
            else:
                return Response({"error": "Loại không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": f"Đã xóa {item_type} khỏi thư viện."}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "Người dùng không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
