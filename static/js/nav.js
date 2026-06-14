(function () {
  'use strict';

  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');
  const navOverlay = document.getElementById('navOverlay');
  const header = document.querySelector('header');
  const backToTop = document.getElementById('backToTop');

  function closeMenu() {
    navLinks?.classList.remove('open');
    menuToggle?.classList.remove('open');
    navOverlay?.classList.remove('visible');
    document.body.style.overflow = '';
  }

  function openMenu() {
    navLinks?.classList.add('open');
    menuToggle?.classList.add('open');
    navOverlay?.classList.add('visible');
    document.body.style.overflow = 'hidden';
  }

  menuToggle?.addEventListener('click', () => {
    if (navLinks?.classList.contains('open')) closeMenu();
    else openMenu();
  });

  navOverlay?.addEventListener('click', closeMenu);
  navLinks?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  window.addEventListener('scroll', () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 20);
    if (backToTop) backToTop.classList.toggle('visible', window.scrollY > 400);
  });

  backToTop?.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  const sections = document.querySelectorAll('section[id], main[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

  if (sections.length && navAnchors.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            navAnchors.forEach((a) => {
              a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
            });
          }
        });
      },
      { rootMargin: '-40% 0px -55% 0px' }
    );
    sections.forEach((s) => observer.observe(s));
  }

  document.querySelectorAll('.reveal').forEach((el, i) => {
    el.style.transitionDelay = `${i * 0.08}s`;
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealObserver.observe(el);
  });
})();
