from django.conf import settings
from io import BytesIO
from PIL import Image
from autocrop import Cropper

import os

BACKGROUND_TRANSPARENT = (255, 255, 255, 0)


def clean_unusable_thumbnails(image_name):
    file_path = os.path.join(settings.MEDIA_ROOT, str(image_name))
    if os.path.isfile(file_path):
        os.remove(file_path)


def get_file_name(file_name):
    """
        Return file name without extension
    """
    return str(file_name).split('.')[0]


def get_file_extension(file_name):
    """
        Return file extension
    """
    extension = None

    if str(file_name).split('.')[-1].lower() != 'jpg':
        extension = str(file_name).split('.')[-1].upper()
    else:
        extension = 'JPEG'

    return extension


def image_crop_optimizer(image, size, rename=None):

    extension = get_file_extension(image)
    image_name = get_file_name(image)

    cropper = Cropper(width=size[0], height=size[1])
    cropped_array = cropper.crop(image.path)
    cropped_image = Image.fromarray(cropped_array)

    if extension == 'JPEG':
        cropped_image = cropped_image.convert('RGB')

    if rename is not None:
        new_image_name = f'{image_name}_{rename}.{extension.lower()}'
    else:
        new_image_name = f'{image_name}.{extension.lower()}'

    cropped_image.seek(0)
    cropped_image.save(os.path.join(settings.MEDIA_ROOT, new_image_name), format=extension, optimize=True, quality=85)

    if str(image).split('.')[-1].lower() == 'jpg':
        clean_unusable_thumbnails(image)

    return new_image_name
