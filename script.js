// Current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// ----- Icon placeholders: show image when src is set -----
function checkImg(el, wrapClass) {
  const wrap = el?.closest(wrapClass);
  if (!el || !wrap) return;
  const hasSrc = el.getAttribute('src') && el.getAttribute('src').trim() !== '';
  if (hasSrc) wrap.classList.add('has-img');
  else wrap.classList.remove('has-img');
}

function initIconPlaceholders() {
  const headerIcon = document.getElementById('header-icon');
  const heroIcon = document.getElementById('hero-icon');
  checkImg(headerIcon, '.icon-placeholder-header');
  checkImg(heroIcon, '.hero-icon-placeholder');
  [headerIcon, heroIcon].forEach((img) => {
    if (!img) return;
    img.addEventListener('load', () => img.closest('.icon-placeholder-header, .hero-icon-placeholder')?.classList.add('has-img'));
  });
}
initIconPlaceholders();

// ----- Scroll reveal -----
const revealEls = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);

revealEls.forEach((el) => revealObserver.observe(el));

// Hero elements: reveal on load with stagger
const heroReveals = document.querySelectorAll('.hero .reveal');
heroReveals.forEach((el, i) => {
  el.style.transitionDelay = `${0.1 * i}s`;
});
setTimeout(() => {
  heroReveals.forEach((el) => el.classList.add('revealed'));
}, 80);

// ----- Stat counter animation -----
function animateValue(el, end) {
  const duration = 1400;
  const start = 0;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easeOut = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(start + (end - start) * easeOut);
    el.textContent = current;
    if (progress < 1) requestAnimationFrame(update);
  }

  requestAnimationFrame(update);
}

const statObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const valueEl = entry.target.querySelector('.stat-value');
      if (!valueEl) return;
      const count = parseInt(valueEl.dataset.count, 10);
      animateValue(valueEl, count);
      statObserver.unobserve(entry.target);
    });
  },
  { threshold: 0.4 }
);

document.querySelectorAll('.stat').forEach((stat) => statObserver.observe(stat));

// ----- Carousel arrows: quick scroll burst -----
const NUDGE_DURATION_MS = 2200;

document.querySelectorAll('.carousel-scroll').forEach((carousel) => {
  const track = carousel.querySelector('.carousel-track');
  const prevBtn = carousel.querySelector('.carousel-prev');
  const nextBtn = carousel.querySelector('.carousel-next');
  if (!track || !prevBtn || !nextBtn) return;

  function nudge(direction) {
    track.classList.remove('nudge-next', 'nudge-prev');
    prevBtn.disabled = true;
    nextBtn.disabled = true;

    track.classList.add(direction === 'next' ? 'nudge-next' : 'nudge-prev');

    setTimeout(() => {
      track.classList.remove('nudge-next', 'nudge-prev');
      prevBtn.disabled = false;
      nextBtn.disabled = false;
    }, NUDGE_DURATION_MS);
  }

  nextBtn.addEventListener('click', () => nudge('next'));
  prevBtn.addEventListener('click', () => nudge('prev'));
});
