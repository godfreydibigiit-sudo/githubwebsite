"""
Admin configuration for team app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.team.models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """
    Admin for team members.
    """
    list_display = ('registration_number', 'full_name', 'role', 'is_leader', 
                   'is_active', 'order')
    list_filter = ('role', 'is_active', 'is_leader')
    search_fields = ('first_name', 'last_name', 'registration_number', 'contribution')
    ordering = ('order', 'last_name')
    
    fieldsets = (
        (_('Personal Information'), {
            'fields': ('registration_number', 'first_name', 'last_name', 'email')
        }),
        (_('Role & Contribution'), {
            'fields': ('role', 'role_description', 'contribution')
        }),
        (_('Profile'), {
            'fields': ('photo', 'bio', 'skills')
        }),
        (_('Social Links'), {
            'fields': ('github_url', 'linkedin_url', 'portfolio_url')
        }),
        (_('Status'), {
            'fields': ('is_active', 'is_leader', 'order')
        }),
    )