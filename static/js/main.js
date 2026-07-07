/**
 * MAIN.JS - Core Functionality
 * Professional Portfolio Website
 */
(function() {
    'use strict';

    // ============ DOM READY ============
    document.addEventListener('DOMContentLoaded', function() {
        initNavigation();
        initBackToTop();
        initSmoothScroll();
        initActiveNavLink();
        initCardHover();
        initPrototypeGallery();
        initLazyLoading();
    });

    // ============ NAVIGATION ============
    function initNavigation() {
        const navbar = document.querySelector('.navbar');
        
        if (!navbar) return;
        
        // Scroll effect
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
        
        // Close mobile menu on link click
        const navLinks = document.querySelectorAll('.nav-link');
        const navbarCollapse = document.querySelector('.navbar-collapse');
        const navbarToggler = document.querySelector('.navbar-toggler');
        
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }

    // ============ BACK TO TOP ============
    function initBackToTop() {
        const backToTop = document.querySelector('.back-to-top');
        
        if (!backToTop) return;
        
        window.addEventListener('scroll', function() {
            if (window.scrollY > 500) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });
        
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ============ SMOOTH SCROLL ============
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                
                if (target) {
                    const offset = 80; // Header height
                    const position = target.getBoundingClientRect().top + window.pageYOffset - offset;
                    
                    window.scrollTo({
                        top: position,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    // ============ ACTIVE NAV LINK ============
    function initActiveNavLink() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');
        
        if (!sections.length || !navLinks.length) return;
        
        window.addEventListener('scroll', function() {
            let current = '';
            const scrollY = window.scrollY + 100;
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                
                if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                    current = section.getAttribute('id');
                }
            });
            
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });
    }

    // ============ CARD HOVER EFFECT ============
    function initCardHover() {
        document.querySelectorAll('.card').forEach(card => {
            card.addEventListener('mousemove', function(e) {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                card.style.setProperty('--mouse-x', `${x}px`);
                card.style.setProperty('--mouse-y', `${y}px`);
            });
        });
    }

    // ============ PROTOTYPE IMAGE GALLERY ============
    function initPrototypeGallery() {
        const prototypeImages = document.querySelectorAll('.prototype-gallery img');
        
        prototypeImages.forEach(img => {
            img.addEventListener('click', function() {
                openLightbox(this.src, this.alt);
            });
        });
    }

    function openLightbox(src, alt) {
        const lightbox = document.createElement('div');
        lightbox.className = 'lightbox-overlay';
        lightbox.innerHTML = `
            <div class="lightbox-container">
                <button class="lightbox-close">&times;</button>
                <img src="${src}" alt="${alt}" class="lightbox-image">
                <p class="lightbox-caption">${alt}</p>
            </div>
        `;
        
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox || e.target.classList.contains('lightbox-close')) {
                document.body.removeChild(lightbox);
            }
        });
        
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                if (document.querySelector('.lightbox-overlay')) {
                    document.body.removeChild(lightbox);
                }
            }
        });
        
        document.body.appendChild(lightbox);
    }

    // ============ LAZY LOADING ============
    function initLazyLoading() {
        const images = document.querySelectorAll('img[data-src]');
        
        if (!images.length) return;
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute('data-src');
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px'
        });
        
        images.forEach(img => imageObserver.observe(img));
    }

    // ============ WINDOW LOAD ============
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
        
        // Remove preloader if exists
        const preloader = document.querySelector('.preloader');
        if (preloader) {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500);
        }
    });

})();