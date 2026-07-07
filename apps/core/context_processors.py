"""
Global context processors for templates.
"""
from django.conf import settings


def site_settings(request):
    """
    Add site settings to all template contexts.
    """
    try:
        from apps.pages.models import SiteSetting
        site_setting = SiteSetting.objects.first()
    except (ImportError, Exception):
        site_setting = None
    
    return {
        'site_settings': site_setting,
    }


def theme_context(request):
    """
    Add theme state to all template contexts.
    """
    theme = request.session.get('theme', 'dark')
    return {
        'current_theme': theme,
    }