/**
 * PARTICLES-CONFIG.JS - Hero Section Particle Animation
 * IT.CO.TZ Inspired Network/Dot Pattern
 */
(function() {
    'use strict';

    // ============ PARTICLES CONFIGURATION ============
    const particlesConfig = {
        // Particle settings
        particles: {
            number: {
                value: 80,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: '#00E5FF'
            },
            shape: {
                type: 'circle',
                stroke: {
                    width: 0,
                    color: '#000000'
                }
            },
            opacity: {
                value: 0.5,
                random: true,
                anim: {
                    enable: true,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                }
            },
            size: {
                value: 3,
                random: true,
                anim: {
                    enable: true,
                    speed: 2,
                    size_min: 0.1,
                    sync: false
                }
            },
            line_linked: {
                enable: true,
                distance: 150,
                color: '#00E5FF',
                opacity: 0.2,
                width: 1
            },
            move: {
                enable: true,
                speed: 1,
                direction: 'none',
                random: true,
                straight: false,
                out_mode: 'out',
                bounce: false,
                attract: {
                    enable: true,
                    rotateX: 600,
                    rotateY: 1200
                }
            }
        },
        
        // Interaction settings
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: {
                    enable: true,
                    mode: 'grab'
                },
                onclick: {
                    enable: true,
                    mode: 'push'
                },
                resize: true
            },
            modes: {
                grab: {
                    distance: 140,
                    line_linked: {
                        opacity: 0.5
                    }
                },
                push: {
                    particles_nb: 4
                }
            }
        },
        
        // Retina display
        retina_detect: true
    };

    // ============ INITIALIZE ============
    function initParticles() {
        const particlesContainer = document.getElementById('particles-js');
        
        if (!particlesContainer) return;
        
        // Check if particles.js is loaded
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', particlesConfig);
        } else {
            console.warn('particles.js not loaded. Hero animation disabled.');
            particlesContainer.style.display = 'none';
        }
    }

    // ============ THEME-AWARE PARTICLES ============
    function updateParticlesColor(theme) {
        const particlesContainer = document.getElementById('particles-js');
        
        if (!particlesContainer) return;
        
        const color = theme === 'dark' ? '#00E5FF' : '#0097A7';
        
        // Update config
        particlesConfig.particles.color.value = color;
        particlesConfig.particles.line_linked.color = color;
        
        // Reinitialize with new colors
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', particlesConfig);
        }
    }

    // ============ LISTEN FOR THEME CHANGES ============
    document.addEventListener('themeChanged', function(e) {
        updateParticlesColor(e.detail.theme);
    });

    // ============ INITIALIZE ON LOAD ============
    document.addEventListener('DOMContentLoaded', function() {
        initParticles();
    });

})();