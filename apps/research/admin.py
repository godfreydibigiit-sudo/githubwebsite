"""
Admin configuration for research app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.research.models import (
    CompetitorSystem, ResearchScreenshot, ProblemFound, 
    Opportunity, ResearchFinding
)


class ResearchScreenshotInline(admin.TabularInline):
    model = ResearchScreenshot
    extra = 1


@admin.register(CompetitorSystem)
class CompetitorSystemAdmin(admin.ModelAdmin):
    """
    Admin for competitor systems.
    """
    list_display = ('name', 'developer', 'system_type', 'order')
    list_filter = ('system_type',)
    search_fields = ('name', 'developer', 'description')
    ordering = ('order', 'name')
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'developer', 'website_url', 'system_type')
        }),
        (_('Analysis'), {
            'fields': ('description', 'features', 'strengths', 'weaknesses')
        }),
        (_('HCI Analysis'), {
            'fields': ('ui_analysis', 'design_patterns_used')
        }),
        (_('Visual Reference'), {
            'fields': ('screenshot',)
        }),
        (_('Display'), {
            'fields': ('order',)
        }),
    )


@admin.register(ProblemFound)
class ProblemFoundAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'affected_users', 'order')
    list_filter = ('severity',)
    search_fields = ('title', 'description')
    ordering = ('severity', 'order')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'description_sw', 'severity', 
                      'affected_users', 'evidence', 'order')
        }),
    )


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'order')
    list_filter = ('priority',)
    search_fields = ('title', 'description')
    filter_horizontal = ('related_problems',)
    ordering = ('priority', 'order')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'description_sw', 'how_to_address', 
                      'priority', 'related_problems', 'icon', 'order')
        }),
    )


@admin.register(ResearchFinding)
class ResearchFindingAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'description')
    ordering = ('order',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'description_sw', 'implication', 
                      'icon', 'order')
        }),
    )