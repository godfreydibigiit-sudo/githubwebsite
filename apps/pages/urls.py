"""
URL configuration for pages app.
"""
from django.urls import path
from apps.pages.views import HomeView, AboutView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]