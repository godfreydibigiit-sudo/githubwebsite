"""
Models for team members and roles.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class TeamMember(models.Model):
    """
    Team member profile for the HCI project.
    """
    class Role(models.TextChoices):
        PROJECT_MANAGER = 'project_manager', _('Project Manager')
        DESIGNER = 'designer', _('Designer')
        EVALUATOR = 'evaluator', _('Evaluator')
        CODER = 'coder', _('Coder')
        RESEARCHER = 'researcher', _('Researcher')
        PRESENTER = 'presenter', _('Presenter')
    
    # Personal Information
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('Registration Number')
    )
    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    
    # Role
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        verbose_name=_('Role')
    )
    role_description = models.TextField(
        verbose_name=_('Role Description'),
        help_text=_('Detailed description of responsibilities'),
        blank=True
    )
    
    # Contribution
    contribution = models.TextField(
        verbose_name=_('Contribution'),
        help_text=_('Specific contributions to the project')
    )
    
    # Profile
    photo = models.ImageField(
        upload_to='team/photos/',
        verbose_name=_('Photo'),
        blank=True,
        help_text=_('Professional headshot or photo')
    )
    bio = models.TextField(
        verbose_name=_('Biography'),
        blank=True,
        help_text=_('Short professional bio')
    )
    
    # Skills
    skills = models.TextField(
        verbose_name=_('Skills'),
        blank=True,
        help_text=_('Relevant skills for HCI, comma separated')
    )
    
    # Social Links
    github_url = models.URLField(verbose_name=_('GitHub URL'), blank=True)
    linkedin_url = models.URLField(verbose_name=_('LinkedIn URL'), blank=True)
    portfolio_url = models.URLField(verbose_name=_('Portfolio URL'), blank=True)
    
    # Meta
    is_active = models.BooleanField(default=True, verbose_name=_('Active Member'))
    is_leader = models.BooleanField(default=False, verbose_name=_('Team Leader'))
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')
        ordering = ['order', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"
    
    @property
    def full_name(self):
        """Return full name."""
        return f"{self.first_name} {self.last_name}"
    
    @property
    def initials(self):
        """Return initials."""
        return f"{self.first_name[0]}{self.last_name[0]}".upper()
    
    @property
    def skill_list(self):
        """Return skills as a list."""
        if self.skills:
            return [s.strip() for s in self.skills.split(',')]
        return []