"""
Models for main portfolio pages - Site settings and configuration.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel


class SiteSetting(models.Model):
    """
    Global site configuration - Singleton model.
    Only one instance should exist.
    """
    # Project Information
    project_name = models.CharField(
        max_length=200,
        default="HCI Portfolio",
        verbose_name=_('Project Name')
    )
    project_name_sw = models.CharField(
        max_length=200,
        default="Kwingiko la HCI",
        verbose_name=_('Project Name (Swahili)')
    )
    
    # Branding
    logo_dark = models.ImageField(
        upload_to='logo/',
        verbose_name=_('Logo (Dark Theme)'),
        help_text=_('Logo for dark mode')
    )
    logo_light = models.ImageField(
        upload_to='logo/',
        verbose_name=_('Logo (Light Theme)'),
        help_text=_('Logo for light mode')
    )
    favicon = models.ImageField(
        upload_to='logo/',
        verbose_name=_('Favicon')
    )
    
    # Hero Section
    hero_title = models.CharField(
        max_length=200,
        default="Human Computer Interface Design",
        verbose_name=_('Hero Title')
    )
    hero_title_sw = models.CharField(
        max_length=200,
        default="Usanifu wa Kiolesura cha Kompyuta na Binadamu",
        verbose_name=_('Hero Title (Swahili)')
    )
    hero_subtitle = models.CharField(
        max_length=200,
        default="A User-Centered Design Case Study",
        verbose_name=_('Hero Subtitle')
    )
    hero_subtitle_sw = models.CharField(
        max_length=200,
        default="Uchunguzi wa Usanifu unaomlenga Mtumiaji",
        verbose_name=_('Hero Subtitle (Swahili)')
    )
    
    # Project Description
    brief_intro = models.TextField(
        verbose_name=_('Brief Introduction'),
        help_text=_('2-3 sentences describing the project')
    )
    brief_intro_sw = models.TextField(
        verbose_name=_('Brief Introduction (Swahili)'),
        blank=True
    )
    problem_statement = models.TextField(
        verbose_name=_('Problem Statement'),
        help_text=_('What problem does this project solve?')
    )
    problem_statement_sw = models.TextField(
        verbose_name=_('Problem Statement (Swahili)'),
        blank=True
    )
    target_users = models.TextField(
        verbose_name=_('Target Users'),
        help_text=_('Who are the intended users?')
    )
    target_users_sw = models.TextField(
        verbose_name=_('Target Users (Swahili)'),
        blank=True
    )
    
    # Academic Information
    programme = models.CharField(
        max_length=200,
        default="BSc. Computer Science / BSc. Information Technology",
        verbose_name=_('Programme')
    )
    course_code = models.CharField(
        max_length=50,
        default="CSU07425/ITUO7425",
        verbose_name=_('Course Code')
    )
    university = models.CharField(
        max_length=200,
        default="Institute of Finance Management",
        verbose_name=_('University')
    )
    faculty = models.CharField(
        max_length=200,
        default="Faculty of Computing, Information Systems and Mathematics",
        verbose_name=_('Faculty')
    )
    
    # Footer
    footer_text = models.CharField(
        max_length=200,
        default="© 2026 HCI Portfolio - IFM. All rights reserved.",
        verbose_name=_('Footer Text')
    )
    
    # Meta
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is Active')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At')
    )
    
    class Meta:
        verbose_name = _('Site Setting')
        verbose_name_plural = _('Site Settings')
    
    def __str__(self):
        return self.project_name
    
    def save(self, *args, **kwargs):
        """Ensure only one instance exists (Singleton pattern)."""
        if not self.pk and SiteSetting.objects.exists():
            raise ValueError("Only one SiteSetting instance can exist. Edit the existing one.")
        super().save(*args, **kwargs)
    
    @classmethod
    def get_instance(cls):
        """Get or create the singleton instance."""
        instance, created = cls.objects.get_or_create(pk=1)
        return instance


class AboutSection(models.Model):
    """
    About page content sections.
    """
    site_setting = models.ForeignKey(
        SiteSetting,
        on_delete=models.CASCADE,
        related_name='about_sections'
    )
    
    title = models.CharField(max_length=200, verbose_name=_('Section Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Section Title (Swahili)'), blank=True)
    content = models.TextField(verbose_name=_('Content'))
    content_sw = models.TextField(verbose_name=_('Content (Swahili)'), blank=True)
    icon = models.CharField(
        max_length=50,
        default='fas fa-info-circle',
        help_text=_('Font Awesome icon class')
    )
    section_type = models.CharField(
        max_length=50,
        choices=[
            ('overview', _('System Overview')),
            ('why_exists', _('Why Project Exists')),
            ('objectives', _('Objectives')),
            ('users', _('Users')),
        ],
        verbose_name=_('Section Type')
    )
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    
    class Meta:
        verbose_name = _('About Section')
        verbose_name_plural = _('About Sections')
        ordering = ['order']
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"


class ProjectObjective(models.Model):
    """
    Project objectives.
    """
    site_setting = models.ForeignKey(
        SiteSetting,
        on_delete=models.CASCADE,
        related_name='objectives'
    )
    
    title = models.CharField(max_length=200, verbose_name=_('Objective'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Objective (Swahili)'), blank=True)
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    icon = models.CharField(max_length=50, default='fas fa-bullseye')
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('Project Objective')
        verbose_name_plural = _('Project Objectives')
        ordering = ['order']
    
    def __str__(self):
        return self.title


class UserGroup(models.Model):
    """
    Target user groups for the system.
    """
    site_setting = models.ForeignKey(
        SiteSetting,
        on_delete=models.CASCADE,
        related_name='user_groups'
    )
    
    name = models.CharField(max_length=200, verbose_name=_('User Group Name'))
    name_sw = models.CharField(max_length=200, verbose_name=_('User Group Name (Swahili)'), blank=True)
    description = models.TextField(verbose_name=_('Description'))
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    icon = models.CharField(max_length=50, default='fas fa-users')
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('User Group')
        verbose_name_plural = _('User Groups')
        ordering = ['order']
    
    def __str__(self):
        return self.name