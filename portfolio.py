# portfolio.py
# Professional Business Portfolio Website using Streamlit
# High-Converting POS & Custom Software Solutions Marketplace

import streamlit as st
import requests

# ---------------- 1. ALWAYS FIRST: SINGLE PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="MZ Professional Tools",
    page_icon="💼",
    layout="wide",
)

# ---------------- 2. CONSOLIDATED PREMIUM MASTER CSS ---------------- #
st.markdown("""
<style>
/* Main Background & Base Styling */
html {
    scroll-behavior: smooth;
}

.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #1e293b);
    color: #f8fafc;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* Remove Streamlit Default Header/Footer */
#MainMenu, footer, header {
    visibility: hidden;
    display: none;
}

/* Sticky Navigation Bar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(2, 6, 23, 0.9);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    z-index: 9999;
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 18px 0;
    border-bottom: 1px solid rgba(6, 182, 212, 0.15);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
    flex-wrap: wrap;
}

.navbar a {
    color: #94a3b8;
    text-decoration: none;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    padding: 5px 12px;
    border-radius: 8px;
}

.navbar a:hover {
    color: #06b6d4;
    background: rgba(6, 182, 212, 0.08);
    transform: translateY(-1px);
}

/* Offset for sections so navbar doesn't cover titles */
.section-anchor {
    scroll-margin-top: 110px;
}

/* Main Container */
.main-container {
    padding: 6rem 5% 2rem;
}

/* Startup Welcome Animation */
.welcome-overlay {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 800;
    color: #06b6d4;
    letter-spacing: 1.5px;
    animation: welcomeFade 4.5s ease-in-out forwards;
    overflow: hidden;
    text-shadow: 0 0 25px rgba(6, 182, 212, 0.6);
    margin-top: 40px;
}

@keyframes welcomeFade {
    0% { opacity: 0; transform: translateY(-20px); max-height: 100px; padding-top: 30px; padding-bottom: 20px;}
    15% { opacity: 1; transform: translateY(0); max-height: 100px; padding-top: 30px; padding-bottom: 20px;}
    80% { opacity: 1; transform: translateY(0); max-height: 100px; padding-top: 30px; padding-bottom: 20px;}
    100% { opacity: 0; max-height: 0; padding-top: 0; padding-bottom: 0; margin: 0; transform: translateY(-20px); }
}

/* Hero Section */
.hero-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 60px;
    padding: 60px 4% 40px;
    max-width: 1300px;
    margin: auto;
}
.hero-text {
    text-align: left;
    flex: 1.2;
}
.hero-text h1 {
    font-size: 4.5rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 16px;
    line-height: 1.15;
    background: linear-gradient(to right, #ffffff, #cbd5e1, #06b6d4, #10b981);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-text p {
    font-size: 1.6rem;
    color: #38bdf8;
    margin-top: 0;
    font-weight: 500;
    letter-spacing: 0.5px;
}
.hero-image-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 0.8;
}
.hero-image {
    width: 340px;
    height: 340px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid rgba(6, 182, 212, 0.4);
    box-shadow: 0 0 40px rgba(6, 182, 212, 0.25);
    transition: all 0.4s ease;
}
.hero-image:hover {
    transform: scale(1.03) rotate(1s);
    border-color: #10b981;
    box-shadow: 0 0 50px rgba(16, 185, 129, 0.4);
}

/* Section Titles */
.section-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #f43f5e;
    margin-top: 70px;
    margin-bottom: 35px;
    text-align: center;
    position: relative;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-shadow: 0 0 15px rgba(244, 63, 94, 0.2);
}

/* Unified Premium Card Matrix System (The Pricing Section Layout Bug Fix) */
.matrix-wrapper {
    display: flex;
    justify-content: center;
    gap: 25px;
    flex-wrap: wrap;
    margin-top: 20px;
    padding-bottom: 20px;
}

.matrix-card {
    background: rgba(30, 41, 59, 0.45);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 40px 30px;
    width: 300px;
    text-align: left;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.matrix-card:hover {
    transform: translateY(-10px);
    border-color: #06b6d4;
    box-shadow: 0 25px 50px rgba(6, 182, 212, 0.2);
    background: rgba(30, 41, 59, 0.7);
}

/* Card Accent Varieties */
.matrix-card.accent-rose { border-left: 4px solid #f43f5e; }
.matrix-card.accent-emerald { border-left: 4px solid #10b981; }
.matrix-card.accent-cyan { border-left: 4px solid #06b6d4; }
.matrix-card.accent-amber { border-left: 4px solid #f59e0b; }

.matrix-card-icon {
    font-size: 3rem;
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.04);
    width: 70px;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.matrix-card-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
}

.matrix-card-desc {
    color: #cbd5e1;
    font-size: 1.05rem;
    line-height: 1.6;
    margin-bottom: 15px;
}

/* About Box Container Upgrades */
.premium-showcase-box {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(6, 182, 212, 0.15);
    padding: 55px;
    border-radius: 28px;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4);
    margin-bottom: 50px;
    position: relative;
}

.showcase-header {
    font-size: 2rem;
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 25px;
    text-align: center;
    letter-spacing: 0.5px;
}

.showcase-text {
    color: #cbd5e1;
    font-size: 1.2rem;
    line-height: 1.9;
    text-align: center;
    max-width: 950px;
    margin: 0 auto 40px auto;
}

.showcase-text strong {
    color: #06b6d4;
    font-weight: 600;
}

.stats-matrix {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 30px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 35px;
}

.stat-matrix-item {
    text-align: center;
    min-width: 180px;
}

.stat-matrix-item h4 {
    font-size: 2.8rem;
    color: #10b981;
    margin: 0;
    font-weight: 800;
    text-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
}

.stat-matrix-item p {
    color: #94a3b8;
    font-size: 1.1rem;
    margin: 8px 0 0 0;
    font-weight: 500;
}

/* Tech Stack Badge Containers */
.tech-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 50px;
}

.tech-badge {
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(6, 182, 212, 0.25);
    color: #f1f5f9;
    padding: 14px 28px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.tech-badge:hover {
    background: linear-gradient(135deg, #06b6d4, #0891b2);
    color: #020617;
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(6, 182, 212, 0.4);
    border-color: #06b6d4;
}

/* HTML Table Matrix Styling for Comparison */
.matrix-table-wrapper {
    overflow-x: auto;
    margin: 30px 0;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);
}
.matrix-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    background: rgba(15, 23, 42, 0.4);
}
.matrix-table th, .matrix-table td {
    padding: 16px 22px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.matrix-table th {
    background: rgba(30, 41, 59, 0.8);
    color: #ffffff;
    font-weight: 700;
}
.matrix-table tr:hover {
    background: rgba(255, 255, 255, 0.02);
}

/* Dropdown list resets inside cards */
details { margin-top: 15px; width: 100%; }
details summary {
    cursor: pointer; color: #06b6d4; font-weight: 600; font-size: 0.95rem;
    padding: 10px; background: rgba(6, 182, 212, 0.06); 
    border: 1px solid rgba(6, 182, 212, 0.15); border-radius: 12px; 
    transition: all 0.3s ease; text-align: center; list-style: none;
}
details summary::-webkit-details-marker { display: none; }
details summary:hover { background: rgba(6, 182, 212, 0.15); border-color: #06b6d4; }
details ul { color: #cbd5e1; padding-left: 5px; margin-top: 12px; list-style-type: none; }
details ul li { position: relative; margin-bottom: 8px; padding-left: 18px; font-size: 0.95rem; }
details ul li::before { content: "⚡"; position: absolute; left: 0; top: 1px; font-size: 0.85rem; }

/* Pricing Elements Unification Layout */
.pricing-container {
    display: flex;
    justify-content: center;
    gap: 25px;
    flex-wrap: wrap;
    margin-top: 30px;
}

.pricing-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 45px 30px;
    width: 290px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.pricing-card:hover {
    transform: translateY(-12px);
    border-color: #06b6d4;
    box-shadow: 0 30px 60px rgba(6, 182, 212, 0.25);
    background: rgba(30, 41, 59, 0.65);
}

.pricing-card.premium-card {
    border: 1px solid rgba(244, 63, 94, 0.4);
    box-shadow: 0 20px 40px rgba(244, 63, 94, 0.15);
}
.pricing-card.premium-card:hover {
    border-color: #f43f5e;
    box-shadow: 0 30px 60px rgba(244, 63, 94, 0.3);
}

.plan-badge {
    position: absolute;
    top: 18px;
    right: -33px;
    background: linear-gradient(135deg, #f43f5e, #be123c);
    color: white;
    padding: 4px 35px;
    font-size: 0.75rem;
    font-weight: bold;
    transform: rotate(45deg);
    letter-spacing: 0.5px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.plan-badge.green-badge { background: linear-gradient(135deg, #10b981, #047857); }
.plan-badge.blue-badge { background: linear-gradient(135deg, #06b6d4, #0369a1); }

.pricing-title { font-size: 1.5rem; color: #ffffff; font-weight: 700; }
.pricing-sub { font-size: 0.95rem; color: #94a3b8; margin-bottom: 15px; }
.pricing-price { font-size: 2.8rem; font-weight: 800; color: #ffffff; margin: 15px 0; }
.pricing-price span { font-size: 1.1rem; color: #06b6d4; font-weight: 600; }
.pricing-card.premium-card .pricing-price span { color: #f43f5e; }

.plan-features { text-align: left; list-style: none; padding: 0; margin: 20px 0 35px 0; flex-grow: 1; }
.plan-features li { color: #cbd5e1; font-size: 0.98rem; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
.plan-features li::before { content: "✓"; color: #10b981; font-weight: bold; font-size: 1.1rem; }
.pricing-card.premium-card .plan-features li::before { color: #f43f5e; }

.wa-btn {
    display: block; padding: 14px; background: linear-gradient(135deg, #06b6d4, #0284c7);
    color: #020617 !important; text-decoration: none; border-radius: 14px; font-weight: 700;
    transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(6, 182, 212, 0.25); text-align: center;
}
.pricing-card.premium-card .wa-btn {
    background: linear-gradient(135deg, #f43f5e, #e11d48); color: white !important;
    box-shadow: 0 4px 15px rgba(244, 63, 94, 0.3);
}
.wa-btn:hover { transform: scale(1.02); filter: brightness(1.15); }

/* Native Streamlit Element Overrides (Forms & Inputs Glow) */
div.stButton > button {
    width: 100%; background-color: #1e293b !important; color: #f8fafc !important;
    border: 1px solid rgba(255,255,255,0.08) !important; padding: 18px !important;
    text-align: left !important; font-size: 16px !important; font-weight: 600 !important;
    border-radius: 12px !important; margin-bottom: 4px !important; transition: all 0.25s ease !important;
}
div.stButton > button:hover {
    background-color: #334155 !important; border-color: #06b6d4 !important;
    box-shadow: 0 0 12px rgba(6, 182, 212, 0.2);
}

.answer-box {
    background: #0b1329; padding: 22px; border-left: 5px solid #06b6d4;
    border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);
    border-radius: 0 0 12px 12px; color: #cbd5e1; margin-bottom: 18px; font-size: 16px; line-height: 1.6;
}

label { color: #f1f5f9 !important; font-weight: 600 !important; margin-bottom: 6px !important; }
div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > textarea {
    background-color: #0f172a !important; border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important; transition: all 0.3s ease !important;
}
input, textarea { color: #ffffff !important; }
div[data-baseweb="input"] > div:focus-within, div[data-baseweb="textarea"] > textarea:focus {
    box-shadow: 0 0 18px rgba(6, 182, 212, 0.35) !important; border-color: #06b6d4 !important;
}

div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #f43f5e, #be123c) !important; color: white !important;
    border: none !important; border-radius: 50px !important; padding: 12px 40px !important;
    font-weight: 700 !important; transition: all 0.3s ease !important; width: auto !important; text-align: center !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px); box-shadow: 0 6px 20px rgba(244, 63, 94, 0.4) !important;
}

/* Contact Block Stylings */
.contact-box {
    text-align: center; padding: 65px 40px; margin-top: 70px;
    background: rgba(15, 23, 42, 0.5); backdrop-filter: blur(20px); border-radius: 28px;
    border: 1px solid rgba(6, 182, 212, 0.15); box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}
.call-btn {
    display: inline-block; padding: 16px 45px; font-size: 1.1rem; font-weight: 700; color: white !important;
    background: linear-gradient(135deg, #10b981, #059669); border-radius: 50px; text-decoration: none;
    transition: all 0.3s; box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
}
.call-btn:hover { transform: translateY(-3px); box-shadow: 0 12px 35px rgba(16, 185, 129, 0.5); }

/* Responsive Adaptations */
@media (max-width: 900px) {
    .navbar { gap: 10px; padding: 12px 5px; }
    .navbar a { font-size: 0.9rem; padding: 4px 8px; }
    .hero-container { flex-direction: column; text-align: center; gap: 35px; padding-top: 80px; }
    .hero-text { text-align: center; }
    .hero-text h1 { font-size: 3.2rem; }
    .hero-image { width: 260px; height: 260px; }
    .matrix-card, .pricing-card { width: 100%; }
}
</style>

<nav class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#tech">Tech Stack</a>
    <a href="#services">Services</a>
    <a href="#modules">POS Modules</a>
    <a href="#calculator">ROI Calculator</a>
    <a href="#features">Why Choose Us</a>
    <a href="#ledger">Khata Ledger</a>  
    <a href="#hardware">Hardware Matrix</a>
    <a href="#process">Our Process</a>
    <a href="#pricing">Pricing Plans</a>
    <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTAINER ---------------- #
st.markdown('<div id="home" class="main-container section-anchor">', unsafe_allow_html=True)

# Welcome Banner
st.markdown('<div class="welcome-overlay">✨ Welcome to Muhammad Zubair Officials ✨</div>', unsafe_allow_html=True)

# Hero Section Header
st.markdown("""
<div class="hero-container">
    <div class="hero-text">
        <h1>MZ Professional Tools</h1>
        <p>Premium Retail POS, Pharmacy Suites & Enterprise Software Solutions</p>
    </div>
    <div class="hero-image-wrapper">
        <img src="https://raw.githubusercontent.com/freefire445879-spec/mz-software-portfolio/main/1767490334321.jpg" alt="Muhammad Zubair" class="hero-image">
    </div>
</div>
""", unsafe_allow_html=True)

# About Developer Section
st.markdown('<div id="about" class="section-title section-anchor">About The Developer</div>', unsafe_allow_html=True)
st.markdown("""
<div class="premium-showcase-box">
    <div class="showcase-header">Architecting High-Speed Business Softwares</div>
    <div class="showcase-text">
        <strong>Muhammad Zubair</strong> (from <strong>Daska, Sialkot</strong>) is an expert Software Developer specializing in ultra-responsive retail automations, local data structures, and intuitive workflows.<br><br>
        I build high-performance business applications such as standalone Windows desktop environments and secure web-based dashboards. By engineering custom business algorithms, I replace slow, outdated software and manual paperwork with secure, lightning-fast digital solutions tailored precisely to your operational workflow.
    </div>
    <div class="stats-matrix">
        <div class="stat-matrix-item"><h4>100%</h4><p>Data Privacy (Offline)</p></div>
        <div class="stat-matrix-item"><h4>Zero</h4><p>Monthly Rental Fees</p></div>
        <div class="stat-matrix-item"><h4>Instant</h4><p>Local File Backups</p></div>
        <div class="stat-matrix-item"><h4>24/7</h4><p>Priority Setup Support</p></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Tech Stack Section
st.markdown('<div id="tech" class="section-title section-anchor">Core Technologies & Systems</div>', unsafe_allow_html=True)
st.markdown("""
<div class="tech-container">
    <div class="tech-badge">🐍 Advanced Python Engineering</div>
    <div class="tech-badge">📊 Streamlit UI Architecture</div>
    <div class="tech-badge">🗄️ Relational SQL Databases</div>
    <div class="tech-badge">🛡️ Multi-User Authentication Lock</div>
    <div class="tech-badge">⚙️ High-Speed Invoicing Engines</div>
    <div class="tech-badge">📦 Standalone Executable Deployment</div>
</div>
""", unsafe_allow_html=True)

# Core Business Services (Unified Matrix Card System Layout)
st.markdown('<div id="services" class="section-title section-anchor">Core Business Offerings</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-wrapper">
    <div class="matrix-card accent-cyan">
        <div>
            <div class="matrix-card-icon">🛒</div>
            <div class="matrix-card-title">Retail POS Systems</div>
            <div class="matrix-card-desc">End-to-end billing and automated inventory infrastructure built for high-traffic retail outlets.</div>
            <details>
                <summary>Explore Retail Features</summary>
                <ul>
                    <li>Real-time automated barcode stock deduction.</li>
                    <li>Dynamic multi-tiered discount calculators.</li>
                    <li>Anti-theft cash drawer transaction recording.</li>
                    <li>Low-stock notification trigger flags.</li>
                </ul>
            </details>
        </div>
    </div>

    <div class="matrix-card accent-rose">
        <div>
            <div class="matrix-card-icon">💊</div>
            <div class="matrix-card-title">Pharmacy POS Suites</div>
            <div class="matrix-card-desc">Advanced medical billing tools with batch number logging and automatic expiry sequence tracking.</div>
            <details>
                <summary>Explore Pharmacy Features</summary>
                <ul>
                    <li>Smart batch tracking with active alert systems.</li>
                    <li>Formula substitute and group drug lookups.</li>
                    <li>Distributor credit and purchase order tracking.</li>
                    <li>Drug Regulatory compliant reporting layouts.</li>
                </ul>
            </details>
        </div>
    </div>

    <div class="matrix-card accent-emerald">
        <div>
            <div class="matrix-card-icon">⚙️</div>
            <div class="matrix-card-title">Custom Business Apps</div>
            <div class="matrix-card-desc">Tailor-made system architectures engineered specifically to match your exact business workflow.</div>
            <details>
                <summary>Explore Custom Features</summary>
                <ul>
                    <li>Unique business logic and reporting views.</li>
                    <li>Scalable local server database links.</li>
                    <li>No locked subscription or hidden overheads.</li>
                    <li>Direct data loading pipeline integrations.</li>
                </ul>
            </details>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# NEW DEEP-DIVE SECTION: POS ADVANCED MODULE SHOWCASE
st.markdown('<div id="modules" class="section-title section-anchor">Inside ZUBAIR.POS.OFFICIAL</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-wrapper">
    <div class="matrix-card accent-cyan">
        <div>
            <div class="matrix-card-icon">📈</div>
            <div class="matrix-card-title">Sales Analytics</div>
            <div class="matrix-card-desc">Track sales dashboards showing exact net margins, gross values, and cash-in-hand changes instantly.</div>
        </div>
    </div>
    <div class="matrix-card accent-amber">
        <div>
            <div class="matrix-card-icon">📦</div>
            <div class="matrix-card-title">Stock Auditing</div>
            <div class="matrix-card-desc">Bulk excel inventory uploads, manual stock increments, and real-time purchase cost re-evaluation logs.</div>
        </div>
    </div>
    <div class="matrix-card accent-emerald">
        <div>
            <div class="matrix-card-icon">👥</div>
            <div class="matrix-card-title">Staff Access Controls</div>
            <div class="matrix-card-desc">Secure permission matrix configurations preventing operators from deleting invoices or editing item prices.</div>
        </div>
    </div>
    <div class="matrix-card accent-rose">
        <div>
            <div class="matrix-card-icon">🧾</div>
            <div class="matrix-card-title">Thermal Invoicing</div>
            <div class="matrix-card-desc">Flawless 80mm/58mm thermal output generation with custom Urdu/English footers and store logos.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# NEW NATIVE INTERACTIVE SECTION: LIVE BUSINESS ROI SAVINGS CALCULATOR
st.markdown('<div id="calculator" class="section-title section-anchor">Interactive ROI Calculator</div>', unsafe_allow_html=True)
st.markdown("""
<div class="premium-showcase-box" style="border-color: #10b981; padding: 40px 35px; margin-bottom: 30px;">
    <h3 style="color:#ffffff; margin-top:0; font-size:1.6rem; text-align:center; margin-bottom:15px;">Calculate Your Monthly Savings With Our POS</h3>
    <p style="color:#94a3b8; text-align:center; margin-bottom:30px;">Adjust the sliders below based on your current manual retail or shop operations to see your estimated savings.</p>
</div>
""", unsafe_allow_html=True)

# Interactive Calculator Calculations using native Streamlit columns
calc_col1, calc_col2 = st.columns(2)

with calc_col1:
    daily_hours_lost = st.slider("Daily manual bookkeeping & billing hours spent:", 1, 6, 3)
    hourly_rate_estimate = st.slider("Estimated value of your time per hour (Rs):", 100, 1000, 300, step=50)
    monthly_leakage = st.number_input("Estimated monthly losses from unrecorded credit (Udhaar/Theft) (Rs):", min_value=0, max_value=50000, value=4000, step=500)

# ROI Logic
time_saved_money = daily_hours_lost * hourly_rate_estimate * 30
total_monthly_saved = time_saved_money + monthly_leakage
yearly_saved = total_monthly_saved * 12

with calc_col2:
    st.markdown(f"""
    <div class="matrix-card accent-emerald" style="width:100%; height:100%; justify-content:center; padding:35px; background:rgba(16, 185, 129, 0.05); border:1px solid rgba(16,185,129,0.3);">
        <h4 style="margin:0; color:#10b981; font-size:1.4rem; text-align:center;">YOUR ESTIMATED SYSTEM ROI</h4>
        <div style="text-align:center; margin:20px 0;">
            <p style="margin:5px 0; color:#94a3b8; font-size:1rem;">Monthly Recovered Capital</p>
            <h2 style="margin:0; color:#ffffff; font-size:2.8rem; font-weight:800;">Rs {total_monthly_saved:,}</h2>
        </div>
        <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:15px; text-align:center;">
            <p style="margin:0; color:#cbd5e1; font-size:1.1rem;">Estimated Yearly Protection: <strong>Rs {yearly_saved:,}</strong></p>
            <p style="margin:8px 0 0 0; color:#94a3b8; font-size:0.85rem; font-style:italic;">System pays for itself within the first few weeks of setup.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Strategic Conversion Feature Pillars
st.markdown('<div id="features" class="section-title section-anchor">Engineered for Profitability</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-wrapper">
    <div class="matrix-card accent-rose">
        <div>
            <div class="matrix-card-icon">📈</div>
            <div class="matrix-card-title">Advanced Profit Dashboards</div>
            <div class="matrix-card-desc">Stop guessing your store performance. Instantly analyze your exact net profit metrics across any date range and immediately identify your highest-earning inventory assets.</div>
        </div>
    </div>

    <div class="matrix-card accent-cyan">
        <div>
            <div class="matrix-card-icon">💰</div>
            <div class="matrix-card-title">Smart Collection Reports</div>
            <div class="matrix-card-desc">Protect your liquid cash flows. Keep real-time ledgers of all outstanding balances, track customer payment delays, and keep credit history organized under a safe view.</div>
        </div>
    </div>

    <div class="matrix-card accent-emerald">
        <div>
            <div class="matrix-card-icon">🛠️</div>
            <div class="matrix-card-title">100% Bespoke Business Rules</div>
            <div class="matrix-card-desc">Get a software engine modeled around your real operations. Never compromise your workflow logic for generic, low-cost commercial cloud tool restrictions.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Khata Ledger System Spotlight
st.markdown('<div id="ledger" class="section-title section-anchor">Digital Khata & Loyalty Ledger</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-wrapper">
    <div class="matrix-card accent-cyan" style="width:31%; min-width:280px;">
        <div>
            <div class="matrix-card-icon">📖</div>
            <div class="matrix-card-title">Unified Customer Credit Ledger</div>
            <div class="matrix-card-desc">Replace manual record notebooks with digital logs. View unified credit limits, track total receipts, and compute balance figures instantly during active checkout sequences.</div>
        </div>
    </div>

    <div class="matrix-card accent-amber" style="width:31%; min-width:280px;">
        <div>
            <div class="matrix-card-icon">🎁</div>
            <div class="matrix-card-title">Automated Customer Loyalty Points</div>
            <div class="matrix-card-desc">Retain your retail buyers. The embedded points engine tracks purchasing volumes automatically, converting regular activity into promotional discounts and rewards.</div>
        </div>
    </div>

    <div class="matrix-card accent-rose" style="width:31%; min-width:280px;">
        <div>
            <div class="matrix-card-icon">📜</div>
            <div class="matrix-card-title">Complete Historical Auditing</div>
            <div class="matrix-card-desc">Never lose transaction traces. Access chronological purchasing histories, review previously applied cash values, and reprint duplicate bill copies with a single click.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# NEW DEEP-DIVE SECTION: HARDWARE COMPATIBILITY MATRIX
st.markdown('<div id="hardware" class="section-title section-anchor">Hardware & Infrastructure Support</div>', unsafe_allow_html=True)
st.markdown("""
<div class="premium-showcase-box" style="padding:40px;">
    <div class="showcase-header">Plug-and-Play Hardware Integration Matrix</div>
    <p style="color:#cbd5e1; text-align:center; margin-bottom:30px;">Our standalone desktop solutions operate perfectly with standard retail peripheral items without requiring third-party configuration files.</p>
    <div class="matrix-table-wrapper">
        <table class="matrix-table">
            <thead>
                <tr>
                    <th>Peripheral Device</th>
                    <th>Supported Protocols / Models</th>
                    <th>System Response Speed</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Thermal Receipt Printers</strong></td>
                    <td>Xprinter, Rongta, Epson (80mm / 58mm USB & Network)</td>
                    <td>&lt; 150 Milliseconds Output</td>
                    <td style="color:#10b981; font-weight:bold;">✓ Fully Native</td>
                </tr>
                <tr>
                    <td><strong>Barcode Scanners</strong></td>
                    <td>All 1D / 2D Laser Handheld & Omnidirectional Scanners</td>
                    <td>Instant Input Capture</td>
                    <td style="color:#10b981; font-weight:bold;">✓ Fully Native</td>
                </tr>
                <tr>
                    <td><strong>Electronic Cash Drawers</strong></td>
                    <td>RJ11 Pulse Trigger Outlines (Automatic on Print command)</td>
                    <td>Real-time Relay Kick</td>
                    <td style="color:#10b981; font-weight:bold;">✓ Fully Native</td>
                </tr>
                <tr>
                    <td><strong>Local Data Networks</strong></td>
                    <td>SQLite Local File Storage & Local Area Multi-PC Sync</td>
                    <td>Zero Latency Offline Lookups</td>
                    <td style="color:#10b981; font-weight:bold;">✓ Fully Native</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
""", unsafe_allow_html=True)


# Verified Client Feedback Section
st.markdown('<div id="testimonials" class="section-title section-anchor">Client Success Stories</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-wrapper">
    <div class="matrix-card accent-cyan" style="width:47%; min-width:320px;">
        <div>
            <div style="font-size:1.5rem; color:#f59e0b; margin-bottom:10px;">⭐⭐⭐⭐⭐</div>
            <p style="font-style:italic; color:#cbd5e1; font-size:1.05rem; line-height:1.6;">"MZ Professional Tools ka POS system use kar raha hoon. Mera stock aur profit manage karna ab baccho ka khel hai. Barcode printing aur automatic billing ne hamara bohot waqt bachaya hai. Highly recommended!"</p>
            <h4 style="margin-top:20px; color:#ffffff; font-size:1.1rem; display:flex; align-items:center; gap:8px;">🛍️ Malik General Store <span style="font-size:0.85rem; color:#94a3b8; font-weight:normal;">— Daska</span></h4>
        </div>
    </div>

    <div class="matrix-card accent-rose" style="width:47%; min-width:320px;">
        <div>
            <div style="font-size:1.5rem; color:#f59e0b; margin-bottom:10px;">⭐⭐⭐⭐⭐</div>
            <p style="font-style:italic; color:#cbd5e1; font-size:1.05rem; line-height:1.6;">"Pharmacy POS ne meri zindagi asaan kar di. Expiry date tracking aur medicine management behtareen hai. Batch calculation automatically ho jati hai aur customer ka record dhoondna bohot fast hai."</p>
            <h4 style="margin-top:20px; color:#ffffff; font-size:1.1rem; display:flex; align-items:center; gap:8px;">💊 City Pharmacy <span style="font-size:0.85rem; color:#94a3b8; font-weight:normal;">— Sialkot District</span></h4>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Systematic Operational Process Showcase
st.markdown('<div id="process" class="section-title section-anchor">System Engineering Process</div>', unsafe_allow_html=True)
st.markdown("""
<div class="matrix-wrapper">
    <div class="matrix-card accent-rose" style="width:220px;">
        <div>
            <div class="matrix-card-icon" style="font-size:2rem; width:50px; height:50px;">📝</div>
            <div class="matrix-card-title" style="font-size:1.2rem;">1. Rule Analysis</div>
            <div class="matrix-card-desc" style="font-size:0.95rem;">Evaluating your inventory configurations and checkout rules.</div>
        </div>
    </div>
    <div class="matrix-card accent-cyan" style="width:220px;">
        <div>
            <div class="matrix-card-icon" style="font-size:2rem; width:50px; height:50px;">🎨</div>
            <div class="matrix-card-title" style="font-size:1.2rem;">2. Custom Layout</div>
            <div class="matrix-card-desc" style="font-size:0.95rem;">Structuring user interfaces optimized for high checkouts.</div>
        </div>
    </div>
    <div class="matrix-card accent-amber" style="width:220px;">
        <div>
            <div class="matrix-card-icon" style="font-size:2rem; width:50px; height:50px;">💻</div>
            <div class="matrix-card-title" style="font-size:1.2rem;">3. Secure Code</div>
            <div class="matrix-card-desc" style="font-size:0.95rem;">Writing fast local algorithms utilizing clean data structures.</div>
        </div>
    </div>
    <div class="matrix-card accent-emerald" style="width:220px;">
        <div>
            <div class="matrix-card-icon" style="font-size:2rem; width:50px; height:50px;">🚀</div>
            <div class="matrix-card-title" style="font-size:1.2rem;">4. Deployment</div>
            <div class="matrix-card-desc" style="font-size:0.95rem;">On-site or remote setup alongside lifetime security backups.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# FIXED & UPGRADED: PREMIUM COMPLIANT PRICING LAYOUT
# ----------------------------------------------------
st.markdown('<div id="pricing" class="section-title section-anchor">Software Pricing Model Plans</div>', unsafe_allow_html=True)
st.markdown("""
<div class="pricing-container">
    <div class="pricing-card">
        <div>
            <div class="plan-badge green-badge">Demo</div>
            <div class="pricing-title">7-Day Free Trial</div>
            <div class="pricing-sub">Test before commitment</div>
            <div class="pricing-price">Rs 0<span> /7 Days</span></div>
            <ul class="plan-features">
                <li>Full Access to POS Modules</li>
                <li>Khata Ledger Management</li>
                <li>Test with Real-world Data</li>
                <li>Basic Installation Support</li>
            </ul>
        </div>
        <a href="https://wa.me/923476712269?text=I%20want%20to%20get%20a%207-Day%20Free%20Trial" class="wa-btn">Try For Free</a>
    </div>

    <div class="pricing-card">
        <div>
            <div class="plan-badge blue-badge">Standard</div>
            <div class="pricing-title">1-Year License</div>
            <div class="pricing-sub">Perfect for running shops</div>
            <div class="pricing-price">Rs 2,000<span> /Year</span></div>
            <ul class="plan-features">
                <li>All Core Functions Working</li>
                <li>Secure Online Backup System</li>
                <li>Expiry & Inventory Tracking</li>
                <li>Standard Customer Ledger</li>
            </ul>
        </div>
        <a href="https://wa.me/923476712269?text=I%20want%20to%20get%20a%201-Year%20License" class="wa-btn">Buy License</a>
    </div>

    <div class="pricing-card premium-card">
        <div>
            <div class="plan-badge">Popular</div>
            <div class="pricing-title">2-Year License</div>
            <div class="pricing-sub">Optimized for growth</div>
            <div class="pricing-price">Rs 3,500<span> /2 Yrs</span></div>
            <ul class="plan-features">
                <li>All 1-Year Functional Features</li>
                <li>Optimized High-Speed Workflows</li>
                <li>Advanced Key Performance Tools</li>
                <li>Priority Local/Cloud Backup</li>
            </ul>
        </div>
        <a href="https://wa.me/923476712269?text=I%20want%20to%20get%20a%202-Year%20License" class="wa-btn">Go Pro</a>
    </div>

    <div class="pricing-card">
        <div>
            <div class="plan-badge blue-badge">Ultimate</div>
            <div class="pricing-title">Lifetime Access</div>
            <div class="pricing-sub">Ultimate control forever</div>
            <div class="pricing-price">Rs 20,000<span> /Once</span></div>
            <ul class="plan-features">
                <li>All System Functions Unlocked</li>
                <li>100% Custom Changes Supported</li>
                <li>Tailored Workflows To Your Rules</li>
                <li>Lifetime Free Upgrades</li>
            </ul>
        </div>
        <a href="https://wa.me/923476712269?text=I%20want%20to%20get%20Lifetime%20Access" class="wa-btn">Get Lifetime</a>
    </div>
</div>
""", unsafe_allow_html=True)


# NEW DEEP-DIVE SECTION: PLAN VALUE COMPARISON MATRIX TABLE
st.markdown('<div class="section-title">Plans Comparison Matrix</div>', unsafe_allow_html=True)
st.markdown("""
<div class="premium-showcase-box" style="padding:35px;">
    <div class="matrix-table-wrapper">
        <table class="matrix-table">
            <thead>
                <tr>
                    <th>Features Matrix</th>
                    <th>Free Trial</th>
                    <th>Annual Licenses</th>
                    <th>Lifetime Ultimate Plan</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Billing & Invoicing Engine</strong></td>
                    <td>✓ Active</td>
                    <td>✓ Active</td>
                    <td>✓ Active</td>
                </tr>
                <tr>
                    <td><strong>Automatic Cloud Mirror Sync</strong></td>
                    <td>❌ Not Included</td>
                    <td>✓ Daily Sync</td>
                    <td>⚡ Real-time Automated Sync</td>
                </tr>
                <tr>
                    <td><strong>Custom Rule Engineering</strong></td>
                    <td>❌ Fixed Template</td>
                    <td>❌ Fixed Template</td>
                    <td>⚡ 100% Tailored Code Support</td>
                </tr>
                <tr>
                    <td><strong>Future Code Update Modules</strong></td>
                    <td>❌ Not Included</td>
                    <td>✓ Active During Plan</td>
                    <td>♾️ Lifetime Free Upgrades</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- FAQs SECTION ---------------- #
faq_data = {
    "1. Can I test the software before buying?": "Yes, absolutely! We provide a full-featured 7-Day Free Demo version that allows you to explore all the modules, including the Point of Sale (POS) and Khata Ledger management. / Ji bilkul! Hum Free Demo version dete hain taake aap purchase karne se pehle poora software test kar sakein.",
    "2. Is this a lifetime license or subscription?": "We offer flexible plans including Annual options or a Lifetime Access license. With Lifetime, you own it forever. There are no hidden charges and no subscription renewals. / Hum Annual plans bhi dete hain aur Lifetime Access bhi. Lifetime mein aap ek baar pay karte hain aur software aapka ho jata hai.",
    "3. What happens to my data if my PC crashes or formats?": "The software creates automated local backups on your hard drive. Additionally, we provide guidance on how to sync your database with cloud storage like Google Drive. / Hamara system automatic local backup banata hai. Hum aapko ye bhi sikhayenge ke data ko Cloud par kaise sync karna hai.",
    "4. Is technical support available after purchase?": "Your purchase includes 24/7 priority support. Whether you face a technical glitch or need help with installation, our team is available via WhatsApp. / Hum apne har client ko 24/7 priority support dete hain. Aapko kabhi bhi koi masla aaye, hum WhatsApp par hamesha aapke sath hain.",
    "5. Can I get free updates and new features?": "Yes! All our active license holders receive free updates. As we continue to develop new features based on user feedback, you will receive them at no extra cost. / Ji, jitni bhi nayi updates aur features software mein aayenge, wo aapko bilkul free milenge.",
    "6. How secure is my business data?": "Security is our core promise. All your business transactions are stored locally on your machine. This means your data never leaves your control. / Aapka data 100% secure aur private hai. Sab kuch aapke computer mein local save hota hai."
}

st.markdown("### ❓ Frequently Asked Questions")

if 'active_faq' not in st.session_state:
    st.session_state.active_faq = None

for i, (question, answer) in enumerate(faq_data.items()):
    if st.button(question, key=f"faq_{i}"):
        if st.session_state.active_faq == i:
            st.session_state.active_faq = None
        else:
            st.session_state.active_faq = i

    if st.session_state.active_faq == i:
        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)


# ---------------- REVIEW FORM SECTION ---------------- #
FORMSPREE_URL = "https://formspree.io/f/xaqkdqep"
st.markdown("### 📝 Leave a Review")

with st.form("review_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
    with col2:
        email = st.text_input("Email Address")
    
    rating = st.radio("Rate Our Service", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], horizontal=True)
    comment = st.text_area("Your Comment")
    submit = st.form_submit_button("Submit Review")

    if submit:
        if name and email and comment:
            data = {"Name": name, "Email": email, "Rating": rating, "Comment": comment}
            try:
                response = requests.post(FORMSPREE_URL, data=data)
                if response.status_code == 200:
                    st.success("Thank you! Your feedback has been sent.")
                else:
                    st.error("Something went wrong. Please try again.")
            except Exception:
                st.error("Error connecting to server.")
        else:
            st.warning("Please fill all the fields (Name, Email, and Comment).")

# ---------------- CONTACT SECTION ---------------- #
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-box">
<div style="font-size: 2.6rem; font-weight: 800; color: #f43f5e; margin-bottom: 20px;">Get In Touch</div>
<div style="font-size: 1.6rem; color: #ffffff; margin: 15px 0 20px; font-weight: 700;">📞 03476712269</div>
<div style="font-size: 1.3rem; margin-bottom: 35px; font-weight: 600; color: #cbd5e1;">📍 Pull Nehar, Daska</div>
<a class="call-btn" href="https://wa.me/923476712269" target="_blank">Chat on WhatsApp</a>
</div>
""", unsafe_allow_html=True)

# Footer Layout Elements
st.markdown("""
<div style="text-align: center; padding: 40px 0 20px 0; color: #64748b; font-size: 0.9rem; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 50px;">
    © 2026 MZ Professional Tools. All Rights Reserved. <br>
    <span style="color: #06b6d4;">Developed with ❤️ by Muhammad Zubair Matrix Engines</span>
</div>
""", unsafe_allow_html=True)