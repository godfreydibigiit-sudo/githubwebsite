/**
 * AOS-INIT.JS - Animate On Scroll Configuration
 * Professional Scroll Animation Setup
 */
(function() {
    'use strict';

    // ============ AOS CONFIGURATION ============
    const aosConfig = {
        // Animation duration
        duration: 800,
        
        // Animation delay
        delay: 0,
        
        // Trigger offset from viewport
        offset: 120,
        
        // Trigger once or every time
        once: true,
        
        // Mirror animations on scroll up
        mirror: false,
        
        // Anchor placement
        anchorPlacement: 'top-bottom',
        
        // Disable on mobile (optional)
        disable: false,
        
        // Disable on reduced motion
        disableMutationObserver: false,
        
        // Custom easing
        easing: 'ease-in-out',
        
        // Start event
        startEvent: 'DOMContentLoaded',
        
        // CSS selector for disabled elements
        disableSelector: '.no-aos'
    };

    // ============ INITIALIZE ============
    function initAOS() {
        // Check if AOS is available
        if (typeof AOS !== 'undefined') {
            AOS.init(aosConfig);
        } else {
            console.warn('AOS library not loaded. Scroll animations disabled.');
        }
    }

    // ============ REFRESH ON DYNAMIC CONTENT ============
    function refreshAOS() {
        if (typeof AOS !== 'undefined') {
            AOS.refresh();
        }
    }

    // ============ RESPECT REDUCED MOTION ============
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    
    function handleReducedMotion(e) {
        if (e.matches) {
            // Disable animations
            aosConfig.disable = true;
            aosConfig.duration = 0;
            document.querySelectorAll('[data-aos]').forEach(el => {
                el.removeAttribute('data-aos');
            });
        } else {
            // Re-enable animations
            aosConfig.disable = false;
            aosConfig.duration = 800;
        }
        refreshAOS();
    }
    
    motionQuery.addEventListener('change', handleReducedMotion);

    // ============ INITIALIZE ON LOAD ============
    document.addEventListener('DOMContentLoaded', function() {
        // Check reduced motion preference
        if (motionQuery.matches) {
            handleReducedMotion(motionQuery);
        } else {
            initAOS();
        }
    });

    // ============ EXPORT REFRESH FUNCTION ============
    window.refreshAOS = refreshAOS;

})();