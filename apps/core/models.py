"""
Core models for HCI Design Portfolio.
Contains team members, site configuration, and base models.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class TimeStampedModel(models.Model):
    """
    Abstract base model with created and updated timestamps.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )
    
    class Meta:
        abstract = True
        ordering = ['-created_at']


class SiteConfiguration(TimeStampedModel):
    """
    Singleton model for site-wide configuration.
    """
    # Project Information
    project_name = models.CharField(
        max_length=200,
        default='HCI Design Portfolio',
        verbose_name=_('Project Name')
    )
    project_tagline = models.CharField(
        max_length=500,
        default='Human-Computer Interface Design Journey',
        verbose_name=_('Project Tagline')
    )
    
    # Academic Information
    programme_name = models.CharField(
        max_length=200,
        default='Bachelor of  Science in information Technology',
        verbose_name=_('Programme Name')
    )
    course_code = models.CharField(
        max_length=20,
        default='CSU07425/ITUO7425',
        verbose_name=_('Course Code')
    )
    university_name = models.CharField(
        max_length=200,
        default='The Institute of Finance Management',
        verbose_name=_('University Name')
    )
    faculty_name = models.CharField(
        max_length=200,
        default='Faculty of Computing and Mathematics',
        verbose_name=_('Faculty Name')
    )
    department_name = models.CharField(
        max_length=200,
        default='Department of Information Technology',
        verbose_name=_('Department Name')
    )
    
    # Branding
    logo = models.ImageField(
        upload_to='branding/',
        blank=True,
        verbose_name=_('Site Logo'),
        help_text=_('Recommended size: 200x60px. PNG or SVG preferred.')
    )
    favicon = models.ImageField(
        upload_to='branding/',
        blank=True,
        verbose_name=_('Favicon'),
        help_text=_('32x32px ICO or PNG file.')
    )
    
    # Design Configuration
    primary_color = models.CharField(
        max_length=7,
        default='#1a237e',
        verbose_name=_('Primary Color'),
        help_text=_('Hex color code (e.g., #1a237e)')
    )
    secondary_color = models.CharField(
        max_length=7,
        default='#1976d2',
        verbose_name=_('Secondary Color'),
        help_text=_('Hex color code (e.g., #1976d2)')
    )
    
    # Content Sections
    project_description = models.TextField(
        blank=True,
        verbose_name=_('Project Description'),
        help_text=_('2-3 sentence compelling description of your project.')
    )
    problem_statement = models.TextField(
        blank=True,
        verbose_name=_('Problem Statement'),
        help_text=_('What problem does your project solve?')
    )
    target_users = models.TextField(
        blank=True,
        verbose_name=_('Target Users'),
        help_text=_('Who are the primary users of your system?')
    )
    system_overview = models.TextField(
        blank=True,
        verbose_name=_('System Overview'),
        help_text=_('Brief overview of the system functionality.')
    )
    objectives = models.TextField(
        blank=True,
        verbose_name=_('Project Objectives'),
        help_text=_('What are the main objectives of this project?')
    )
    
    class Meta:
        verbose_name = _('Site Configuration')
        verbose_name_plural = _('Site Configuration')
    
    def save(self, *args, **kwargs):
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValidationError(
                _('Only one site configuration can exist. Please edit the existing one instead.')
            )
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def __str__(self):
        return f'Site Configuration: {self.project_name}'


class TeamMember(TimeStampedModel):
    """
    Team member model with roles and contributions.
    """
    # Role choices with full descriptive names
    class Role(models.TextChoices):
        PROJECT_MANAGER = 'PM', _('Project Manager - Coordination & Scheduling')
        PRESENTER = 'PR', _('Presenter - Creates & Delivers Presentations')
        EVALUATOR = 'EV', _('Evaluator - Performs & Documents Evaluations')
        CODER = 'CO', _('Coder - Develops Prototypes & Code')
        DESIGNER = 'DE', _('Designer - Low & Medium Fidelity Prototypes')
        RESEARCHER = 'RE', _('Researcher - Research Other Similar Systems')
    
    # Personal Information
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('Registration Number'),
        help_text=_('Student registration number (e.g., CSU/2024/001)')
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('First Name')
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('Last Name')
    )
    email = models.EmailField(
        verbose_name=_('Email Address')
    )
    
    # Role Information - This is the dropdown field
    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default='PM',
        verbose_name=_('Role'),
        help_text=_('Select the team member role from the dropdown')
    )
    contribution = models.TextField(
        verbose_name=_('Contribution'),
        help_text=_('Describe what this member contributed to the project.')
    )
    
    # Optional Information
    bio = models.TextField(
        blank=True,
        verbose_name=_('Biography'),
        help_text=_('Short professional biography (optional).')
    )
    photo = models.ImageField(
        upload_to='team/photos/',
        blank=True,
        verbose_name=_('Photo'),
        help_text=_('Professional headshot (optional). Recommended: 400x400px.')
    )
    linkedin_url = models.URLField(
        blank=True,
        verbose_name=_('LinkedIn URL')
    )
    github_url = models.URLField(
        blank=True,
        verbose_name=_('GitHub URL')
    )
    
    # Display Order
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Display Order'),
        help_text=_('Lower numbers appear first. Use 0, 1, 2, 3...')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active'),
        help_text=_('Show this member on the website.')
    )
    
    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')
        ordering = ['order', 'last_name', 'first_name']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.get_role_display()}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_role_short(self):
        """Return short role name without description"""
        role_map = {
            'PM': 'Project Manager',
            'PR': 'Presenter',
            'EV': 'Evaluator',
            'CO': 'Coder',
            'DE': 'Designer',
            'RE': 'Researcher',
        }
        return role_map.get(self.role, self.role)