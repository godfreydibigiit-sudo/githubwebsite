"""
Views for requirements app.
"""
from django.views.generic import TemplateView
from apps.requirements.models import FunctionalRequirement, NonFunctionalRequirement


class RequirementsView(TemplateView):
    """
    Display all functional and non-functional requirements.
    """
    template_name = 'pages/requirements.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all requirements organized by category
        context['functional_requirements'] = FunctionalRequirement.objects.all()
        context['non_functional_requirements'] = NonFunctionalRequirement.objects.all()
        
        # Group non-functional by category
        from itertools import groupby
        nfr_grouped = {}
        for category in NonFunctionalRequirement.Category.values:
            reqs = NonFunctionalRequirement.objects.filter(category=category)
            if reqs.exists():
                nfr_grouped[category] = reqs
        
        context['nfr_grouped'] = nfr_grouped
        context['page_title'] = 'Requirements'
        
        return context