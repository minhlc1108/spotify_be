from django import forms

from .models import Album, Artist
from .validators import validate_image


class ArtistAdminForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            try:
                validate_image(image)
            except forms.ValidationError as e:
                raise forms.ValidationError(f"Ảnh không hợp lệ: {e}")
        return image


class AlbumAdminForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = "__all__"

    def clean_cover_image(self):
        cover_image = self.cleaned_data.get("cover_image")
        if cover_image:
            try:
                validate_image(cover_image)
            except forms.ValidationError as e:
                raise forms.ValidationError(f"Ảnh không hợp lệ: {e}")
        return cover_image
