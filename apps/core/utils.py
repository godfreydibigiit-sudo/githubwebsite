"""
Utility functions for HCI Portfolio.
"""
import os
from django.conf import settings
from django.utils.text import slugify


def get_file_upload_path(instance, filename, folder):
    """
    Generate upload path for model instances.
    
    Usage in models:
        image = models.ImageField(upload_to=get_file_upload_path('prototypes'))
    """
    ext = filename.split('.')[-1]
    model_name = instance.__class__.__name__.lower()
    filename = f"{slugify(instance.title if hasattr(instance, 'title') else 'file')}.{ext}"
    return os.path.join(folder, filename)


def get_image_dimensions(image_field):
    """
    Get image dimensions from an ImageField.
    Returns (width, height) tuple.
    """
    from PIL import Image
    
    try:
        img = Image.open(image_field)
        return img.size
    except Exception:
        return (0, 0)


def format_file_size(size_bytes):
    """
    Convert bytes to human-readable format.
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def get_current_language():
    """
    Get current active language code.
    """
    from django.utils import translation
    return translation.get_language()