"""
Admin configuration for prototypes app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.prototypes.models import (
    LowFidelityPrototype, MediumFidelityPrototype,
    HighFidelityPrototype, HighFiScreenshot, DesignIteration
)


class HighFiScreenshotInline(admin.TabularInline):
    model = HighFiScreenshot
    extra = 1


@admin.register(LowFidelityPrototype)
class LowFidelityPrototypeAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'order')
    search_fields = ('page_name', 'title', 'description')
    ordering = ('order',)
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'title_sw', 'page_name', 'description', 'description_sw')
        }),
        (_('Sketch'), {
            'fields': ('sketch_image',)
        }),
        (_('Design Details'), {
            'fields': ('design_rationale', 'user_interactions')
        }),
        (_('Display'), {
            'fields': ('order',)
        }),
    )


@admin.register(MediumFidelityPrototype)
class MediumFidelityPrototypeAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'lowfi_reference', 'order')
    search_fields = ('page_name', 'title', 'description')
    list_filter = ('lowfi_reference',)
    ordering = ('order',)
    filter_horizontal = ('connected_screens',)
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'title_sw', 'page_name', 'description', 'description_sw')
        }),
        (_('Wireframe'), {
            'fields': ('wireframe_image',)
        }),
        (_('Navigation'), {
            'fields': ('navigation_flow', 'connected_screens')
        }),
        (_('Improvements'), {
            'fields': ('improvements_from_lowfi', 'improvements_from_lowfi_sw')
        }),
        (_('Reference'), {
            'fields': ('lowfi_reference',)
        }),
        (_('Display'), {
            'fields': ('order',)
        }),
    )


@admin.register(HighFidelityPrototype)
class HighFidelityPrototypeAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'screen_type', 'is_featured', 'order')
    list_filter = ('screen_type', 'is_featured')
    search_fields = ('page_name', 'title', 'description')
    ordering = ('order',)
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'title_sw', 'page_name', 'screen_type', 
                      'description', 'description_sw')
        }),
        (_('Screenshot'), {
            'fields': ('screenshot',)
        }),
        (_('Design Details'), {
            'fields': ('color_palette', 'typography', 'interaction_details', 
                      'design_system_notes')
        }),
        (_('Reference'), {
            'fields': ('medfi_reference',)
        }),
        (_('Display'), {
            'fields': ('is_featured', 'order')
        }),
    )


@admin.register(DesignIteration)
class DesignIterationAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'description', 'reason')
    ordering = ('order',)
    
    fieldsets = (
        (_('Change Information'), {
            'fields': ('title', 'description', 'reason')
        }),
        (_('Before & After'), {
            'fields': ('before_image', 'after_image')
        }),
        (_('Reference'), {
            'fields': ('lowfi', 'mediumfi', 'highfi')
        }),
        (_('Display'), {
            'fields': ('order',)
        }),
    )