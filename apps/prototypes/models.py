"""
Models for all fidelity prototypes - Low, Medium, and High fidelity.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel


class LowFidelityPrototype(models.Model):
    """
    Hand sketches and paper wireframes - Assignment #2.
    """
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Title (Swahili)'), blank=True)
    page_name = models.CharField(
        max_length=100,
        verbose_name=_('Page/Screen Name'),
        help_text=_('e.g., Home Page, Login Screen, Dashboard')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Explain the sketch, what it represents, and design decisions')
    )
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    # Sketch Image
    sketch_image = models.ImageField(
        upload_to='prototypes/low-fi/',
        verbose_name=_('Sketch Image'),
        help_text=_('Upload clear photo/scan of hand sketch')
    )
    
    # Design Notes
    design_rationale = models.TextField(
        verbose_name=_('Design Rationale'),
        blank=True,
        help_text=_('Why this design approach was chosen')
    )
    user_interactions = models.TextField(
        verbose_name=_('User Interactions'),
        blank=True,
        help_text=_('Describe how users will interact with this screen')
    )
    
    # Meta
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Low-Fidelity Prototype')
        verbose_name_plural = _('Low-Fidelity Prototypes')
        ordering = ['order']
    
    def __str__(self):
        return f"Low-Fi: {self.page_name} - {self.title}"


class MediumFidelityPrototype(models.Model):
    """
    Digital wireframes with navigation flow - Assignment #3.
    """
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Title (Swahili)'), blank=True)
    page_name = models.CharField(
        max_length=100,
        verbose_name=_('Page/Screen Name')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Describe the wireframe and its functionality')
    )
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    # Wireframe Image
    wireframe_image = models.ImageField(
        upload_to='prototypes/med-fi/',
        verbose_name=_('Wireframe Image')
    )
    
    # Navigation
    navigation_flow = models.TextField(
        verbose_name=_('Navigation Flow'),
        help_text=_('Describe how users navigate to and from this screen')
    )
    connected_screens = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        verbose_name=_('Connected Screens'),
        help_text=_('Other screens this wireframe links to')
    )
    
    # Improvements from Low-Fi
    improvements_from_lowfi = models.TextField(
        verbose_name=_('Improvements from Low-Fidelity'),
        help_text=_('What changed from the paper sketches and why')
    )
    improvements_from_lowfi_sw = models.TextField(
        verbose_name=_('Improvements from Low-Fidelity (Swahili)'),
        blank=True
    )
    
    # Reference to Low-Fi
    lowfi_reference = models.ForeignKey(
        LowFidelityPrototype,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='mediumfi_versions',
        verbose_name=_('Low-Fi Reference'),
        help_text=_('Link to the original low-fidelity sketch')
    )
    
    # Meta
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Medium-Fidelity Prototype')
        verbose_name_plural = _('Medium-Fidelity Prototypes')
        ordering = ['order']
    
    def __str__(self):
        return f"Med-Fi: {self.page_name} - {self.title}"


class HighFidelityPrototype(models.Model):
    """
    Final UI screens with full styling - Assignment #4.
    """
    class ScreenType(models.TextChoices):
        HOME = 'home', _('Home Page')
        DASHBOARD = 'dashboard', _('Dashboard')
        LOGIN = 'login', _('Login/Register')
        PROFILE = 'profile', _('User Profile')
        LIST = 'list', _('List View')
        DETAIL = 'detail', _('Detail View')
        FORM = 'form', _('Form/Input')
        SETTINGS = 'settings', _('Settings')
        OTHER = 'other', _('Other')
    
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    title_sw = models.CharField(max_length=200, verbose_name=_('Title (Swahili)'), blank=True)
    page_name = models.CharField(max_length=100, verbose_name=_('Page/Screen Name'))
    screen_type = models.CharField(
        max_length=20,
        choices=ScreenType.choices,
        default=ScreenType.OTHER,
        verbose_name=_('Screen Type')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Detailed explanation of this screen')
    )
    description_sw = models.TextField(verbose_name=_('Description (Swahili)'), blank=True)
    
    # Screenshot
    screenshot = models.ImageField(
        upload_to='prototypes/high-fi/',
        verbose_name=_('Screenshot')
    )
    additional_screenshots = models.ManyToManyField(
        'HighFiScreenshot',
        blank=True,
        related_name='highfi_prototypes'
    )
    
    # Design Details
    color_palette = models.TextField(
        verbose_name=_('Color Palette'),
        blank=True,
        help_text=_('Hex codes and color usage')
    )
    typography = models.TextField(
        verbose_name=_('Typography'),
        blank=True,
        help_text=_('Fonts, sizes, and usage')
    )
    interaction_details = models.TextField(
        verbose_name=_('Interaction Details'),
        blank=True,
        help_text=_('Animations, transitions, micro-interactions')
    )
    design_system_notes = models.TextField(
        verbose_name=_('Design System Notes'),
        blank=True,
        help_text=_('Components, patterns, and design decisions')
    )
    
    # Reference to Med-Fi
    medfi_reference = models.ForeignKey(
        MediumFidelityPrototype,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='highfi_versions',
        verbose_name=_('Med-Fi Reference')
    )
    
    # Meta
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    order = models.IntegerField(default=0, verbose_name=_('Display Order'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('High-Fidelity Prototype')
        verbose_name_plural = _('High-Fidelity Prototypes')
        ordering = ['order']
    
    def __str__(self):
        return f"Hi-Fi: {self.page_name} - {self.title}"


class HighFiScreenshot(models.Model):
    """
    Additional screenshots for high-fidelity prototypes.
    """
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    image = models.ImageField(upload_to='prototypes/high-fi/extra/')
    caption = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('Additional Screenshot')
        verbose_name_plural = _('Additional Screenshots')
        ordering = ['order']
    
    def __str__(self):
        return self.title


class DesignIteration(models.Model):
    """
    Track design changes between fidelity levels.
    """
    title = models.CharField(max_length=200, verbose_name=_('Change Title'))
    description = models.TextField(verbose_name=_('What Changed'))
    reason = models.TextField(verbose_name=_('Why It Changed'))
    
    # Before/After
    before_image = models.ImageField(
        upload_to='prototypes/iterations/before/',
        verbose_name=_('Before Screenshot')
    )
    after_image = models.ImageField(
        upload_to='prototypes/iterations/after/',
        verbose_name=_('After Screenshot')
    )
    
    # Links to prototypes
    lowfi = models.ForeignKey(
        LowFidelityPrototype,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    mediumfi = models.ForeignKey(
        MediumFidelityPrototype,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    highfi = models.ForeignKey(
        HighFidelityPrototype,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Design Iteration')
        verbose_name_plural = _('Design Iterations')
        ordering = ['order']
    
    def __str__(self):
        return self.title