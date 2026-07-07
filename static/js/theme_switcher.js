/**
 * THEME-SWITCHER.JS - Dark/Light Mode Toggle
 * Professional Implementation with Local Storage
 */
(function() {
    'use strict';

    // ============ THEME MANAGER ============
    const ThemeManager = {
        // Get current theme
        getTheme: function() {
            // Check localStorage first
            const savedTheme = localStorage.getItem('hci-theme');
            if (savedTheme) return savedTheme;
            
            // Check system preference
            if (window.matchMedia('(prefers-color-scheme: light)').matches) {
                return 'light';
            }
            
            // Default: dark (IT.CO.TZ style)
            return 'dark';
        },
        
        // Set theme
        setTheme: function(theme) {
            // Validate theme
            if (theme !== 'dark' && theme !== 'light') {
                theme = 'dark';
            }
            
            // Apply theme
            document.documentElement.setAttribute('data-theme', theme);
            
            // Save preference
            localStorage.setItem('hci-theme', theme);
            
            // Update toggle button
            this.updateToggleButton(theme);
            
            // Dispatch event
            document.dispatchEvent(new CustomEvent('themeChanged', {
                detail: { theme: theme }
            }));
        },
        
        // Toggle theme
        toggleTheme: function() {
            const currentTheme = this.getTheme();
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            this.setTheme(newTheme);
            return newTheme;
        },
        
        // Update toggle button
        updateToggleButton: function(theme) {
            const toggleBtns = document.querySelectorAll('.theme-toggle');
            
            toggleBtns.forEach(btn => {
                const icon = btn.querySelector('i');
                if (!icon) return;
                
                if (theme === 'dark') {
                    icon.className = 'fas fa-sun';
                    btn.setAttribute('title', 'Switch to Light Mode');
                } else {
                    icon.className = 'fas fa-moon';
                    btn.setAttribute('title', 'Switch to Dark Mode');
                }
            });
        },
        
        // Initialize
        init: function() {
            // Apply saved theme on load
            const currentTheme = this.getTheme();
            this.setTheme(currentTheme);
            
            // Add click handlers to all theme toggles
            document.querySelectorAll('.theme-toggle').forEach(btn => {
                btn.addEventListener('click', () => {
                    // Add rotation animation
                    btn.style.transition = 'transform 0.5s ease';
                    btn.style.transform = 'rotate(360deg)';
                    
                    setTimeout(() => {
                        btn.style.transform = 'rotate(0deg)';
                    }, 500);
                    
                    this.toggleTheme();
                });
            });
            
            // Listen for system theme changes
            window.matchMedia('(prefers-color-scheme: dark)')
                .addEventListener('change', (e) => {
                    // Only update if user hasn't manually set preference
                    if (!localStorage.getItem('hci-theme')) {
                        this.setTheme(e.matches ? 'dark' : 'light');
                    }
                });
        }
    };

    // ============ INITIALIZE ============
    document.addEventListener('DOMContentLoaded', function() {
        ThemeManager.init();
    });

    // ============ EXPORT ============
    window.ThemeManager = ThemeManager;

})();