"""
URL configuration for requirements app.
"""
from django.urls import path
from apps.requirements.views import RequirementsView

app_name = 'requirements'

urlpatterns = [
    path('', RequirementsView.as_view(), name='list'),
]