"""
URL configuration for prototypes app.
"""
from django.urls import path
from apps.prototypes.views import (
    PrototypesOverviewView,
    LowFidelityView, LowFidelityDetailView,
    MediumFidelityView, MediumFidelityDetailView,
    HighFidelityView, HighFidelityDetailView,
    DesignIterationsView,
)

app_name = 'prototypes'

urlpatterns = [
    # Overview
    path('', PrototypesOverviewView.as_view(), name='overview'),
    
    # Low-Fidelity
    path('low-fidelity/', LowFidelityView.as_view(), name='low_fidelity_list'),
    path('low-fidelity/<int:pk>/', LowFidelityDetailView.as_view(), name='low_fidelity_detail'),
    
    # Medium-Fidelity
    path('medium-fidelity/', MediumFidelityView.as_view(), name='medium_fidelity_list'),
    path('medium-fidelity/<int:pk>/', MediumFidelityDetailView.as_view(), name='medium_fidelity_detail'),
    
    # High-Fidelity
    path('high-fidelity/', HighFidelityView.as_view(), name='high_fidelity_list'),
    path('high-fidelity/<int:pk>/', HighFidelityDetailView.as_view(), name='high_fidelity_detail'),
    
    # Design Iterations
    path('iterations/', DesignIterationsView.as_view(), name='iterations'),
]