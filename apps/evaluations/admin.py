"""
Admin configuration for evaluations app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.evaluations.models import (
    HeuristicEvaluation, Heuristic, EvaluationFinding, Poster
)


class EvaluationFindingInline(admin.TabularInline):
    """Inline editor for evaluation findings."""
    model = EvaluationFinding
    extra = 0
    fields = ('problem_title', 'severity', 'status', 'discovered_by')
    show_change_link = True


@admin.register(HeuristicEvaluation)
class HeuristicEvaluationAdmin(admin.ModelAdmin):
    list_display = ('title', 'method', 'date_conducted', 'total_problems_found')
    list_filter = ('method', 'date_conducted')
    search_fields = ('title', 'evaluators')
    inlines = [EvaluationFindingInline]
    
    fieldsets = (
        (_('Evaluation Information'), {
            'fields': ('title', 'method', 'date_conducted', 'prototype_evaluated', 
                      'session_duration')
        }),
        (_('Evaluators'), {
            'fields': ('evaluators', 'number_of_evaluators')
        }),
        (_('Results'), {
            'fields': ('total_problems_found', 'summary', 'summary_sw')
        }),
        (_('Report'), {
            'fields': ('full_report_link',)
        }),
    )


@admin.register(Heuristic)
class HeuristicAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    ordering = ('number',)
    
    fieldsets = (
        (None, {
            'fields': ('number', 'name', 'name_sw', 'description', 'description_sw')
        }),
    )


@admin.register(EvaluationFinding)
class EvaluationFindingAdmin(admin.ModelAdmin):
    list_display = ('finding_number', 'problem_title', 'severity', 'status', 
                   'discovered_by', 'evaluation')
    list_filter = ('severity', 'status', 'evaluation', 'heuristic_violated')
    search_fields = ('problem_title', 'problem_description', 'discovered_by')
    ordering = ('evaluation', 'severity', 'finding_number')
    
    fieldsets = (
        (_('Links'), {
            'fields': ('evaluation', 'heuristic_violated', 'finding_number')
        }),
        (_('Problem'), {
            'fields': ('problem_title', 'problem_description', 'problem_description_sw',
                      'screen_location')
        }),
        (_('Classification'), {
            'fields': ('severity', 'status', 'discovered_by')
        }),
        (_('Evidence'), {
            'fields': ('before_screenshot', 'after_screenshot')
        }),
        (_('Solution'), {
            'fields': ('recommendation', 'changes_made', 'why_changes_were_made')
        }),
    )


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    
    fieldsets = (
        (_('Poster Information'), {
            'fields': ('title', 'title_sw', 'poster_image', 'description', 'description_sw')
        }),
        (_('Poster Content'), {
            'fields': ('problem_summary', 'solution_summary', 'methodology_summary',
                      'key_features', 'results_summary')
        }),
        (_('Status'), {
            'fields': ('is_published',)
        }),
    )