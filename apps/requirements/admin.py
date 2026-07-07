"""
Admin configuration for requirements app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.requirements.models import FunctionalRequirement, NonFunctionalRequirement


@admin.register(FunctionalRequirement)
class FunctionalRequirementAdmin(admin.ModelAdmin):
    """
    Admin for functional requirements.
    """
    list_display = ('code', 'title', 'category', 'priority', 'status', 'order')
    list_filter = ('priority', 'status', 'category')
    search_fields = ('title', 'code', 'description')
    ordering = ('order', 'code')
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('code', 'title', 'title_sw', 'description', 'description_sw')
        }),
        (_('Classification'), {
            'fields': ('category', 'priority', 'status')
        }),
        (_('Display'), {
            'fields': ('icon', 'order')
        }),
    )
    
    prepopulated_fields = {}  # Remove if you want auto code generation


@admin.register(NonFunctionalRequirement)
class NonFunctionalRequirementAdmin(admin.ModelAdmin):
    """
    Admin for non-functional requirements.
    """
    list_display = ('code', 'title', 'category', 'priority', 'order')
    list_filter = ('category', 'priority')
    search_fields = ('title', 'code', 'description')
    ordering = ('category', 'order')
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('code', 'title', 'title_sw', 'description', 'description_sw')
        }),
        (_('Classification'), {
            'fields': ('category', 'priority')
        }),
        (_('Display'), {
            'fields': ('icon', 'order')
        }),
    )