/**
 * LANGUAGE-SWITCHER.JS - Internationalization (i18n)
 * English & Kiswahili Translation Support
 */
(function() {
    'use strict';

    // ============ LANGUAGE MANAGER ============
    const LanguageManager = {
        // Available languages
        languages: {
            en: {
                code: 'en',
                name: 'English',
                nativeName: 'English',
                flag: '🇬🇧'
            },
            sw: {
                code: 'sw',
                name: 'Swahili',
                nativeName: 'Kiswahili',
                flag: '🇹🇿'
            }
        },
        
        // Get current language
        getLanguage: function() {
            const savedLang = localStorage.getItem('hci-language');
            if (savedLang && this.languages[savedLang]) {
                return savedLang;
            }
            
            // Check browser language
            const browserLang = navigator.language.split('-')[0];
            if (this.languages[browserLang]) {
                return browserLang;
            }
            
            // Default: English
            return 'en';
        },
        
        // Set language
        setLanguage: function(langCode) {
            if (!this.languages[langCode]) return;
            
            // Save preference
            localStorage.setItem('hci-language', langCode);
            
            // Update HTML lang attribute
            document.documentElement.lang = langCode;
            
            // Update language switcher
            this.updateSwitchers(langCode);
            
            // Reload page with new language (Django i18n)
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.set('lang', langCode);
            
            // Dispatch event
            document.dispatchEvent(new CustomEvent('languageChanged', {
                detail: { language: langCode }
            }));
            
            // Redirect to same page with new language
            window.location.href = currentUrl.toString();
        },
        
        // Update all language switchers
        updateSwitchers: function(langCode) {
            const switchers = document.querySelectorAll('.language-switcher select');
            
            switchers.forEach(select => {
                select.value = langCode;
            });
        },
        
        // Create language switcher HTML
        createSwitcher: function() {
            const currentLang = this.getLanguage();
            const lang = this.languages[currentLang];
            
            return `
                <div class="language-switcher">
                    <select onchange="LanguageManager.setLanguage(this.value)" 
                            aria-label="Select Language">
                        ${Object.values(this.languages).map(l => `
                            <option value="${l.code}" ${l.code === currentLang ? 'selected' : ''}>
                                ${l.flag} ${l.nativeName}
                            </option>
                        `).join('')}
                    </select>
                </div>
            `;
        },
        
        // Initialize
        init: function() {
            const currentLang = this.getLanguage();
            document.documentElement.lang = currentLang;
            this.updateSwitchers(currentLang);
        }
    };

    // ============ INITIALIZE ============
    document.addEventListener('DOMContentLoaded', function() {
        LanguageManager.init();
    });

    // ============ EXPORT ============
    window.LanguageManager = LanguageManager;

})();