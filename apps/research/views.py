"""
Views for research app.
"""
from django.views.generic import TemplateView, DetailView
from apps.research.models import CompetitorSystem, ProblemFound, Opportunity, ResearchFinding


class ResearchView(TemplateView):
    """
    Main research page showing all research components.
    """
    template_name = 'pages/research.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competitors'] = CompetitorSystem.objects.all()
        context['problems'] = ProblemFound.objects.all()
        context['opportunities'] = Opportunity.objects.all()
        context['findings'] = ResearchFinding.objects.all()
        context['page_title'] = 'Research'
        return context


class CompetitorDetailView(DetailView):
    """
    Detailed view of a single competitor system.
    """
    model = CompetitorSystem
    template_name = 'pages/competitor_detail.html'
    context_object_name = 'competitor'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.name
        return context