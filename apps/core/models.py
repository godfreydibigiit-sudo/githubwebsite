"""
Abstract base models for the HCI Portfolio project.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    Abstract model that provides created_at and updated_at fields.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        abstract = True


class TranslatedModel(models.Model):
    """
    Abstract model with translation helper methods.
    """
    class Meta:
        abstract = True
    
    def get_translated_field(self, field_name):
        """Get translated field based on current language."""
        from django.utils import translation
        current_lang = translation.get_language()
        
        if current_lang == 'sw':
            sw_field = f'{field_name}_sw'
            value = getattr(self, sw_field, None)
            if value:
                return value
        
        return getattr(self, field_name, '')