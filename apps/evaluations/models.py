"""
Models for heuristic evaluation and usability testing - Assignment #5.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class HeuristicEvaluation(models.Model):
    """
    Main heuristic evaluation session.
    """
    class EvaluationMethod(models.TextChoices):
        HEURISTIC = 'heuristic', _("Nielsen's Heuristic Evaluation")
        COGNITIVE = 'cognitive', _('Cognitive Walkthrough')
        THINK_ALOUD = 'think_aloud', _('Think Aloud Protocol')
        EXPERT_REVIEW = 'expert_review', _('Expert Review')
    
    # Evaluation Info
    title = models.CharField(max_length=200, verbose_name=_('Evaluation Title'))
    method = models.CharField(
        max_length=20,
        choices=EvaluationMethod.choices,
        default=EvaluationMethod.HEURISTIC,
        verbose_name=_('Evaluation Method')
    )
    date_conducted = models.DateField(verbose_name=_('Date Conducted'))
    
    # Evaluators
    evaluators = models.TextField(
        verbose_name=_('Evaluators'),
        help_text=_('Names and roles of evaluators, one per line')
    )
    number_of_evaluators = models.IntegerField(
        verbose_name=_('Number of Evaluators'),
        default=3
    )
    
    # Session Details
    prototype_evaluated = models.CharField(
        max_length=200,
        verbose_name=_('Prototype Evaluated'),
        help_text=_('Which prototype version was evaluated?')
    )
    session_duration = models.CharField(
        max_length=50,
        verbose_name=_('Session Duration'),
        help_text=_('e.g., 2 hours, 1 day'
    )
    )
    
    # Results Summary
    total_problems_found = models.IntegerField(default=0)
    summary = models.TextField(
        verbose_name=_('Evaluation Summary'),
        help_text=_('Overall findings and recommendations')
    )
    summary_sw = models.TextField(verbose_name=_('Evaluation Summary (Swahili)'), blank=True)
    
    # Report
    full_report_link = models.URLField(
        verbose_name=_('Full Report Link'),
        blank=True,
        help_text=_('Link to detailed evaluation report (Google Docs, PDF, etc.)')
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Heuristic Evaluation')
        verbose_name_plural = _('Heuristic Evaluations')
    
    def __str__(self):
        return f"{self.title} - {self.date_conducted}"


class Heuristic(models.Model):
    """
    Nielsen's 10 Usability Heuristics reference.
    """
    number = models.IntegerField(unique=True, verbose_name=_('Heuristic Number'))
    name = models.CharField(max_length=200, verbose_name=_('Heuristic Name'))
    name_sw = models.CharField(max_length=200, verbose_name=_('Heuristic Name (Swahili)'), blank=True)
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    class Meta:
        verbose_name = _('Heuristic')
        verbose_name_plural = _('Heuristics')
        ordering = ['number']
    
    def __str__(self):
        return f"H{self.number}: {self.name}"


class EvaluationFinding(models.Model):
    """
    Individual problems found during evaluation.
    """
    class Severity(models.TextChoices):
        COSMETIC = 'cosmetic', _('0 - Cosmetic (No fix needed)')
        MINOR = 'minor', _('1 - Minor (Fix if time)')
        MAJOR = 'major', _('2 - Major (Important to fix)')
        CATASTROPHIC = 'catastrophic', _('3 - Catastrophic (Must fix)')
    
    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        IN_PROGRESS = 'in_progress', _('In Progress')
        FIXED = 'fixed', _('Fixed')
        WONT_FIX = 'wont_fix', _("Won't Fix")
    
    # Links
    evaluation = models.ForeignKey(
        HeuristicEvaluation,
        on_delete=models.CASCADE,
        related_name='findings',
        verbose_name=_('Evaluation Session')
    )
    heuristic_violated = models.ForeignKey(
        Heuristic,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Heuristic Violated')
    )
    
    # Problem Details
    problem_title = models.CharField(max_length=200, verbose_name=_('Problem Title'))
    problem_description = models.TextField(
        verbose_name=_('Problem Description'),
        help_text=_('Detailed description of the usability problem')
    )
    problem_description_sw = models.TextField(
        verbose_name=_('Problem Description (Swahili)'),
        blank=True
    )
    
    # Location
    screen_location = models.CharField(
        max_length=200,
        verbose_name=_('Screen/Page Location'),
        help_text=_('Where in the interface was the problem found?')
    )
    
    # Classification
    severity = models.CharField(
        max_length=15,
        choices=Severity.choices,
        default=Severity.MINOR,
        verbose_name=_('Severity Rating')
    )
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.OPEN,
        verbose_name=_('Status')
    )
    
    # Evidence - Before/After Screenshots
    before_screenshot = models.ImageField(
        upload_to='evaluations/before/',
        verbose_name=_('Before Screenshot'),
        help_text=_('Screenshot showing the problem')
    )
    after_screenshot = models.ImageField(
        upload_to='evaluations/after/',
        verbose_name=_('After Screenshot'),
        help_text=_('Screenshot showing the fix')
    )
    
    # Solution
    recommendation = models.TextField(
        verbose_name=_('Recommendation'),
        help_text=_('How to fix the problem')
    )
    changes_made = models.TextField(
        verbose_name=_('Changes Made'),
        help_text=_('What was actually changed')
    )
    why_changes_were_made = models.TextField(
        verbose_name=_('Why Changes Were Made'),
        help_text=_('Justification for the design changes')
    )
    
    # Discovered By
    discovered_by = models.CharField(
        max_length=200,
        verbose_name=_('Discovered By'),
        help_text=_('Which evaluator found this issue?')
    )
    
    # Meta
    finding_number = models.IntegerField(default=0, verbose_name=_('Finding Number'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Evaluation Finding')
        verbose_name_plural = _('Evaluation Findings')
        ordering = ['severity', 'finding_number']
    
    def __str__(self):
        return f"Finding #{self.finding_number}: {self.problem_title}"


class Poster(models.Model):
    """
    Project poster - Assignment #5.
    """
    title = models.CharField(max_length=200, verbose_name=_('Poster Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Poster Title (Swahili)'), blank=True)
    poster_image = models.ImageField(
        upload_to='posters/',
        verbose_name=_('Poster Image')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Brief description of the poster content')
    )
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    # Poster Sections
    problem_summary = models.TextField(verbose_name=_('Problem Summary'), blank=True)
    solution_summary = models.TextField(verbose_name=_('Solution Summary'), blank=True)
    methodology_summary = models.TextField(verbose_name=_('Methodology Summary'), blank=True)
    key_features = models.TextField(verbose_name=_('Key Features'), blank=True)
    results_summary = models.TextField(verbose_name=_('Results Summary'), blank=True)
    
    is_published = models.BooleanField(default=False, verbose_name=_('Published'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Poster')
        verbose_name_plural = _('Posters')
    
    def __str__(self):
        return self.title