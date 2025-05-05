from rest_framework import generics
from django.contrib.auth import get_user_model
from api.models import Library
from api.serializers import LibrarySerializer

User = get_user_model()

class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LibrarySerializer

    def get_object(self):
        try:
            user = User.objects.get(id=1)
            return Library.objects.get(user=user)
        except User.DoesNotExist:
            raise Http404("User mặc định (id=1) không tồn tại.")
        except Library.DoesNotExist:
            raise Http404("Library chưa được tạo.")
