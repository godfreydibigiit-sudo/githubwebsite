"""
Views for evaluations app.
"""
from django.views.generic import TemplateView, DetailView
from apps.evaluations.models import (
    HeuristicEvaluation, Heuristic, EvaluationFinding, Poster
)


class EvaluationView(TemplateView):
    """
    Main evaluation page - Assignment #4.
    """
    template_name = 'pages/evaluation.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evaluation'] = HeuristicEvaluation.objects.first()
        context['findings'] = EvaluationFinding.objects.all()
        context['heuristics'] = Heuristic.objects.all()
        context['page_title'] = 'Heuristic Evaluation'
        return context


class EvaluationDetailView(DetailView):
    """
    Detailed view of a single evaluation session.
    """
    model = HeuristicEvaluation
    template_name = 'pages/evaluation_detail.html'
    context_object_name = 'evaluation'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['findings'] = self.object.findings.all()
        context['page_title'] = self.object.title
        return context


class FindingDetailView(DetailView):
    """
    Detailed view of a single evaluation finding with before/after.
    """
    model = EvaluationFinding
    template_name = 'pages/finding_detail.html'
    context_object_name = 'finding'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Finding #{self.object.finding_number}"
        return context


class PosterView(TemplateView):
    """
    Project poster page - Assignment #5.
    """
    template_name = 'pages/poster.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poster'] = Poster.objects.filter(is_published=True).first()
        context['page_title'] = 'Project Poster'
        return context