/**
 * Optional Django integration layer.
 * The static site keeps local data as a resilient fallback. When the frontend
 * is served from the same origin as Django, this module hydrates content from
 * /api/site/ and posts assistance requests to /api/leads/.
 */
window.API = (() => {
  const API_BASE = window.SITE_CONFIG?.apiBase || '/api';

  async function loadSiteContent() {
    try {
      const response = await fetch(`${API_BASE}/site/`, {
        headers: { Accept: 'application/json' },
        credentials: 'same-origin'
      });
      if (!response.ok) throw new Error(`API responded with ${response.status}`);
      const payload = await response.json();

      if (payload.site) {
        const site = payload.site;
        window.SITE_CONFIG.brandName = site.brand_name_fa || window.SITE_CONFIG.brandName;
        window.SITE_CONFIG.brandShort = site.brand_name_fa || window.SITE_CONFIG.brandShort;
        window.SITE_CONFIG.phone = site.phone || window.SITE_CONFIG.phone;
        window.SITE_CONFIG.whatsapp = site.whatsapp || window.SITE_CONFIG.whatsapp;
      }

      if (payload.stats?.length) {
        const stats = payload.stats;
        window.SITE_CONFIG.stats = {
          missions: stats.find(s => s.label_fa === 'مأموریت موفق')?.value || window.SITE_CONFIG.stats.missions,
          experience: stats.find(s => s.label_fa === 'سال تجربه')?.value || window.SITE_CONFIG.stats.experience,
          satisfaction: stats.find(s => s.label_fa === 'رضایت مشتری')?.value || window.SITE_CONFIG.stats.satisfaction
        };
      }

      if (payload.services?.length) {
        window.SITE_DATA.services = payload.services.map(item => ({
          id: item.slug,
          icon: item.icon,
          title: item.title_fa,
          text: item.description_fa
        }));
      }

      if (payload.vehicles?.length) {
        window.SITE_DATA.vehicles = payload.vehicles.map(item => ({
          title: item.title_fa,
          text: item.description_fa,
          icon: item.slug === 'foreign' ? 'premium' : item.slug === 'chinese' ? 'suv' : 'car'
        }));
      }

      if (payload.faq?.length) {
        window.SITE_DATA.faq = payload.faq.map(item => ({ q: item.question_fa, a: item.answer_fa }));
      }

      if (payload.testimonials?.length) {
        window.SITE_DATA.testimonials = payload.testimonials.map(item => ({
          name: item.name,
          text: item.text_fa,
          role: 'مشتری'
        }));
      }

      if (payload.blog?.length) {
        window.SITE_DATA.blog = payload.blog.map(item => ({
          category: 'راهنمای خودرو',
          title: item.title_fa,
          excerpt: item.excerpt_fa,
          date: item.published_at ? new Date(item.published_at).toLocaleDateString('fa-IR') : 'مقاله'
        }));
      }
    } catch (error) {
      // Local static data remains the fallback when Django is not available.
      console.info('[API] Using local frontend data:', error.message);
    }
  }

  async function submitLead(payload) {
    const response = await fetch(`${API_BASE}/leads/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || data.message || 'Request failed');
    return data;
  }

  return { loadSiteContent, submitLead };
})();
