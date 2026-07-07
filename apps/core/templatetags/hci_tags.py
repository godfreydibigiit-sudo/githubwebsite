"""
Custom template tags for HCI Portfolio.
"""
from django import template
from django.utils.translation import gettext as _

register = template.Library()


@register.simple_tag
def get_translated_field(obj, field_name):
    """
    Template tag to get translated field value.
    Usage: {% get_translated_field object 'title' %}
    """
    from django.utils import translation
    current_lang = translation.get_language()
    
    if current_lang == 'sw':
        sw_field = f'{field_name}_sw'
        value = getattr(obj, sw_field, None)
        if value:
            return value
    
    return getattr(obj, field_name, '')


@register.simple_tag(takes_context=True)
def current_language_flag(context):
    """
    Returns current language code.
    """
    return translation.get_language()


@register.filter
def get_item(dictionary, key):
    """
    Get item from dictionary by key.
    """
    return dictionary.get(key, '')


@register.simple_tag
def severity_badge_class(severity):
    """
    Return appropriate Bootstrap badge class for heuristic severity.
    """
    severity_map = {
        'cosmetic': 'bg-info',
        'minor': 'bg-warning',
        'major': 'bg-danger',
        'catastrophic': 'bg-dark',
    }
    return severity_map.get(severity, 'bg-secondary')


@register.simple_tag
def priority_badge_class(priority):
    """
    Return appropriate Bootstrap badge class for requirement priority.
    """
    priority_map = {
        'high': 'bg-danger',
        'medium': 'bg-warning text-dark',
        'low': 'bg-success',
    }
    return priority_map.get(priority, 'bg-secondary')