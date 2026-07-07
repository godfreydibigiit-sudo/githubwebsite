"""
Views for prototypes app.
"""
from django.views.generic import TemplateView, DetailView
from apps.prototypes.models import (
    LowFidelityPrototype, MediumFidelityPrototype, 
    HighFidelityPrototype, DesignIteration
)


class PrototypesOverviewView(TemplateView):
    """
    Overview of all prototype fidelity levels.
    """
    template_name = 'pages/prototypes_overview.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Prototypes'
        return context


class LowFidelityView(TemplateView):
    """
    Display all low-fidelity prototypes - Assignment #2.
    """
    template_name = 'pages/low_fidelity.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prototypes'] = LowFidelityPrototype.objects.all()
        context['page_title'] = 'Low-Fidelity Prototypes'
        return context


class LowFidelityDetailView(DetailView):
    """
    Detailed view of a single low-fidelity prototype.
    """
    model = LowFidelityPrototype
    template_name = 'pages/low_fidelity_detail.html'
    context_object_name = 'prototype'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.page_name
        context['mediumfi_versions'] = self.object.mediumfi_versions.all()
        return context


class MediumFidelityView(TemplateView):
    """
    Display all medium-fidelity wireframes - Assignment #3.
    """
    template_name = 'pages/medium_fidelity.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prototypes'] = MediumFidelityPrototype.objects.all()
        context['page_title'] = 'Medium-Fidelity Prototypes'
        return context


class MediumFidelityDetailView(DetailView):
    """
    Detailed view of a single medium-fidelity wireframe.
    """
    model = MediumFidelityPrototype
    template_name = 'pages/medium_fidelity_detail.html'
    context_object_name = 'prototype'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.page_name
        context['connected_screens'] = self.object.connected_screens.all()
        context['highfi_versions'] = self.object.highfi_versions.all()
        return context


class HighFidelityView(TemplateView):
    """
    Display all high-fidelity screens - Assignment #4.
    """
    template_name = 'pages/high_fidelity.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prototypes'] = HighFidelityPrototype.objects.all()
        context['page_title'] = 'High-Fidelity Prototype'
        return context


class HighFidelityDetailView(DetailView):
    """
    Detailed view of a single high-fidelity screen.
    """
    model = HighFidelityPrototype
    template_name = 'pages/high_fidelity_detail.html'
    context_object_name = 'prototype'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.page_name
        return context


class DesignIterationsView(TemplateView):
    """
    Display design iterations (before/after comparisons).
    """
    template_name = 'pages/design_iterations.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['iterations'] = DesignIteration.objects.all()
        context['page_title'] = 'Design Iterations'
        return context