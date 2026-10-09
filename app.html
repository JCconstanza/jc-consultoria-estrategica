<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#0A2342">
<title>JC Fiscal | Jonathan Constanza</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:wght@400;700&family=Noto+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --azul: #0A2342;
    --azul-medio: #0d2d56;
    --azul-claro: #1a4070;
    --oro: #C5A572;
    --oro-claro: #d4bb90;
    --crema: #F4F4F6;
    --blanco: #ffffff;
    --texto-oscuro: #1a1a2e;
    --texto-medio: #4a5568;
    --verde: #1a6b3c;
    --rojo: #c53030;
    --nav-h: 64px;
    --bottom-h: 68px;
  }

  * { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }
  html, body { height:100%; overflow:hidden; }

  body {
    font-family: 'Noto Sans', sans-serif;
    font-weight: 400;
    background: var(--crema);
    color: var(--texto-oscuro);
    max-width: 430px;
    margin: 0 auto;
    position: relative;
  }

  /* ── TOP NAV ── */
  .top-nav {
    position: fixed; top:0; left:50%; transform:translateX(-50%);
    width:100%; max-width:430px; height:var(--nav-h);
    background: var(--azul);
    display: flex; align-items:center; justify-content:space-between;
    padding: 0 1.2rem;
    z-index: 200;
    box-shadow: 0 2px 20px rgba(10,35,66,0.3);
  }

  .top-nav-logo { display:flex; align-items:center; gap:0.6rem; }
  .top-monogram {
    width:36px; height:36px; background:rgba(197,165,114,0.15);
    border:1px solid rgba(197,165,114,0.4); border-radius:8px;
    display:flex; align-items:center; justify-content:center;
  }
  .top-monogram span { font-family:'Noto Serif',serif; font-weight:700; color:var(--oro); font-size:0.8rem; }
  .top-nav-info { display:flex; flex-direction:column; }
  .top-nav-name { font-family:'Noto Serif',serif; font-weight:700; font-size:0.85rem; color:var(--blanco); }
  .top-nav-sub { font-size:0.6rem; color:rgba(197,165,114,0.7); letter-spacing:0.1em; text-transform:uppercase; }

  .top-nav-right { display:flex; align-items:center; gap:0.5rem; }
  .nav-pill {
    background:rgba(197,165,114,0.15); border:1px solid rgba(197,165,114,0.3);
    border-radius:20px; padding:0.3rem 0.7rem;
    font-size:0.6rem; color:var(--oro); letter-spacing:0.1em; text-transform:uppercase; font-weight:600;
    display:flex; align-items:center; gap:0.3rem;
  }
  .nav-pill .dot { width:5px; height:5px; background:#4ade80; border-radius:50%; animation:blink 2s infinite; }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

  /* ── SCROLL CONTAINER ── */
  .app-scroll {
    position: fixed; top:var(--nav-h); bottom:var(--bottom-h);
    left:50%; transform:translateX(-50%);
    width:100%; max-width:430px;
    overflow-y: auto; overflow-x:hidden;
    -webkit-overflow-scrolling: touch;
    scroll-behavior: smooth;
  }

  /* ── SCREENS ── */
  .screen { display:none; padding:1.2rem; min-height:100%; animation:fadeIn 0.3s ease; }
  .screen.active { display:block; }
  @keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }

  /* ── BOTTOM NAV ── */
  .bottom-nav {
    position:fixed; bottom:0; left:50%; transform:translateX(-50%);
    width:100%; max-width:430px; height:var(--bottom-h);
    background:var(--blanco);
    border-top:1px solid rgba(10,35,66,0.08);
    display:flex; align-items:center;
    z-index:200;
    box-shadow: 0 -4px 20px rgba(10,35,66,0.08);
    padding: 0 0.5rem;
    padding-bottom: env(safe-area-inset-bottom);
  }

  .nav-item {
    flex:1; display:flex; flex-direction:column; align-items:center;
    gap:0.25rem; padding:0.5rem 0.3rem;
    cursor:pointer; transition:all 0.2s;
    border-radius:10px; border:none; background:none;
  }
  .nav-item .nav-icon { font-size:1.35rem; transition:transform 0.2s; }
  .nav-item .nav-label { font-size:0.55rem; font-weight:500; letter-spacing:0.06em; text-transform:uppercase; color:rgba(74,85,104,0.6); transition:color 0.2s; }
  .nav-item.active .nav-label { color:var(--azul); font-weight:700; }
  .nav-item.active .nav-icon { transform:translateY(-2px); }
  .nav-item.active { background:rgba(10,35,66,0.05); }

  /* ── CARDS ── */
  .card {
    background:var(--blanco); border-radius:14px;
    border:1px solid rgba(10,35,66,0.06);
    box-shadow:0 2px 12px rgba(10,35,66,0.06);
    overflow:hidden; margin-bottom:1rem;
  }

  .card-header {
    padding:1rem 1.2rem 0.8rem;
    border-bottom:1px solid rgba(10,35,66,0.05);
    display:flex; align-items:center; gap:0.6rem;
  }
  .card-header-icon { font-size:1.1rem; }
  .card-header-title { font-family:'Noto Serif',serif; font-weight:700; font-size:0.9rem; color:var(--azul); }
  .card-header-badge {
    margin-left:auto; font-size:0.58rem; font-weight:600; letter-spacing:0.1em;
    text-transform:uppercase; color:var(--oro);
    background:rgba(197,165,114,0.12); border:1px solid rgba(197,165,114,0.25);
    padding:0.2rem 0.5rem; border-radius:4px;
  }
  .card-body { padding:1.2rem; }

  /* ── SECTION LABEL ── */
  .section-label {
    font-size:0.62rem; font-weight:700; letter-spacing:0.18em;
    text-transform:uppercase; color:var(--texto-medio);
    margin-bottom:0.7rem; padding-left:0.2rem;
  }

  /* ══════════════════════════════
     DASHBOARD
  ══════════════════════════════ */
  .dash-hero {
    background: linear-gradient(135deg, var(--azul) 0%, var(--azul-claro) 100%);
    border-radius:16px; padding:1.5rem;
    margin-bottom:1rem; position:relative; overflow:hidden;
  }
  .dash-hero::after {
    content:'.JC'; position:absolute; right:-0.5rem; bottom:-1rem;
    font-family:'Noto Serif',serif; font-weight:700; font-size:5rem;
    color:rgba(197,165,114,0.07); line-height:1; pointer-events:none;
  }
  .dash-hero-date { font-size:0.65rem; color:rgba(197,165,114,0.7); letter-spacing:0.12em; text-transform:uppercase; margin-bottom:0.4rem; }
  .dash-hero-title { font-family:'Noto Serif',serif; font-weight:700; font-size:1.15rem; color:var(--blanco); margin-bottom:0.2rem; }
  .dash-hero-sub { font-size:0.75rem; color:rgba(244,244,246,0.55); }

  .dash-kpis { display:grid; grid-template-columns:1fr 1fr; gap:0.7rem; margin-bottom:1rem; }
  .kpi-card {
    background:var(--blanco); border-radius:12px; padding:1rem;
    border:1px solid rgba(10,35,66,0.06);
    box-shadow:0 2px 8px rgba(10,35,66,0.05);
    position:relative; overflow:hidden;
  }
  .kpi-card::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:var(--oro); }
  .kpi-icon { font-size:1.4rem; margin-bottom:0.5rem; }
  .kpi-value { font-family:'Noto Serif',serif; font-weight:700; font-size:1.25rem; color:var(--azul); }
  .kpi-label { font-size:0.62rem; color:var(--texto-medio); margin-top:0.15rem; letter-spacing:0.04em; }
  .kpi-trend { font-size:0.6rem; margin-top:0.3rem; font-weight:600; }
  .kpi-trend.up { color:var(--verde); }
  .kpi-trend.warn { color:#d69e2e; }

  .quick-actions { display:grid; grid-template-columns:repeat(4,1fr); gap:0.6rem; margin-bottom:1rem; }
  .qa-btn {
    background:var(--blanco); border-radius:12px; padding:0.8rem 0.4rem;
    border:1px solid rgba(10,35,66,0.06); cursor:pointer;
    display:flex; flex-direction:column; align-items:center; gap:0.35rem;
    transition:all 0.2s; box-shadow:0 2px 8px rgba(10,35,66,0.05);
  }
  .qa-btn:active { transform:scale(0.95); background:var(--crema); }
  .qa-btn .qa-icon { font-size:1.3rem; }
  .qa-btn .qa-label { font-size:0.55rem; font-weight:600; letter-spacing:0.06em; text-transform:uppercase; color:var(--azul); text-align:center; line-height:1.3; }

  .alerta-item {
    display:flex; align-items:center; gap:0.8rem;
    padding:0.9rem 1.2rem;
    border-bottom:1px solid rgba(10,35,66,0.04);
  }
  .alerta-item:last-child { border-bottom:none; }
  .alerta-dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
  .alerta-dot.rojo { background:#fc8181; }
  .alerta-dot.amarillo { background:#f6e05e; }
  .alerta-dot.verde { background:#68d391; }
  .alerta-info { flex:1; }
  .alerta-titulo { font-size:0.78rem; font-weight:600; color:var(--azul); margin-bottom:0.1rem; }
  .alerta-fecha { font-size:0.65rem; color:var(--texto-medio); }
  .alerta-dias {
    font-size:0.62rem; font-weight:700; letter-spacing:0.06em;
    padding:0.2rem 0.5rem; border-radius:6px;
  }
  .alerta-dias.urgente { background:rgba(252,129,129,0.15); color:#c53030; }
  .alerta-dias.pronto { background:rgba(246,224,94,0.2); color:#b7791f; }
  .alerta-dias.ok { background:rgba(104,211,145,0.15); color:#276749; }

  /* ══════════════════════════════
     ASISTENTE FISCAL IA
  ══════════════════════════════ */
  .chat-wrap {
    display:flex; flex-direction:column;
    height: calc(100vh - var(--nav-h) - var(--bottom-h) - 2.4rem);
  }

  .chat-messages {
    flex:1; overflow-y:auto; padding:0 0 1rem;
    display:flex; flex-direction:column; gap:0.8rem;
    -webkit-overflow-scrolling:touch;
  }

  .msg { display:flex; flex-direction:column; max-width:88%; }
  .msg.user { align-self:flex-end; align-items:flex-end; }
  .msg.bot { align-self:flex-start; align-items:flex-start; }

  .msg-bubble {
    padding:0.75rem 1rem; border-radius:16px;
    font-size:0.82rem; line-height:1.6;
  }
  .msg.user .msg-bubble {
    background:var(--azul); color:var(--blanco);
    border-bottom-right-radius:4px;
  }
  .msg.bot .msg-bubble {
    background:var(--blanco); color:var(--texto-oscuro);
    border:1px solid rgba(10,35,66,0.08);
    border-bottom-left-radius:4px;
    box-shadow:0 2px 8px rgba(10,35,66,0.06);
  }
  .msg-time { font-size:0.58rem; color:rgba(74,85,104,0.5); margin-top:0.2rem; padding:0 0.3rem; }

  .bot-avatar {
    width:28px; height:28px; background:var(--azul); border-radius:8px;
    display:flex; align-items:center; justify-content:center;
    margin-bottom:0.3rem; flex-shrink:0;
  }
  .bot-avatar span { font-family:'Noto Serif',serif; font-weight:700; color:var(--oro); font-size:0.62rem; }

  .typing-indicator {
    display:flex; gap:4px; padding:0.75rem 1rem;
    background:var(--blanco); border-radius:16px; border-bottom-left-radius:4px;
    border:1px solid rgba(10,35,66,0.08); width:fit-content;
  }
  .typing-indicator span {
    width:6px; height:6px; background:var(--oro); border-radius:50%;
    animation:typing 1.2s infinite;
  }
  .typing-indicator span:nth-child(2) { animation-delay:0.2s; }
  .typing-indicator span:nth-child(3) { animation-delay:0.4s; }
  @keyframes typing { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-6px)} }

  .chat-chips { display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:0.8rem; }
  .chat-chip {
    font-size:0.68rem; padding:0.4rem 0.8rem;
    background:var(--blanco); border:1px solid rgba(10,35,66,0.12);
    border-radius:20px; cursor:pointer; color:var(--azul); font-weight:500;
    transition:all 0.2s; white-space:nowrap;
  }
  .chat-chip:active { background:var(--azul); color:var(--oro); }

  .chat-input-bar {
    display:flex; gap:0.5rem; align-items:flex-end;
    padding-top:0.8rem;
    border-top:1px solid rgba(10,35,66,0.07);
  }
  .chat-input {
    flex:1; background:var(--blanco);
    border:1.5px solid rgba(10,35,66,0.12); border-radius:12px;
    padding:0.7rem 1rem; font-family:'Noto Sans',sans-serif;
    font-size:0.85rem; color:var(--texto-oscuro); outline:none;
    resize:none; max-height:100px; line-height:1.5;
    transition:border-color 0.25s;
  }
  .chat-input:focus { border-color:var(--oro); }
  .chat-input::placeholder { color:rgba(74,85,104,0.45); }
  .chat-send {
    width:42px; height:42px; border-radius:12px;
    background:var(--azul); color:var(--oro);
    border:none; cursor:pointer; font-size:1.1rem;
    display:flex; align-items:center; justify-content:center;
    transition:all 0.2s; flex-shrink:0;
  }
  .chat-send:active { transform:scale(0.92); background:var(--azul-claro); }
  .chat-send:disabled { opacity:0.5; }

  /* ══════════════════════════════
     CALCULADORA
  ══════════════════════════════ */
  .calc-tabs { display:flex; gap:0; background:var(--blanco); border-radius:12px; padding:4px; margin-bottom:1rem; border:1px solid rgba(10,35,66,0.06); }
  .calc-tab {
    flex:1; padding:0.6rem; text-align:center;
    font-size:0.68rem; font-weight:600; letter-spacing:0.06em; text-transform:uppercase;
    border-radius:9px; cursor:pointer; transition:all 0.2s; border:none; background:none;
    color:var(--texto-medio);
  }
  .calc-tab.active { background:var(--azul); color:var(--oro); }

  .calc-panel { display:none; }
  .calc-panel.active { display:block; animation:fadeIn 0.25s ease; }

  .calc-field { margin-bottom:1rem; }
  .calc-label { font-size:0.7rem; font-weight:600; color:var(--texto-medio); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.4rem; display:block; }
  .calc-input {
    width:100%; background:var(--blanco); border:1.5px solid rgba(10,35,66,0.12);
    border-radius:10px; padding:0.8rem 1rem;
    font-family:'Noto Sans',sans-serif; font-size:1rem; font-weight:600;
    color:var(--texto-oscuro); outline:none; transition:border-color 0.25s;
  }
  .calc-input:focus { border-color:var(--oro); }
  .calc-select {
    width:100%; background:var(--blanco); border:1.5px solid rgba(10,35,66,0.12);
    border-radius:10px; padding:0.8rem 1rem;
    font-family:'Noto Sans',sans-serif; font-size:0.88rem;
    color:var(--texto-oscuro); outline:none; appearance:none;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%234a5568' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat:no-repeat; background-position:right 1rem center;
  }

  .calc-btn {
    width:100%; padding:1rem; border-radius:12px;
    background:var(--azul); color:var(--oro);
    border:none; font-family:'Noto Sans',sans-serif;
    font-size:0.85rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase;
    cursor:pointer; transition:all 0.25s;
  }
  .calc-btn:active { transform:scale(0.98); background:var(--azul-claro); }

  .calc-result {
    display:none; background:linear-gradient(135deg, var(--azul), var(--azul-claro));
    border-radius:14px; padding:1.4rem; margin-top:1rem;
    animation:fadeIn 0.3s ease;
  }
  .calc-result.visible { display:block; }
  .result-label { font-size:0.6rem; letter-spacing:0.18em; text-transform:uppercase; color:rgba(197,165,114,0.6); margin-bottom:0.3rem; }
  .result-value { font-family:'Noto Serif',serif; font-weight:700; font-size:1.8rem; color:var(--blanco); }
  .result-breakdown { margin-top:1rem; display:flex; flex-direction:column; gap:0.5rem; }
  .result-row { display:flex; justify-content:space-between; align-items:center; }
  .result-row-label { font-size:0.72rem; color:rgba(244,244,246,0.6); }
  .result-row-val { font-size:0.8rem; font-weight:600; color:var(--oro); }

  /* ══════════════════════════════
     CALENDARIO DGII
  ══════════════════════════════ */
  .cal-month {
    background:var(--azul); border-radius:14px; padding:1.2rem;
    margin-bottom:1rem; text-align:center;
  }
  .cal-month-name { font-family:'Noto Serif',serif; font-weight:700; font-size:1rem; color:var(--blanco); margin-bottom:0.2rem; }
  .cal-month-sub { font-size:0.65rem; color:rgba(197,165,114,0.6); letter-spacing:0.1em; text-transform:uppercase; }

  .cal-event {
    display:flex; align-items:center; gap:1rem;
    padding:1rem 1.2rem;
    border-bottom:1px solid rgba(10,35,66,0.05);
    cursor:pointer; transition:background 0.15s;
  }
  .cal-event:last-child { border-bottom:none; }
  .cal-event:active { background:var(--crema); }

  .cal-date-box {
    min-width:46px; height:46px; border-radius:10px;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    flex-shrink:0;
  }
  .cal-date-box.urgente { background:rgba(197,48,48,0.1); border:1px solid rgba(197,48,48,0.2); }
  .cal-date-box.pronto { background:rgba(214,158,46,0.1); border:1px solid rgba(214,158,46,0.2); }
  .cal-date-box.normal { background:rgba(10,35,66,0.06); border:1px solid rgba(10,35,66,0.1); }
  .cal-date-box.pasado { background:rgba(104,211,145,0.1); border:1px solid rgba(104,211,145,0.2); }
  .cal-day { font-family:'Noto Serif',serif; font-weight:700; font-size:1rem; line-height:1; }
  .cal-date-box.urgente .cal-day { color:var(--rojo); }
  .cal-date-box.pronto .cal-day { color:#b7791f; }
  .cal-date-box.normal .cal-day { color:var(--azul); }
  .cal-date-box.pasado .cal-day { color:var(--verde); }
  .cal-mes-short { font-size:0.58rem; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; color:inherit; opacity:0.7; }

  .cal-info { flex:1; }
  .cal-titulo { font-size:0.82rem; font-weight:600; color:var(--azul); margin-bottom:0.15rem; }
  .cal-desc { font-size:0.68rem; color:var(--texto-medio); line-height:1.4; }
  .cal-tag {
    font-size:0.58rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase;
    padding:0.2rem 0.5rem; border-radius:6px; white-space:nowrap; flex-shrink:0;
  }
  .cal-tag.urgente { background:rgba(197,48,48,0.1); color:var(--rojo); }
  .cal-tag.pronto { background:rgba(214,158,46,0.12); color:#b7791f; }
  .cal-tag.normal { background:rgba(10,35,66,0.07); color:var(--azul); }
  .cal-tag.pasado { background:rgba(26,107,60,0.1); color:var(--verde); }

  /* ══════════════════════════════
     BLOG GENERATOR
  ══════════════════════════════ */
  .blog-chips { display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1rem; }
  .blog-chip {
    font-size:0.68rem; padding:0.4rem 0.8rem;
    background:var(--blanco); border:1px solid rgba(10,35,66,0.12);
    border-radius:20px; cursor:pointer; color:var(--azul); font-weight:500;
    transition:all 0.2s;
  }
  .blog-chip:active { background:var(--azul); color:var(--oro); border-color:var(--azul); }

  .blog-textarea {
    width:100%; background:var(--blanco); border:1.5px solid rgba(10,35,66,0.12);
    border-radius:12px; padding:0.9rem 1rem;
    font-family:'Noto Sans',sans-serif; font-size:0.85rem;
    color:var(--texto-oscuro); outline:none; resize:none;
    height:90px; line-height:1.6; transition:border-color 0.25s;
    margin-bottom:0.8rem;
  }
  .blog-textarea:focus { border-color:var(--oro); }
  .blog-textarea::placeholder { color:rgba(74,85,104,0.45); }

  .blog-result {
    display:none; background:var(--blanco);
    border:1px solid rgba(197,165,114,0.2); border-radius:14px;
    overflow:hidden; margin-top:1rem;
    animation:fadeIn 0.35s ease;
  }
  .blog-result.visible { display:block; }
  .blog-result-header {
    background:var(--azul); padding:0.8rem 1.2rem;
    display:flex; align-items:center; justify-content:space-between;
  }
  .blog-result-label { font-size:0.62rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--oro); font-weight:600; }
  .blog-copy-btn {
    font-size:0.65rem; font-weight:600; color:rgba(197,165,114,0.7);
    background:none; border:1px solid rgba(197,165,114,0.3); border-radius:6px;
    padding:0.25rem 0.6rem; cursor:pointer; letter-spacing:0.08em; text-transform:uppercase;
    transition:all 0.2s;
  }
  .blog-copy-btn:active { background:rgba(197,165,114,0.2); }
  .blog-result-content { padding:1.2rem; font-size:0.82rem; color:var(--texto-oscuro); line-height:1.85; white-space:pre-wrap; max-height:280px; overflow-y:auto; }

  /* ── TOAST ── */
  .toast {
    position:fixed; bottom:calc(var(--bottom-h) + 1rem); left:50%; transform:translateX(-50%) translateY(10px);
    background:var(--azul); color:var(--oro);
    padding:0.6rem 1.2rem; border-radius:30px;
    font-size:0.75rem; font-weight:600; letter-spacing:0.06em;
    opacity:0; transition:all 0.3s ease; z-index:999;
    border:1px solid rgba(197,165,114,0.3); white-space:nowrap;
  }
  .toast.show { opacity:1; transform:translateX(-50%) translateY(0); }

  /* ── LOADING ── */
  .spinner {
    width:20px; height:20px; border:2px solid rgba(197,165,114,0.2);
    border-top-color:var(--oro); border-radius:50%;
    animation:spin 0.8s linear infinite; display:inline-block; margin-right:0.5rem;
  }
  @keyframes spin { to{transform:rotate(360deg)} }

  /* scrollbar */
  ::-webkit-scrollbar { width:3px; }
  ::-webkit-scrollbar-track { background:transparent; }
  ::-webkit-scrollbar-thumb { background:rgba(197,165,114,0.3); border-radius:10px; }
</style>
</head>
<body>

<!-- TOP NAV -->
<div class="top-nav">
  <div class="top-nav-logo">
    <div class="top-monogram"><span>.JC</span></div>
    <div class="top-nav-info">
      <span class="top-nav-name">JC Fiscal</span>
      <span class="top-nav-sub">Consultoría Estratégica</span>
    </div>
  </div>
  <div class="top-nav-right">
    <div class="nav-pill"><div class="dot"></div> IA Activa</div>
  </div>
</div>

<!-- MAIN SCROLL -->
<div class="app-scroll" id="app-scroll">

  <!-- ══ DASHBOARD ══ -->
  <div class="screen active" id="screen-home">

    <div class="dash-hero">
      <div class="dash-hero-date" id="dash-date">Cargando fecha...</div>
      <div class="dash-hero-title">Buenos días, Jonathan</div>
      <div class="dash-hero-sub">Tu resumen fiscal del día</div>
    </div>

    <p class="section-label">Alertas próximas</p>
    <div class="card">
      <div class="alerta-item">
        <div class="alerta-dot rojo"></div>
        <div class="alerta-info">
          <div class="alerta-titulo">IR-2 Personas Físicas</div>
          <div class="alerta-fecha">Vence 30 de abril 2026</div>
        </div>
        <div class="alerta-dias urgente">12 días</div>
      </div>
      <div class="alerta-item">
        <div class="alerta-dot amarillo"></div>
        <div class="alerta-info">
          <div class="alerta-titulo">ITBIS — Período marzo</div>
          <div class="alerta-fecha">Vence 20 de mayo 2026</div>
        </div>
        <div class="alerta-dias pronto">32 días</div>
      </div>
      <div class="alerta-item">
        <div class="alerta-dot verde"></div>
        <div class="alerta-info">
          <div class="alerta-titulo">TSS — Nómina abril</div>
          <div class="alerta-fecha">Vence 3 de junio 2026</div>
        </div>
        <div class="alerta-dias ok">46 días</div>
      </div>
    </div>

    <p class="section-label">Accesos rápidos</p>
    <div class="quick-actions">
      <button class="qa-btn" onclick="goTo('asistente')">
        <span class="qa-icon">💬</span>
        <span class="qa-label">Consultar IA</span>
      </button>
      <button class="qa-btn" onclick="goTo('calculadora')">
        <span class="qa-icon">🧮</span>
        <span class="qa-label">Calcular</span>
      </button>
      <button class="qa-btn" onclick="goTo('calendario')">
        <span class="qa-icon">📅</span>
        <span class="qa-label">Calendario</span>
      </button>
      <button class="qa-btn" onclick="goTo('blog')">
        <span class="qa-icon">✍️</span>
        <span class="qa-label">Blog IA</span>
      </button>
    </div>

    <p class="section-label">Indicadores clave</p>
    <div class="dash-kpis">
      <div class="kpi-card">
        <div class="kpi-icon">🏛️</div>
        <div class="kpi-value">18%</div>
        <div class="kpi-label">Tasa ITBIS vigente</div>
        <div class="kpi-trend ok">✓ Sin cambios 2026</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-icon">📊</div>
        <div class="kpi-value">27%</div>
        <div class="kpi-label">ISR personas jurídicas</div>
        <div class="kpi-trend ok">✓ Vigente</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-icon">👥</div>
        <div class="kpi-value">9.97%</div>
        <div class="kpi-label">Cotiz. empleador TSS</div>
        <div class="kpi-trend warn">⚠ Actualizado</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-icon">💡</div>
        <div class="kpi-value">e-CF</div>
        <div class="kpi-label">Facturación electrónica</div>
        <div class="kpi-trend warn">⚠ Obligatorio 2026</div>
      </div>
    </div>

    <div style="height:0.5rem"></div>
  </div>

  <!-- ══ ASISTENTE IA ══ -->
  <div class="screen" id="screen-asistente">
    <div class="chat-wrap">
      <div class="chat-messages" id="chat-messages">
        <div class="msg bot">
          <div class="bot-avatar"><span>.JC</span></div>
          <div class="msg-bubble">¡Hola! Soy el asistente fiscal de Jonathan Constanza. Puedo ayudarte con consultas sobre DGII, ITBIS, TSS, facturación electrónica y más. ¿En qué te asisto hoy?</div>
          <div class="msg-time">Ahora</div>
        </div>
      </div>

      <div class="chat-chips" id="chat-chips">
        <span class="chat-chip" onclick="enviarChip(this)">¿Qué es el e-CF?</span>
        <span class="chat-chip" onclick="enviarChip(this)">¿Cuándo vence el ITBIS?</span>
        <span class="chat-chip" onclick="enviarChip(this)">¿Cómo reduzco mi ISR?</span>
        <span class="chat-chip" onclick="enviarChip(this)">Obligaciones TSS empleador</span>
      </div>

      <div class="chat-input-bar">
        <textarea class="chat-input" id="chat-input" placeholder="Escribe tu consulta fiscal…" rows="1"></textarea>
        <button class="chat-send" id="chat-send" onclick="enviarMensaje()">➤</button>
      </div>
    </div>
  </div>

  <!-- ══ CALCULADORA ══ -->
  <div class="screen" id="screen-calculadora">

    <div class="calc-tabs">
      <button class="calc-tab active" onclick="switchCalc('itbis',this)">ITBIS</button>
      <button class="calc-tab" onclick="switchCalc('isr',this)">ISR</button>
      <button class="calc-tab" onclick="switchCalc('anticipos',this)">Anticipos</button>
    </div>

    <!-- ITBIS -->
    <div class="calc-panel active" id="calc-itbis">
      <div class="card">
        <div class="card-header">
          <span class="card-header-icon">🧾</span>
          <span class="card-header-title">Calculadora ITBIS</span>
          <span class="card-header-badge">18%</span>
        </div>
        <div class="card-body">
          <div class="calc-field">
            <label class="calc-label">Monto base (RD$)</label>
            <input type="number" class="calc-input" id="itbis-monto" placeholder="Ej: 50,000" oninput="calcItbis()">
          </div>
          <div class="calc-field">
            <label class="calc-label">Tipo de operación</label>
            <select class="calc-select" id="itbis-tipo" onchange="calcItbis()">
              <option value="gravado">Gravado al 18%</option>
              <option value="reducido">Tasa reducida 16%</option>
              <option value="exento">Exento</option>
            </select>
          </div>
          <div class="calc-result" id="itbis-result">
            <div class="result-label">ITBIS a pagar</div>
            <div class="result-value" id="itbis-valor">RD$ 0.00</div>
            <div class="result-breakdown">
              <div class="result-row">
                <span class="result-row-label">Base imponible</span>
                <span class="result-row-val" id="itbis-base">—</span>
              </div>
              <div class="result-row">
                <span class="result-row-label">Tasa aplicada</span>
                <span class="result-row-val" id="itbis-tasa">18%</span>
              </div>
              <div class="result-row">
                <span class="result-row-label">Total con ITBIS</span>
                <span class="result-row-val" id="itbis-total">—</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ISR -->
    <div class="calc-panel" id="calc-isr">
      <div class="card">
        <div class="card-header">
          <span class="card-header-icon">📈</span>
          <span class="card-header-title">Calculadora ISR</span>
          <span class="card-header-badge">Personas Físicas</span>
        </div>
        <div class="card-body">
          <div class="calc-field">
            <label class="calc-label">Ingreso neto anual (RD$)</label>
            <input type="number" class="calc-input" id="isr-monto" placeholder="Ej: 1,500,000">
          </div>
          <div class="calc-field">
            <label class="calc-label">Tipo de contribuyente</label>
            <select class="calc-select" id="isr-tipo">
              <option value="fisica">Persona Física</option>
              <option value="juridica">Persona Jurídica (27%)</option>
            </select>
          </div>
          <button class="calc-btn" onclick="calcIsr()">Calcular ISR</button>
          <div class="calc-result" id="isr-result">
            <div class="result-label">ISR estimado anual</div>
            <div class="result-value" id="isr-valor">RD$ 0.00</div>
            <div class="result-breakdown">
              <div class="result-row">
                <span class="result-row-label">Ingreso neto</span>
                <span class="result-row-val" id="isr-ingreso">—</span>
              </div>
              <div class="result-row">
                <span class="result-row-label">Tramo / tasa</span>
                <span class="result-row-val" id="isr-tramo">—</span>
              </div>
              <div class="result-row">
                <span class="result-row-label">ISR mensual aprox.</span>
                <span class="result-row-val" id="isr-mensual">—</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ANTICIPOS -->
    <div class="calc-panel" id="calc-anticipos">
      <div class="card">
        <div class="card-header">
          <span class="card-header-icon">💰</span>
          <span class="card-header-title">Anticipos ISR</span>
          <span class="card-header-badge">1.5% / 12 cuotas</span>
        </div>
        <div class="card-body">
          <div class="calc-field">
            <label class="calc-label">ISR del ejercicio anterior (RD$)</label>
            <input type="number" class="calc-input" id="ant-monto" placeholder="Ej: 300,000">
          </div>
          <button class="calc-btn" onclick="calcAnticipos()">Calcular cuotas</button>
          <div class="calc-result" id="ant-result">
            <div class="result-label">Anticipo mensual</div>
            <div class="result-value" id="ant-cuota">RD$ 0.00</div>
            <div class="result-breakdown">
              <div class="result-row">
                <span class="result-row-label">Total anticipos año</span>
                <span class="result-row-val" id="ant-total">—</span>
              </div>
              <div class="result-row">
                <span class="result-row-label">Base de cálculo</span>
                <span class="result-row-val" id="ant-base">—</span>
              </div>
              <div class="result-row">
                <span class="result-row-label">Vence cada mes</span>
                <span class="result-row-val">Día 15</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- ══ CALENDARIO ══ -->
  <div class="screen" id="screen-calendario">

    <div class="cal-month">
      <div class="cal-month-name">Abril – Junio 2026</div>
      <div class="cal-month-sub">Vencimientos DGII & TSS</div>
    </div>

    <div class="card">
      <div class="cal-event">
        <div class="cal-date-box urgente">
          <span class="cal-day">20</span>
          <span class="cal-mes-short">Abr</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">ITBIS — Período marzo 2026</div>
          <div class="cal-desc">Declaración y pago mensual del ITBIS (IR-17)</div>
        </div>
        <span class="cal-tag urgente">Urgente</span>
      </div>
      <div class="cal-event">
        <div class="cal-date-box urgente">
          <span class="cal-day">30</span>
          <span class="cal-mes-short">Abr</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">IR-2 — Declaración personas físicas</div>
          <div class="cal-desc">Plazo ampliado por la DGII para ejercicio fiscal 2025</div>
        </div>
        <span class="cal-tag urgente">Urgente</span>
      </div>
      <div class="cal-event">
        <div class="cal-date-box pronto">
          <span class="cal-day">03</span>
          <span class="cal-mes-short">May</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">TSS — Nómina abril</div>
          <div class="cal-desc">Pago cotizaciones seguridad social del período</div>
        </div>
        <span class="cal-tag pronto">Pronto</span>
      </div>
      <div class="cal-event">
        <div class="cal-date-box pronto">
          <span class="cal-day">20</span>
          <span class="cal-mes-short">May</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">ITBIS — Período abril 2026</div>
          <div class="cal-desc">Declaración y pago mensual del ITBIS</div>
        </div>
        <span class="cal-tag pronto">Pronto</span>
      </div>
      <div class="cal-event">
        <div class="cal-date-box normal">
          <span class="cal-day">15</span>
          <span class="cal-mes-short">May</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">Anticipo ISR — Cuota mayo</div>
          <div class="cal-desc">Pago de anticipo mensual del Impuesto Sobre la Renta</div>
        </div>
        <span class="cal-tag normal">Pendiente</span>
      </div>
      <div class="cal-event">
        <div class="cal-date-box normal">
          <span class="cal-day">03</span>
          <span class="cal-mes-short">Jun</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">TSS — Nómina mayo</div>
          <div class="cal-desc">Pago cotizaciones seguridad social del período</div>
        </div>
        <span class="cal-tag normal">Pendiente</span>
      </div>
      <div class="cal-event">
        <div class="cal-date-box normal">
          <span class="cal-day">20</span>
          <span class="cal-mes-short">Jun</span>
        </div>
        <div class="cal-info">
          <div class="cal-titulo">ITBIS — Período mayo 2026</div>
          <div class="cal-desc">Declaración y pago mensual del ITBIS</div>
        </div>
        <span class="cal-tag normal">Pendiente</span>
      </div>
    </div>
    <div style="height:0.5rem"></div>
  </div>

  <!-- ══ BLOG GENERATOR ══ -->
  <div class="screen" id="screen-blog">

    <div class="card">
      <div class="card-header">
        <span class="card-header-icon">✍️</span>
        <span class="card-header-title">Generador de Artículos</span>
        <span class="card-header-badge">IA</span>
      </div>
      <div class="card-body">
        <p class="section-label">Temas sugeridos</p>
        <div class="blog-chips">
          <span class="blog-chip" onclick="setBlogTema(this)">Facturación e-CF 2026</span>
          <span class="blog-chip" onclick="setBlogTema(this)">Errores ITBIS comunes</span>
          <span class="blog-chip" onclick="setBlogTema(this)">Anticipos ISR paso a paso</span>
          <span class="blog-chip" onclick="setBlogTema(this)">TSS: obligaciones empleador</span>
          <span class="blog-chip" onclick="setBlogTema(this)">PYMES: ventajas fiscales RD</span>
          <span class="blog-chip" onclick="setBlogTema(this)">KPIs financieros esenciales</span>
        </div>

        <p class="section-label">Tu tema</p>
        <textarea class="blog-textarea" id="blog-input" placeholder="Describe el tema del artículo… Ej: ¿Cómo implementar la facturación electrónica en mi empresa?"></textarea>

        <button class="calc-btn" id="blog-btn" onclick="generarBlog()">
          <span id="blog-btn-text">✦ Generar artículo</span>
        </button>

        <div class="blog-result" id="blog-result">
          <div class="blog-result-header">
            <span class="blog-result-label">✦ Borrador generado — JC Asistente</span>
            <button class="blog-copy-btn" onclick="copiarBlog()">Copiar</button>
          </div>
          <div class="blog-result-content" id="blog-content"></div>
        </div>
      </div>
    </div>
  </div>

</div><!-- /app-scroll -->

<!-- BOTTOM NAV -->
<nav class="bottom-nav">
  <button class="nav-item active" id="nav-home" onclick="goTo('home')">
    <span class="nav-icon">🏠</span>
    <span class="nav-label">Inicio</span>
  </button>
  <button class="nav-item" id="nav-asistente" onclick="goTo('asistente')">
    <span class="nav-icon">💬</span>
    <span class="nav-label">Asistente</span>
  </button>
  <button class="nav-item" id="nav-calculadora" onclick="goTo('calculadora')">
    <span class="nav-icon">🧮</span>
    <span class="nav-label">Calcular</span>
  </button>
  <button class="nav-item" id="nav-calendario" onclick="goTo('calendario')">
    <span class="nav-icon">📅</span>
    <span class="nav-label">Calendario</span>
  </button>
  <button class="nav-item" id="nav-blog" onclick="goTo('blog')">
    <span class="nav-icon">✍️</span>
    <span class="nav-label">Blog IA</span>
  </button>
</nav>

<div class="toast" id="toast"></div>

<script>
  // ── Fecha actual
  const ahora = new Date();
  const dias = ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'];
  const meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
  document.getElementById('dash-date').textContent = `${dias[ahora.getDay()]}, ${ahora.getDate()} de ${meses[ahora.getMonth()]} ${ahora.getFullYear()}`;

  // ── Navegación
  function goTo(screen) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    document.getElementById('screen-' + screen).classList.add('active');
    document.getElementById('nav-' + screen).classList.add('active');
    document.getElementById('app-scroll').scrollTop = 0;
  }

  // ── Toast
  function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2500);
  }

  // ── CALCULADORA ITBIS
  function calcItbis() {
    const monto = parseFloat(document.getElementById('itbis-monto').value) || 0;
    const tipo = document.getElementById('itbis-tipo').value;
    if (monto <= 0) { document.getElementById('itbis-result').classList.remove('visible'); return; }

    let tasa = tipo === 'gravado' ? 0.18 : tipo === 'reducido' ? 0.16 : 0;
    const itbis = monto * tasa;
    const total = monto + itbis;
    const fmt = v => 'RD$ ' + v.toLocaleString('es-DO', {minimumFractionDigits:2, maximumFractionDigits:2});

    document.getElementById('itbis-valor').textContent = fmt(itbis);
    document.getElementById('itbis-base').textContent = fmt(monto);
    document.getElementById('itbis-tasa').textContent = tipo === 'exento' ? 'Exento (0%)' : (tasa*100)+'%';
    document.getElementById('itbis-total').textContent = fmt(total);
    document.getElementById('itbis-result').classList.add('visible');
  }

  // ── CALCULADORA ISR
  function calcIsr() {
    const monto = parseFloat(document.getElementById('isr-monto').value) || 0;
    const tipo = document.getElementById('isr-tipo').value;
    if (monto <= 0) return;

    const fmt = v => 'RD$ ' + v.toLocaleString('es-DO', {minimumFractionDigits:2, maximumFractionDigits:2});
    let isr = 0, tramo = '';

    if (tipo === 'juridica') {
      isr = monto * 0.27;
      tramo = '27% tasa fija';
    } else {
      // Escala DGII 2026 personas físicas (aproximada)
      if (monto <= 416220) { isr = 0; tramo = 'Exento'; }
      else if (monto <= 624329) { isr = (monto - 416220) * 0.15; tramo = '15%'; }
      else if (monto <= 867123) { isr = 31216 + (monto - 624329) * 0.20; tramo = '20%'; }
      else { isr = 79776 + (monto - 867123) * 0.25; tramo = '25%'; }
    }

    document.getElementById('isr-valor').textContent = fmt(isr);
    document.getElementById('isr-ingreso').textContent = fmt(monto);
    document.getElementById('isr-tramo').textContent = tramo;
    document.getElementById('isr-mensual').textContent = fmt(isr / 12);
    document.getElementById('isr-result').classList.add('visible');
  }

  // ── CALCULADORA ANTICIPOS
  function calcAnticipos() {
    const monto = parseFloat(document.getElementById('ant-monto').value) || 0;
    if (monto <= 0) return;
    const fmt = v => 'RD$ ' + v.toLocaleString('es-DO', {minimumFractionDigits:2, maximumFractionDigits:2});
    const total = monto * 1.5;
    const cuota = total / 12;
    document.getElementById('ant-cuota').textContent = fmt(cuota);
    document.getElementById('ant-total').textContent = fmt(total);
    document.getElementById('ant-base').textContent = fmt(monto) + ' × 1.5';
    document.getElementById('ant-result').classList.add('visible');
  }

  function switchCalc(tab, btn) {
    document.querySelectorAll('.calc-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.calc-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('calc-' + tab).classList.add('active');
  }

  // ── CHAT IA
  let chatHistory = [];

  function getTime() {
    const n = new Date();
    return n.getHours().toString().padStart(2,'0') + ':' + n.getMinutes().toString().padStart(2,'0');
  }

  function appendMsg(role, text) {
    const wrap = document.getElementById('chat-messages');
    const div = document.createElement('div');
    div.className = 'msg ' + role;
    if (role === 'bot') {
      div.innerHTML = `<div class="bot-avatar"><span>.JC</span></div><div class="msg-bubble">${text}</div><div class="msg-time">${getTime()}</div>`;
    } else {
      div.innerHTML = `<div class="msg-bubble">${text}</div><div class="msg-time">${getTime()}</div>`;
    }
    wrap.appendChild(div);
    wrap.scrollTop = wrap.scrollHeight;
    return div;
  }

  function showTyping() {
    const wrap = document.getElementById('chat-messages');
    const div = document.createElement('div');
    div.className = 'msg bot'; div.id = 'typing-div';
    div.innerHTML = `<div class="bot-avatar"><span>.JC</span></div><div class="typing-indicator"><span></span><span></span><span></span></div>`;
    wrap.appendChild(div);
    wrap.scrollTop = wrap.scrollHeight;
  }

  function removeTyping() {
    const t = document.getElementById('typing-div');
    if (t) t.remove();
  }

  function enviarChip(el) {
    document.getElementById('chat-input').value = el.textContent;
    enviarMensaje();
    document.getElementById('chat-chips').style.display = 'none';
  }

  async function enviarMensaje() {
    const input = document.getElementById('chat-input');
    const msg = input.value.trim();
    if (!msg) return;

    const btn = document.getElementById('chat-send');
    input.value = ''; btn.disabled = true;
    appendMsg('user', msg);

    chatHistory.push({ role: 'user', content: msg });
    showTyping();

    try {
      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 600,
          system: `Eres el asistente fiscal de Jonathan Constanza, CPA y Data Analyst dominicano. Respondes consultas sobre fiscalidad dominicana (DGII, ITBIS, ISR, TSS, facturación electrónica e-CF, Código Tributario). Tus respuestas son concisas, directas y técnicas, adaptadas al contexto dominicano. Máximo 3 párrafos cortos. Si no tienes certeza de algo, dilo claramente y sugiere consultar directamente a Jonathan.`,
          messages: chatHistory
        })
      });
      const data = await res.json();
      const reply = data.content?.map(b => b.text || '').join('') || 'No pude generar una respuesta. Intenta de nuevo.';
      removeTyping();
      appendMsg('bot', reply);
      chatHistory.push({ role: 'assistant', content: reply });
    } catch (e) {
      removeTyping();
      appendMsg('bot', 'Error de conexión. Verifica tu internet e intenta de nuevo.');
    }

    btn.disabled = false;
    input.focus();
  }

  document.getElementById('chat-input').addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); enviarMensaje(); }
  });

  // ── BLOG IA
  function setBlogTema(el) {
    document.getElementById('blog-input').value = el.textContent;
    document.getElementById('blog-input').focus();
  }

  async function generarBlog() {
    const tema = document.getElementById('blog-input').value.trim();
    if (!tema) return;

    const btn = document.getElementById('blog-btn');
    const btnText = document.getElementById('blog-btn-text');
    btnText.innerHTML = '<span class="spinner"></span>Generando…';
    btn.disabled = true;
    document.getElementById('blog-result').classList.remove('visible');

    try {
      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1000,
          messages: [{
            role: 'user',
            content: `Eres Jonathan Constanza, CPA y Data Analyst dominicano con 10+ años de experiencia en consultoría fiscal y financiera en República Dominicana. Tu estilo es profesional, directo y con autoridad técnica.

Genera un artículo de blog sobre: "${tema}"

Incluye:
- Título atractivo orientado al empresario dominicano
- 3 secciones con subtítulos
- Referencias a regulaciones dominicanas (DGII, TSS, Código Tributario, e-CF) cuando aplique
- Párrafo final con llamada a la acción para agendar consultoría con Jonathan Constanza
- Tono experto pero accesible
- 300-400 palabras`
          }]
        })
      });
      const data = await res.json();
      const text = data.content?.map(b => b.text || '').join('') || 'No se pudo generar el artículo.';
      document.getElementById('blog-content').textContent = text;
      document.getElementById('blog-result').classList.add('visible');
    } catch (e) {
      document.getElementById('blog-content').textContent = 'Error de conexión. Intenta de nuevo.';
      document.getElementById('blog-result').classList.add('visible');
    }

    btnText.textContent = '✦ Generar artículo';
    btn.disabled = false;
  }

  function copiarBlog() {
    const text = document.getElementById('blog-content').textContent;
    navigator.clipboard.writeText(text).then(() => showToast('✓ Artículo copiado'));
  }
</script>
</body>
</html>
