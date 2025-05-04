from django import forms
from PIL import Image
import os
from mutagen import File as MutagenFile


def validate_image(file, max_size_mb=5, allowed_types=("JPEG", "PNG", "WEBP")):
    # Kiểm tra dung lượng ảnh

    if file.size > max_size_mb * 1024 * 1024:
        raise forms.ValidationError(f"Ảnh phải nhỏ hơn {max_size_mb}MB.")

    # Kiểm tra định dạng ảnh
    try:
        image = Image.open(file)
        file.seek(0)
        if image.format.upper() not in allowed_types:
            raise forms.ValidationError(
                f"Chỉ hỗ trợ định dạng ảnh: {', '.join(allowed_types)}."
            )
    except Exception:
        raise forms.ValidationError("File không phải là ảnh hợp lệ.")


def validate_audio(
    file, max_size_mb=10, allowed_extensions=("mp3", "wav", "m4a", "flac")
):
    # 1. Kiểm tra dung lượng
    if file.size > max_size_mb * 1024 * 1024:
        raise forms.ValidationError(f"File audio phải nhỏ hơn {max_size_mb}MB.")

    # 2. Kiểm tra phần mở rộng
    ext = os.path.splitext(file.name)[1][1:].lower()
    if ext not in allowed_extensions:
        raise forms.ValidationError(
            f"Chỉ chấp nhận các định dạng audio: {', '.join(allowed_extensions)}."
        )

    # 3. Kiểm tra có phải file audio thực sự không
    try:
        audio_file = MutagenFile(file)
        if (
            audio_file is None
            or not hasattr(audio_file, "info")
            or not hasattr(audio_file.info, "length")
        ):
            raise forms.ValidationError("File không phải là audio hợp lệ.")
    except Exception:
        raise forms.ValidationError("Không thể phân tích file audio.")
