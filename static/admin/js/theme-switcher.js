/**
 * JAZZMIN THEME SWITCHER
 * IT.CO.TZ Inspired Dark/Light Mode Toggle
 */
(function() {
    'use strict';

    const ThemeSwitcher = {
        // Available themes
        themes: {
            dark: {
                name: 'Dark Mode',
                icon: 'fas fa-moon',
                next: 'light',
                navbar: 'navbar-dark',
                sidebar: 'sidebar-dark-cyan',
                theme: 'darkly'
            },
            light: {
                name: 'Light Mode',
                icon: 'fas fa-sun',
                next: 'dark',
                navbar: 'navbar-white',
                sidebar: 'sidebar-light-cyan',
                theme: 'flatly'
            }
        },

        // Get current theme
        getTheme: function() {
            return localStorage.getItem('admin-theme') || 'dark';
        },

        // Set theme
        setTheme: function(themeName) {
            const theme = this.themes[themeName];
            if (!theme) return;

            // Save preference
            localStorage.setItem('admin-theme', themeName);

            // Apply to body
            document.body.className = document.body.className
                .replace(/theme-\w+/g, '')
                .replace(/sidebar-\w+(-\w+)?/g, '')
                .replace(/navbar-\w+/g, '');
            
            document.body.classList.add(
                'theme-' + theme.theme,
                theme.sidebar,
                theme.navbar
            );

            // Update toggle button
            this.updateButton(themeName);

            // Dispatch event
            document.dispatchEvent(new CustomEvent('themeChanged', {
                detail: { theme: themeName }
            }));
        },

        // Toggle theme
        toggle: function() {
            const current = this.getTheme();
            const next = this.themes[current].next;
            this.setTheme(next);
        },

        // Update button
        updateButton: function(themeName) {
            const theme = this.themes[themeName];
            const buttons = document.querySelectorAll('.theme-switcher-btn');
            
            buttons.forEach(btn => {
                const icon = btn.querySelector('i');
                const text = btn.querySelector('.theme-text');
                
                if (icon) {
                    icon.className = theme.icon;
                }
                if (text) {
                    text.textContent = theme.name;
                }
            });
        },

        // Create button HTML
        createButton: function() {
            const currentTheme = this.getTheme();
            const theme = this.themes[currentTheme];
            
            return `
                <button class="btn theme-switcher-btn" 
                        onclick="AdminThemeSwitcher.toggle()" 
                        title="Switch Theme"
                        style="background: rgba(0,229,255,0.1); 
                               border: 1px solid rgba(0,229,255,0.3); 
                               color: #00E5FF; 
                               border-radius: 50px; 
                               padding: 6px 16px;
                               font-size: 0.85rem;
                               transition: all 0.3s ease;
                               cursor: pointer;">
                    <i class="${theme.icon} me-2"></i>
                    <span class="theme-text">${theme.name}</span>
                </button>
            `;
        },

        // Initialize
        init: function() {
            const currentTheme = this.getTheme();
            this.setTheme(currentTheme);

            // Add button to navbar
            this.injectButton();
        },

        // Inject button into navbar
        injectButton: function() {
            // Try multiple selectors for Jazzmin navbar
            const targets = [
                '.navbar .navbar-nav.ml-auto',
                '.navbar .navbar-nav:last-child',
                '.navbar-nav[class*="order-1"]',
                '.main-header .navbar-nav'
            ];

            let navContainer = null;
            for (const selector of targets) {
                navContainer = document.querySelector(selector);
                if (navContainer) break;
            }

            if (navContainer) {
                const li = document.createElement('li');
                li.className = 'nav-item d-flex align-items-center ms-2';
                li.innerHTML = this.createButton();
                navContainer.appendChild(li);
            }
        }
    };

    // Initialize on load
    document.addEventListener('DOMContentLoaded', function() {
        // Wait for Jazzmin to fully load
        setTimeout(() => {
            ThemeSwitcher.init();
        }, 500);
    });

    // Export globally
    window.AdminThemeSwitcher = ThemeSwitcher;

})();
