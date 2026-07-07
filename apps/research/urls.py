"""
URL configuration for research app.
"""
from django.urls import path
from apps.research.views import ResearchView, CompetitorDetailView

app_name = 'research'

urlpatterns = [
    path('', ResearchView.as_view(), name='list'),
    path('competitor/<int:pk>/', CompetitorDetailView.as_view(), name='competitor_detail'),
]