"""
Admin configuration for pages app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.pages.models import SiteSetting, AboutSection, ProjectObjective, UserGroup


class AboutSectionInline(admin.StackedInline):
    """Inline editor for About sections."""
    model = AboutSection
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('section_type', 'title', 'title_sw', 'content', 'content_sw', 'icon', 'order')
        }),
    )


class ProjectObjectiveInline(admin.TabularInline):
    """Inline editor for Project objectives."""
    model = ProjectObjective
    extra = 0


class UserGroupInline(admin.TabularInline):
    """Inline editor for User groups."""
    model = UserGroup
    extra = 0


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Site Setting (Singleton).
    """
    fieldsets = (
        (_('Project Information'), {
            'fields': ('project_name', 'project_name_sw')
        }),
        (_('Branding'), {
            'fields': ('logo_dark', 'logo_light', 'favicon')
        }),
        (_('Hero Section'), {
            'fields': ('hero_title', 'hero_title_sw', 'hero_subtitle', 'hero_subtitle_sw')
        }),
        (_('Project Description'), {
            'fields': ('brief_intro', 'brief_intro_sw', 'problem_statement', 
                      'problem_statement_sw', 'target_users', 'target_users_sw')
        }),
        (_('Academic Information'), {
            'fields': ('programme', 'course_code', 'university', 'faculty')
        }),
        (_('Footer'), {
            'fields': ('footer_text',)
        }),
        (_('Status'), {
            'fields': ('is_active',)
        }),
    )
    
    inlines = [AboutSectionInline, ProjectObjectiveInline, UserGroupInline]
    
    def has_add_permission(self, request):
        """Prevent adding new instances if one exists."""
        if SiteSetting.objects.exists():
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the singleton instance."""
        return False


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'order')
    list_filter = ('section_type',)
    search_fields = ('title', 'content')
    ordering = ('section_type', 'order')


@admin.register(ProjectObjective)
class ProjectObjectiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'description')
    ordering = ('order',)