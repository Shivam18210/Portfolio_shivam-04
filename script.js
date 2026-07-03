/* ==========================================================================
   SHIVAM RAJPUT PORTFOLIO INTERACTION ENGINE (SCRIPT.JS)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

    /* ==========================================
       1. HEADER STICKY & SCROLL PROGRESS BAR
       ========================================== */
    const header = document.getElementById('navbar-header');
    const scrollProgress = document.getElementById('scroll-progress');
    
    window.addEventListener('scroll', () => {
        // Sticky Header Toggle
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Scroll Progress Bar Update
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        scrollProgress.style.width = scrolled + '%';
    });


    /* ==========================================
       2. MOBILE OVERLAY MENU DRAWER
       ========================================== */
    const hamburger = document.getElementById('nav-hamburger');
    const mobileMenu = document.getElementById('mobile-menu-overlay');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');

    function toggleMobileMenu() {
        const isOpen = hamburger.classList.toggle('open');
        mobileMenu.classList.toggle('open');
        hamburger.setAttribute('aria-expanded', isOpen);
    }

    function closeMobileMenu() {
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
    }

    hamburger.addEventListener('click', toggleMobileMenu);

    // Close mobile menu on clicking any navigation link
    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    // Close mobile menu on resize to desktop view
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            closeMobileMenu();
        }
    });


    /* ==========================================
       3. TYPING SUBTITLE HERO ANIMATION
       ========================================== */
    const typewriterElement = document.getElementById('typewriter-text');
    const roles = ["Web Developer", "Python Backend Developer", "React.js Developer", "FastAPI Engineer"];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function handleTypewriter() {
        const currentRole = roles[roleIndex];
        
        if (isDeleting) {
            // Deleting character
            typewriterElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 50; // faster deleting
        } else {
            // Adding character
            typewriterElement.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 150; // normal typing
        }

        // State Check: Word fully typed
        if (!isDeleting && charIndex === currentRole.length) {
            isDeleting = true;
            typingSpeed = 2000; // Pause at the end of the word
        } 
        // State Check: Word fully deleted
        else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typingSpeed = 500; // Small pause before typing next word
        }

        setTimeout(handleTypewriter, typingSpeed);
    }

    if (typewriterElement) {
        handleTypewriter();
    }


    /* ==========================================
       4. SCROLL-SPY NAVBAR LINK HIGHLIGHTER
       ========================================== */
    const sections = document.querySelectorAll('.scroll-section');
    const desktopLinks = document.querySelectorAll('.nav-link');
    const mobLinks = document.querySelectorAll('.mobile-nav-link');

    function highlightActiveSection() {
        let currentSectionId = 'home';
        const scrollPosition = window.scrollY + 150; // Offset for navbar header

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        // Highlight Desktop Navbar Link
        desktopLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });

        // Highlight Mobile Navbar Link
        mobLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    }

    window.addEventListener('scroll', highlightActiveSection);
    highlightActiveSection(); // Run once on startup


    /* ==========================================
       5. INTERSECTION OBSERVER FOR ENTRANCE REVEALS
       ========================================== */
    // Scroll Entrance Animations (fade-in-element)
    const fadeElements = document.querySelectorAll('.fade-in-element');
    
    const elementObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal');
                observer.unobserve(entry.target); // Trigger only once
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    fadeElements.forEach(el => {
        elementObserver.observe(el);
    });

    // Skill Bar Fill Animations Observer
    const skillBars = document.querySelectorAll('.skill-bar-fill');
    
    const skillObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetFill = entry.target;
                const targetPercentage = targetFill.getAttribute('data-progress');
                targetFill.style.width = targetPercentage;
                observer.unobserve(targetFill);
            }
        });
    }, {
        threshold: 0.2
    });

    skillBars.forEach(bar => {
        skillObserver.observe(bar);
    });


    /* ==========================================
       6. PROJECTS GALLERY DYNAMIC FILTER SYSTEM
       ========================================== */
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active state from current button, add to clicked button
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                
                // Add fade out state, filter, and fade in
                card.style.opacity = '0';
                card.style.transform = 'scale(0.95)';

                setTimeout(() => {
                    if (filterValue === 'all' || cardCategory === filterValue) {
                        card.classList.remove('hidden');
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        card.classList.add('hidden');
                    }
                }, 300);
            });
        });
    });


    /* ==========================================
       7. CONTACT FORM VALIDATOR & TOAST SYSTEM
       ========================================== */
    const contactForm = document.getElementById('contact-form');
    const toastContainer = document.getElementById('toast-container');

    // Float Form Group error helpers
    const nameInput = document.getElementById('form-name');
    const emailInput = document.getElementById('form-email');
    const subjectInput = document.getElementById('form-subject');
    const messageInput = document.getElementById('form-message');

    // Validate Specific Form Fields
    function validateField(input, errorElementId, validationFn) {
        const formGroup = input.parentElement;
        const isValid = validationFn(input.value.trim());

        if (!isValid) {
            formGroup.classList.add('invalid');
            return false;
        } else {
            formGroup.classList.remove('invalid');
            return true;
        }
    }

    // Email Pattern validator
    function isEmailValid(email) {
        const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return pattern.test(email);
    }

    // Bind real-time input checkups
    nameInput.addEventListener('input', () => {
        validateField(nameInput, 'error-name', (val) => val.length > 0);
    });

    emailInput.addEventListener('input', () => {
        validateField(emailInput, 'error-email', (val) => isEmailValid(val));
    });

    subjectInput.addEventListener('input', () => {
        validateField(subjectInput, 'error-subject', (val) => val.length > 0);
    });

    messageInput.addEventListener('input', () => {
        validateField(messageInput, 'error-message', (val) => val.length > 0);
    });

    // Custom Dynamic Toast Launcher
    function launchToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        const iconClass = type === 'success' ? 'fa-circle-check' : 'fa-circle-exclamation';
        toast.innerHTML = `
            <i class="fa-solid ${iconClass} toast-icon"></i>
            <span>${message}</span>
        `;
        
        toastContainer.appendChild(toast);
        
        // Slide Toast In
        setTimeout(() => {
            toast.classList.add('show');
        }, 100);
        
        // Remove Toast after delay
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toast.remove();
            }, 400);
        }, 4000);
    }

    // Bind Form Submit Triggers
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Run final check validations
            const isNameOk = validateField(nameInput, 'error-name', (val) => val.length > 0);
            const isEmailOk = validateField(emailInput, 'error-email', (val) => isEmailValid(val));
            const isSubjectOk = validateField(subjectInput, 'error-subject', (val) => val.length > 0);
            const isMessageOk = validateField(messageInput, 'error-message', (val) => val.length > 0);

            if (isNameOk && isEmailOk && isSubjectOk && isMessageOk) {
                // Success Mock submission!
                launchToast(`Thanks, ${nameInput.value}! Your message has been sent successfully.`, 'success');
                
                // Clear Form Fields cleanly
                contactForm.reset();
                
                // Remove form invalid overlays
                document.querySelectorAll('.form-group').forEach(grp => {
                    grp.classList.remove('invalid');
                });
            } else {
                launchToast('Please fill out all contact fields correctly.', 'error');
            }
        });
    }


    /* ==========================================
       8. FLOATING BACK TO TOP BUTTON LOGIC
       ========================================== */
    const backToTopBtn = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

});
