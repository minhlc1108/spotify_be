from django import forms

from .models import Album, Artist, Track,Library
from .validators import validate_image, validate_audio


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
class LibraryAdminForm(forms.ModelForm):

    class Meta:
        model = Library
        fields = "__all__"



class TrackAdminForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = "__all__"

    def clean_cover_image(self):
        cover_image = self.cleaned_data.get("cover_image")
        if cover_image:
            try:
                validate_image(cover_image)
            except forms.ValidationError as e:
                raise forms.ValidationError(f"Ảnh không hợp lệ: {e}")
        return cover_image

    def clean_audio_file(self):
        audio_file = self.cleaned_data.get("audio_file")
        if audio_file:
            try:
                validate_audio(audio_file)
            except forms.ValidationError as e:
                raise forms.ValidationError(f"File âm thanh không hợp lệ: {e}")
        return audio_file
