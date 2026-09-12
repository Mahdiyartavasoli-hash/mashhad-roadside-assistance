/** Lightweight inline SVG icon factory; no external icon dependency. */
window.icon = function(name, cls = "w-6 h-6") {
  const common = `class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"`;
  const p = {
    truck: `<svg ${common}><path d="M3 7h11v10H3z"/><path d="M14 10h4l3 3v4h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>`,
    car: `<svg ${common}><path d="M5 16l1.2-6h11.6l1.2 6"/><path d="M4 16h16v3H4z"/><path d="M8 10l1.5-3h5L16 10"/><circle cx="8" cy="19" r="1.5"/><circle cx="16" cy="19" r="1.5"/></svg>`,
    battery: `<svg ${common}><rect x="3" y="7" width="18" height="10" rx="2"/><path d="M7 5v2M17 5v2M12 9v6M9 12h6"/></svg>`,
    tire: `<svg ${common}><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 4v3M12 17v3M4 12h3M17 12h3"/></svg>`,
    wrench: `<svg ${common}><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L4 17l3 3 5.3-5.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2-2z"/></svg>`,
    fuel: `<svg ${common}><path d="M6 20V5h9v15"/><path d="M6 9h9M9 5V3h5v2"/><path d="M15 7h3l2 2v8a2 2 0 0 1-4 0v-5"/></svg>`,
    alert: `<svg ${common}><path d="M12 3l9 16H3z"/><path d="M12 9v4M12 17h.01"/></svg>`,
    bolt: `<svg ${common}><path d="M13 2L4 14h6l-1 8 9-12h-6z"/></svg>`,
    key: `<svg ${common}><circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 5l3 3M14 7l3 3"/></svg>`,
    settings: `<svg ${common}><path d="M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1-1.7 1.7-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.5v.2h-2.4v-.2a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.9.3l-.1.1-1.7-1.7.1-.1A1.7 1.7 0 0 0 8.4 15a1.7 1.7 0 0 0-1.5-1H6.7v-2.4h.2a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.9L8 8.6l1.7-1.7.1.1a1.7 1.7 0 0 0 1.9.3 1.7 1.7 0 0 0 1-1.5v-.2h2.4v.2a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1 1.7 1.7-.1.1a1.7 1.7 0 0 0-.3 1.9 1.7 1.7 0 0 0 1.5 1h.2V14h-.2a1.7 1.7 0 0 0-1.5 1z"/></svg>`,
    scan: `<svg ${common}><path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3"/><path d="M8 12h8M12 8v8"/></svg>`,
    snow: `<svg ${common}><path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M8 5l4 3 4-3M8 19l4-3 4 3"/></svg>`,
    phone: `<svg ${common}><path d="M6.5 3.5l3 2.5-2 3a13 13 0 0 0 7.5 7.5l3-2 2.5 3c-1 2-2.5 3-4.5 3C9.4 20.5 3.5 14.6 3.5 8c0-2 .9-3.5 3-4.5z"/></svg>`,
    arrow: `<svg ${common}><path d="M5 12h14M13 6l6 6-6 6"/></svg>`,
    chevron: `<svg ${common}><path d="M6 9l6 6 6-6"/></svg>`,
    menu: `<svg ${common}><path d="M4 7h16M4 12h16M4 17h16"/></svg>`,
    close: `<svg ${common}><path d="M6 6l12 12M18 6L6 18"/></svg>`,
    map: `<svg ${common}><path d="M4 6l5-2 6 2 5-2v14l-5 2-6-2-5 2z"/><path d="M9 4v14M15 6v14"/></svg>`,
    clock: `<svg ${common}><circle cx="12" cy="12" r="8"/><path d="M12 7v5l3 2"/></svg>`,
    check: `<svg ${common}><path d="M5 12l4 4L19 6"/></svg>`,
    chat: `<svg ${common}><path d="M5 5h14v10H9l-4 4z"/></svg>`,
    star: `<svg ${common}><path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9z"/></svg>`,
    menuDots: `<svg ${common}><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>`
  };
  return p[name] || p.car;
};
