(async function () {
  "use strict";

  // Hydrate editable content from Django when available; otherwise use local fallback data.
  if (window.API) await window.API.loadSiteContent();

  const { SITE_CONFIG: config, SITE_DATA: data } = window;
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

  // Render brand/configurable content.
  $$('[data-brand]').forEach(el => el.textContent = config.brandShort);
  $$('[data-stat="missions"]').forEach(el => el.textContent = config.stats.missions);
  $$('[data-stat="experience"]').forEach(el => el.textContent = config.stats.experience);
  $$('[data-stat="satisfaction"]').forEach(el => el.textContent = config.stats.satisfaction);
  $$('[data-phone]').forEach(el => el.textContent = config.phoneDisplay);

  // Use centralized phone values so changing one config value updates the UI.
  $$('a[href^="tel:"]').forEach(a => { a.href = `tel:${config.phone}`; });
  $$('a[href*="wa.me"]').forEach(a => { a.href = `https://wa.me/${config.whatsapp}`; });

  $('#menu-button').innerHTML = icon('menu');
  $('#hero-phone-icon').innerHTML = icon('phone', 'h-5 w-5');
  $('#hero-map-icon').innerHTML = icon('map', 'h-5 w-5');
  $('#contact-phone-icon').innerHTML = icon('phone', 'h-5 w-5 text-red-400');

  function cardIcon(name, size = 'h-6 w-6') { return icon(name, size); }

  // Problems are intentionally data-driven for future CMS/API replacement.
  $('#problems-grid').innerHTML = data.problems.map(item => `
    <a href="#contact" class="problem-card rounded-2xl border border-zinc-200 bg-white p-4 shadow-sm sm:p-5 focus:outline-none focus:ring-4 focus:ring-red-100">
      <span class="grid h-11 w-11 place-items-center rounded-xl bg-red-50 text-red-600">${cardIcon(item.icon)}</span>
      <h3 class="mt-4 text-sm font-black sm:text-base">${item.title}</h3>
      <p class="mt-2 text-xs leading-6 text-zinc-500 sm:text-sm">${item.text}</p>
    </a>`).join('');

  $('#services-grid').innerHTML = data.services.map(item => `
    <article class="service-card group rounded-3xl border border-white/10 bg-white/[.04] p-5 hover:border-red-500/50 hover:bg-white/[.07]">
      <div class="flex items-start justify-between gap-3"><span class="grid h-11 w-11 place-items-center rounded-xl bg-red-600/10 text-red-400 group-hover:bg-red-600 group-hover:text-white">${cardIcon(item.icon)}</span><span class="text-zinc-600">${cardIcon('arrow','h-5 w-5')}</span></div>
      <h3 class="mt-5 font-black">${item.title}</h3><p class="mt-2 text-sm leading-7 text-zinc-400">${item.text}</p>
    </article>`).join('');

  $('#vehicles-grid').innerHTML = data.vehicles.map(item => `
    <article class="reveal rounded-3xl border border-zinc-200 bg-white p-6 shadow-sm">
      <div class="grid h-14 w-14 place-items-center rounded-2xl bg-zinc-950 text-white">${cardIcon(item.icon, 'h-7 w-7')}</div>
      <h3 class="mt-5 font-black">${item.title}</h3><p class="mt-2 text-sm leading-7 text-zinc-500">${item.text}</p>
    </article>`).join('');

  $('#testimonials-grid').innerHTML = data.testimonials.map(item => `
    <article class="testimonial-card rounded-3xl border border-white/10 bg-white/[.04] p-6"><div class="flex gap-1 text-amber-400">${Array(5).fill(cardIcon('star','h-4 w-4')).join('')}</div><p class="mt-5 text-sm leading-7 text-zinc-300">“${item.text}”</p><div class="mt-6 border-t border-white/10 pt-4"><strong class="block text-sm">${item.name}</strong><span class="text-xs text-zinc-500">${item.role}</span></div></article>`).join('');

  $('#blog-grid').innerHTML = data.blog.slice(0, 3).map((item, i) => `
    <article class="blog-card overflow-hidden rounded-3xl border border-zinc-200 bg-white shadow-sm"><div class="aspect-[16/9] bg-gradient-to-br ${i === 0 ? 'from-red-900 to-zinc-900' : i === 1 ? 'from-zinc-800 to-red-950' : 'from-zinc-700 to-zinc-950'} p-6"><div class="flex h-full items-end"><span class="rounded-full bg-white/10 px-3 py-1 text-xs font-bold text-white backdrop-blur">${item.category}</span></div></div><div class="p-6"><h3 class="text-lg font-black leading-8">${item.title}</h3><p class="mt-3 text-sm leading-7 text-zinc-500">${item.excerpt}</p><div class="mt-5 text-xs font-bold text-red-600">${item.date} ←</div></div></article>`).join('');

  $('#faq-list').innerHTML = data.faq.map((item, i) => `
    <div class="faq-item rounded-2xl border border-zinc-200 bg-white"><button type="button" class="faq-button flex w-full items-center justify-between gap-5 p-5 text-right font-bold focus:outline-none focus:ring-4 focus:ring-red-100" aria-expanded="${i === 0 ? 'true' : 'false'}"><span>${item.q}</span><span class="faq-icon shrink-0 text-red-600">${cardIcon('chevron','h-5 w-5')}</span></button><div class="faq-answer ${i === 0 ? '' : 'hidden'} px-5 pb-5 text-sm leading-7 text-zinc-600">${item.a}</div></div>`).join('');

  // Mobile menu.
  const menuButton = $('#menu-button');
  const mobileMenu = $('#mobile-menu');
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!open));
    menuButton.innerHTML = icon(open ? 'menu' : 'close');
    mobileMenu.classList.toggle('hidden', open);
  });
  $$('#mobile-menu a').forEach(a => a.addEventListener('click', () => {
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.innerHTML = icon('menu');
    mobileMenu.classList.add('hidden');
  }));

  // FAQ accordion.
  $$('.faq-button').forEach(button => button.addEventListener('click', () => {
    const item = button.closest('.faq-item');
    const answer = $('.faq-answer', item);
    const isOpen = button.getAttribute('aria-expanded') === 'true';
    $$('.faq-button').forEach(other => {
      other.setAttribute('aria-expanded', 'false');
      $('.faq-answer', other.closest('.faq-item')).classList.add('hidden');
    });
    if (!isOpen) {
      button.setAttribute('aria-expanded', 'true');
      answer.classList.remove('hidden');
    }
  }));

  // Submit to Django when available. If the API is not deployed yet, keep the UX usable.
  $('#request-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const form = event.currentTarget;
    const message = $('#form-message');
    const name = form.elements.name.value.trim();
    const phone = form.elements.phone.value.trim();
    if (!name || !phone) {
      message.textContent = 'لطفاً نام و شماره تماس را وارد کنید.';
      message.className = 'mt-3 rounded-xl bg-red-50 p-3 text-center text-sm font-bold text-red-700';
      message.classList.remove('hidden');
      return;
    }

    const payload = {
      name,
      phone,
      vehicle: form.elements.vehicle.value,
      problem: form.elements.problem.value,
      location: form.elements.location.value.trim(),
      description: form.elements.details.value.trim(),
      website: form.elements.website?.value || ''
    };

    try {
      if (!window.API) throw new Error('API client unavailable');
      await window.API.submitLead(payload);
      message.textContent = 'درخواست شما با موفقیت ثبت شد. به‌زودی با شما تماس می‌گیریم.';
      message.className = 'mt-3 rounded-xl bg-green-50 p-3 text-center text-sm font-bold text-green-700';
      message.classList.remove('hidden');
      form.reset();
    } catch (error) {
      message.textContent = 'فعلاً امکان ثبت آنلاین درخواست وجود ندارد. لطفاً از دکمه تماس فوری استفاده کنید.';
      message.className = 'mt-3 rounded-xl bg-amber-50 p-3 text-center text-sm font-bold text-amber-800';
      message.classList.remove('hidden');
    }
  });

  // Progressive reveal animation with reduced-motion support.
  const revealItems = $$('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('is-visible'); obs.unobserve(entry.target); } });
    }, { threshold: 0.12 });
    revealItems.forEach(el => observer.observe(el));
  } else revealItems.forEach(el => el.classList.add('is-visible'));

  // JSON-LD: deliberately excludes fabricated address/geo/reviews.
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'AutomotiveBusiness',
    name: config.brandName,
    url: window.location.origin + window.location.pathname,
    telephone: `+98${config.phone.replace(/^0/, '')}`,
    areaServed: { '@type': 'City', name: 'Mashhad' },
    openingHours: 'Mo-Su 00:00-23:59'
  };
  $('#business-schema').textContent = JSON.stringify(schema);
})();
