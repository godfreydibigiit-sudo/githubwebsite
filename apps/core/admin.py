"""
Admin configuration for core models.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import SiteConfiguration, TeamMember


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    """
    Admin interface for site-wide configuration.
    """
    fieldsets = (
        (_('Project Information'), {
            'fields': (
                'project_name', 'project_tagline',
                'programme_name', 'course_code',
                'university_name', 'faculty_name', 'department_name',
            )
        }),
        (_('Branding'), {
            'fields': ('logo', 'favicon'),
        }),
        (_('Design'), {
            'fields': ('primary_color', 'secondary_color'),
        }),
        (_('Content'), {
            'fields': (
                'project_description', 'problem_statement',
                'target_users', 'system_overview', 'objectives',
            ),
        }),
    )
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """
    Admin interface for team members.
    """
    list_display = [
        'get_full_name', 'registration_number', 'role_display',
        'order', 'is_active'
    ]
    list_filter = ['role', 'is_active']
    search_fields = [
        'first_name', 'last_name', 'registration_number', 'email'
    ]
    ordering = ['order', 'last_name']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        (_('Personal Information'), {
            'fields': (
                ('first_name', 'last_name'),
                'registration_number',
                'email',
                'photo',
            )
        }),
        (_('Role & Contribution'), {
            'fields': ('role', 'contribution', 'bio'),
            'description': _('Select the role from the dropdown and describe the contribution.')
        }),
        (_('Social Links (Optional)'), {
            'fields': ('linkedin_url', 'github_url'),
            'classes': ('collapse',),
        }),
        (_('Display Settings'), {
            'fields': ('order', 'is_active'),
            'description': _('Set the display order (0 = first) and whether to show on website.')
        }),
    )
    
    def role_display(self, obj):
        """Display role with color coding in list view."""
        role_map = {
            'PM': '👔 Project Manager',
            'PR': '🎤 Presenter',
            'EV': '📋 Evaluator',
            'CO': '💻 Coder',
            'DE': '🎨 Designer',
            'RE': '🔍 Researcher',
        }
        return role_map.get(obj.role, obj.get_role_display())
    role_display.short_description = _('Role')
    role_display.admin_order_field = 'role'