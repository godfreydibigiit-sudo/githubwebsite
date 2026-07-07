"""
Models for functional and non-functional requirements.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel


class FunctionalRequirement(models.Model):
    """
    Functional requirements for the system.
    """
    class Priority(models.TextChoices):
        HIGH = 'high', _('High')
        MEDIUM = 'medium', _('Medium')
        LOW = 'low', _('Low')
    
    class Status(models.TextChoices):
        IMPLEMENTED = 'implemented', _('Implemented')
        IN_PROGRESS = 'in_progress', _('In Progress')
        PLANNED = 'planned', _('Planned')
    
    # Core fields
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Title (Swahili)'), blank=True)
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('Requirement Code'),
        help_text=_('e.g., FR-001, FR-002')
    )
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    # Classification
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        verbose_name=_('Priority')
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
        verbose_name=_('Status')
    )
    category = models.CharField(
        max_length=100,
        verbose_name=_('Category'),
        help_text=_('e.g., User Management, Authentication, Reporting')
    )
    
    # UI Representation
    icon = models.CharField(
        max_length=50,
        default='fas fa-check-circle',
        verbose_name=_('Icon'),
        help_text=_('Font Awesome icon class')
    )
    
    # Meta
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Functional Requirement')
        verbose_name_plural = _('Functional Requirements')
        ordering = ['order', 'code']
    
    def __str__(self):
        return f"{self.code} - {self.title}"


class NonFunctionalRequirement(models.Model):
    """
    Non-functional requirements including usability requirements.
    """
    class Category(models.TextChoices):
        USABILITY = 'usability', _('Usability')
        PERFORMANCE = 'performance', _('Performance')
        SECURITY = 'security', _('Security')
        RELIABILITY = 'reliability', _('Reliability')
        MAINTAINABILITY = 'maintainability', _('Maintainability')
        COMPATIBILITY = 'compatibility', _('Compatibility')
    
    class Priority(models.TextChoices):
        HIGH = 'high', _('High')
        MEDIUM = 'medium', _('Medium')
        LOW = 'low', _('Low')
    
    # Core fields
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Title (Swahili)'), blank=True)
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('Requirement Code'),
        help_text=_('e.g., NFR-001, UR-001')
    )
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    # Classification
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        verbose_name=_('Category')
    )
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        verbose_name=_('Priority')
    )
    
    # UI Representation
    icon = models.CharField(
        max_length=50,
        default='fas fa-shield-alt',
        verbose_name=_('Icon'),
        help_text=_('Font Awesome icon class')
    )
    
    # Meta
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Non-Functional Requirement')
        verbose_name_plural = _('Non-Functional Requirements')
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.code} - {self.title}"