import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-hci-portfolio-dev-key-2026')

DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'jazzmin', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Local apps
    'apps.core',
    'apps.pages',
    'apps.requirements',
    'apps.research',
    'apps.prototypes',
    'apps.evaluations',
    'apps.team',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.ThemeMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ============================================
# JAZZMIN SETTINGS - Professional Admin Panel
# IT.CO.TZ Inspired Design System
# ============================================

# ============================================
# JAZZMIN SETTINGS - Professional Admin Panel
# ============================================

JAZZMIN_SETTINGS = {
    # Site Configuration
    "site_title": "HCI Portfolio Admin",
    "site_header": "HCI Portfolio",
    "site_brand": "HCI Portfolio",
    "welcome_sign": "Welcome to HCI Portfolio Admin Panel",
    "copyright": "IFM - Faculty of Computing, Information Systems and Mathematics",
    
    # Search (Fixed format - use "app_label.model_name")
    "search_model": [
        "auth.User",
        "team.TeamMember",
    ],
    
    # Top Menu
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Website", "url": "/en/", "new_window": True},
    ],
    
    # User Menu
    "usermenu_links": [
        {"name": "View Website", "url": "/en/", "new_window": True, "icon": "fas fa-globe"},
    ],
    
    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    
    # Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        
        "pages": "fas fa-file-alt",
        "pages.sitesetting": "fas fa-cog",
        "pages.aboutsection": "fas fa-info-circle",
        "pages.projectobjective": "fas fa-bullseye",
        "pages.usergroup": "fas fa-user-friends",
        
        "requirements": "fas fa-clipboard-list",
        "requirements.functionalrequirement": "fas fa-check-circle",
        "requirements.nonfunctionalrequirement": "fas fa-shield-alt",
        
        "research": "fas fa-search",
        "research.competitorsystem": "fas fa-building",
        "research.problemfound": "fas fa-exclamation-triangle",
        "research.opportunity": "fas fa-lightbulb",
        "research.researchfinding": "fas fa-chart-line",
        
        "prototypes": "fas fa-pencil-ruler",
        "prototypes.lowfidelityprototype": "fas fa-pencil-alt",
        "prototypes.mediumfidelityprototype": "fas fa-wireframe",
        "prototypes.highfidelityprototype": "fas fa-desktop",
        "prototypes.designiteration": "fas fa-sync-alt",
        
        "evaluations": "fas fa-clipboard-check",
        "evaluations.heuristicevaluation": "fas fa-check-double",
        "evaluations.heuristic": "fas fa-bookmark",
        "evaluations.evaluationfinding": "fas fa-bug",
        "evaluations.poster": "fas fa-image",
        
        "team": "fas fa-users",
        "team.teammember": "fas fa-user-tie",
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    # UI Features
    "related_modal_active": True,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "language_chooser": True,
    "custom_css": [
        "admin/css/admin-custom.css",
        "admin/css/admin-theme.css",
    ],
}



# ============================================
# JAZZMIN UI TWEAKS
# ============================================

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-cyan",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-cyan",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": True,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'apps.core.context_processors.site_settings',
                'apps.core.context_processors.theme_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('sw', 'Kiswahili'),
]

LOCALE_PATHS = [BASE_DIR / 'locale']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
