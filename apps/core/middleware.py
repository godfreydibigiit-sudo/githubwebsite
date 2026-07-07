"""
Custom middleware for HCI Portfolio.
"""
from django.utils import translation


class ThemeMiddleware:
    """
    Middleware to handle dark/light theme switching.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Handle theme switching via GET parameter
        theme_param = request.GET.get('theme')
        if theme_param in ['dark', 'light']:
            request.session['theme'] = theme_param
        
        # Set default theme if not set
        if 'theme' not in request.session:
            request.session['theme'] = 'dark'
        
        response = self.get_response(request)
        return response