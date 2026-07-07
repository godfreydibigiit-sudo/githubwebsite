"""
Class-Based Views for main portfolio pages.
"""
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from apps.pages.models import SiteSetting, AboutSection, ProjectObjective, UserGroup
from apps.team.models import TeamMember


class HomeView(TemplateView):
    """
    Landing page - Project overview and team.
    """
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSetting.get_instance()
        context['team_members'] = TeamMember.objects.filter(is_active=True).order_by('order')
        context['page_title'] = 'Home'
        return context


class AboutView(TemplateView):
    """
    About page - System overview, objectives, users.
    """
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSetting.get_instance()
        context['about_sections'] = AboutSection.objects.all()
        context['objectives'] = ProjectObjective.objects.all()
        context['user_groups'] = UserGroup.objects.all()
        context['page_title'] = 'About'
        return context