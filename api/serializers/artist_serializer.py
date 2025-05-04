from rest_framework import serializers
from api.models import Artist
from api.validators import validate_image


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

    def validate_image(self, value):
        validate_image(value)
        return value
