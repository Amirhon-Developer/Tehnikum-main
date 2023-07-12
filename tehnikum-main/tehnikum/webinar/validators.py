from django.core.exceptions import ValidationError


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    SIZE_LIMIT = 5
    if filesize > SIZE_LIMIT * 1024 * 1024:
        raise ValidationError(f"Max file size is {SIZE_LIMIT}MB")
