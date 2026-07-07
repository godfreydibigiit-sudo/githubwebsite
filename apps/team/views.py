"""
Views for team app.
"""
from django.views.generic import TemplateView, DetailView
from apps.team.models import TeamMember


class TeamView(TemplateView):
    """
    Display all team members with roles.
    """
    template_name = 'pages/team.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.filter(is_active=True).order_by('order')
        context['team_leader'] = TeamMember.objects.filter(is_leader=True).first()
        context['page_title'] = 'Team'
        
        # Group by role for organized display
        from collections import defaultdict
        members_by_role = defaultdict(list)
        for member in context['team_members']:
            members_by_role[member.get_role_display()].append(member)
        context['members_by_role'] = dict(members_by_role)
        
        return context


class TeamMemberDetailView(DetailView):
    """
    Detailed view of a single team member.
    """
    model = TeamMember
    template_name = 'pages/team_member_detail.html'
    context_object_name = 'member'
    slug_field = 'registration_number'
    slug_url_kwarg = 'reg_number'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.full_name
        return context