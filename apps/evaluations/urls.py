"""
URL configuration for evaluations app.
"""
from django.urls import path
from apps.evaluations.views import (
    EvaluationView, EvaluationDetailView,
    FindingDetailView, PosterView
)

app_name = 'evaluations'

urlpatterns = [
    path('', EvaluationView.as_view(), name='list'),
    path('detail/<int:pk>/', EvaluationDetailView.as_view(), name='detail'),
    path('finding/<int:pk>/', FindingDetailView.as_view(), name='finding_detail'),
    path('poster/', PosterView.as_view(), name='poster'),
]