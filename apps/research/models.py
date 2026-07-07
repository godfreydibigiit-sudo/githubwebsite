"""
Models for competitor analysis and research findings.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel


class CompetitorSystem(models.Model):
    """
    Existing systems analyzed during research phase.
    """
    class SystemType(models.TextChoices):
        DIRECT = 'direct', _('Direct Competitor')
        INDIRECT = 'indirect', _('Indirect Competitor')
        INSPIRATION = 'inspiration', _('Inspiration Source')
    
    # Basic Information
    name = models.CharField(max_length=200, verbose_name=_('System Name'))
    developer = models.CharField(max_length=200, verbose_name=_('Developer/Company'), blank=True)
    website_url = models.URLField(verbose_name=_('Website URL'), blank=True)
    system_type = models.CharField(
        max_length=20,
        choices=SystemType.choices,
        default=SystemType.DIRECT,
        verbose_name=_('System Type')
    )
    
    # Analysis
    description = models.TextField(verbose_name=_('Description'))
    features = models.TextField(verbose_name=_('Key Features'))
    strengths = models.TextField(verbose_name=_('Strengths'))
    weaknesses = models.TextField(verbose_name=_('Weaknesses'))
    
    # HCI-Specific Analysis
    ui_analysis = models.TextField(
        verbose_name=_('UI/UX Analysis'),
        help_text=_('Analysis of interface design, usability, and user experience')
    )
    design_patterns_used = models.TextField(
        verbose_name=_('Design Patterns Used'),
        blank=True,
        help_text=_('UI patterns, navigation styles, interaction methods')
    )
    
    # Visual Reference
    screenshot = models.ImageField(
        upload_to='research/screenshots/',
        verbose_name=_('Screenshot')
    )
    additional_screenshots = models.ManyToManyField(
        'ResearchScreenshot',
        blank=True,
        related_name='competitor_systems'
    )
    
    # Meta
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Competitor System')
        verbose_name_plural = _('Competitor Systems')
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_system_type_display()})"


class ResearchScreenshot(models.Model):
    """
    Additional screenshots for competitor analysis.
    """
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    image = models.ImageField(upload_to='research/screenshots/')
    caption = models.CharField(max_length=500, blank=True)
    
    class Meta:
        verbose_name = _('Research Screenshot')
        verbose_name_plural = _('Research Screenshots')
    
    def __str__(self):
        return self.title


class ProblemFound(models.Model):
    """
    Problems discovered during research phase.
    """
    class Severity(models.TextChoices):
        HIGH = 'high', _('High')
        MEDIUM = 'medium', _('Medium')
        LOW = 'low', _('Low')
    
    title = models.CharField(max_length=200, verbose_name=_('Problem Title'))
    description = models.TextField(verbose_name=_('Problem Description'))
    description_sw = models.TextField(verbose_name=_('Problem Description (Swahili)'), blank=True)
    severity = models.CharField(
        max_length=10,
        choices=Severity.choices,
        default=Severity.MEDIUM,
        verbose_name=_('Severity')
    )
    affected_users = models.CharField(max_length=200, verbose_name=_('Affected Users'))
    evidence = models.TextField(
        verbose_name=_('Evidence'),
        help_text=_('How was this problem discovered?')
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('Problem Found')
        verbose_name_plural = _('Problems Found')
        ordering = ['severity', 'order']
    
    def __str__(self):
        return self.title


class Opportunity(models.Model):
    """
    Opportunities identified from research.
    """
    class Priority(models.TextChoices):
        HIGH = 'high', _('High Priority')
        MEDIUM = 'medium', _('Medium Priority')
        LOW = 'low', _('Low Priority')
    
    title = models.CharField(max_length=200, verbose_name=_('Opportunity Title'))
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    how_to_address = models.TextField(
        verbose_name=_('How to Address'),
        help_text=_('How our system will address this opportunity')
    )
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    related_problems = models.ManyToManyField(
        ProblemFound,
        blank=True,
        related_name='opportunities'
    )
    icon = models.CharField(max_length=50, default='fas fa-lightbulb')
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('Opportunity')
        verbose_name_plural = _('Opportunities')
        ordering = ['priority', 'order']
    
    def __str__(self):
        return self.title


class ResearchFinding(models.Model):
    """
    Key findings from the research phase.
    """
    title = models.CharField(max_length=200, verbose_name=_('Finding'))
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    implication = models.TextField(
        verbose_name=_('Design Implication'),
        help_text=_('How this finding affects our design decisions')
    )
    icon = models.CharField(max_length=50, default='fas fa-search')
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('Research Finding')
        verbose_name_plural = _('Research Findings')
        ordering = ['order']
    
    def __str__(self):
        return self.title