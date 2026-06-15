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
    background: linear-gradient(135deg, #030712, #0b1528, #111827);
    color: #f3f4f6;
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
    background: rgba(3, 7, 18, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    z-index: 9999;
    display: flex;
    justify-content: center;
    gap: 30px;
    padding: 15px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
}

.navbar a {
    color: #cbd5e1;
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 600;
    transition: color 0.3s ease, transform 0.3s ease;
}

.navbar a:hover {
    color: #00cfff;
    transform: translateY(-2px);
}

/* Offset for sections so navbar doesn't cover titles */
.section-anchor {
    scroll-margin-top: 100px;
}

/* Main Container */
.main-container {
    padding: 4rem 6% 2rem;
}

/* Startup Welcome Animation */
.welcome-overlay {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 800;
    color: #00cfff;
    letter-spacing: 1px;
    animation: welcomeFade 4.5s ease-in-out forwards;
    overflow: hidden;
    text-shadow: 0 0 20px rgba(0, 207, 255, 0.5);
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
    padding: 80px 5% 40px;
    max-width: 1200px;
    margin: auto;
}
.hero-text {
    text-align: left;
    flex: 1;
}
.hero-text h1 {
    font-size: 4.8rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 12px;
    line-height: 1.1;
    background: linear-gradient(to right, #ffffff, #93c5fd, #00cfff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-text p {
    font-size: 1.5rem;
    color: #00cfff;
    margin-top: 0;
    font-weight: 500;
    letter-spacing: 0.5px;
}
.hero-image-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}
.hero-image {
    width: 320px;
    height: 320px;
    border-radius: 50%;
    object-fit: cover;
    transition: transform 0.4s ease;
}
.hero-image:hover {
    transform: scale(1.05);
}

/* Section Titles */
.section-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #ff5c5c;
    margin-top: 40px;
    margin-bottom: 30px;
    text-align: center;
    position: relative;
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* Professional About Section */
.about-box {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 50px;
    border-radius: 24px;
    box-shadow: 0 10px 40px rgba(0, 207, 255, 0.04);
    margin-bottom: 60px;
}

.about-header {
    font-size: 1.8rem;
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 20px;
    text-align: center;
}

.about-text {
    color: #cbd5e1;
    font-size: 1.15rem;
    line-height: 1.8;
    text-align: center;
    max-width: 900px;
    margin: 0 auto 40px auto;
}

.about-text strong {
    color: #00cfff;
}

.stats-row {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 30px;
}

.stat-item {
    text-align: center;
}

.stat-item h4 {
    font-size: 2.5rem;
    color: #ff5c5c;
    margin: 0;
    font-weight: 800;
}

.stat-item p {
    color: #94a3b8;
    font-size: 1.1rem;
    margin: 5px 0 0 0;
    font-weight: 500;
}

/* Tech Stack Badge Containers */
.tech-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 60px;
}

.tech-badge {
    background: rgba(0, 207, 255, 0.1);
    border: 1px solid rgba(0, 207, 255, 0.3);
    color: #ffffff;
    padding: 12px 25px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    transition: all 0.3s ease;
}

.tech-badge:hover {
    background: #00cfff;
    color: #030712;
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 207, 255, 0.3);
}

/* Service Cards */
.card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 24px;
    padding: 35px 25px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    height: 100%;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
}

.card:hover {
    transform: translateY(-10px);
    border-color: rgba(0, 207, 255, 0.6);
    box-shadow: 0 20px 40px rgba(0, 207, 255, 0.15);
    background: rgba(255, 255, 255, 0.05);
}

.card-icon {
    font-size: 3.5rem;
    margin-bottom: 20px;
}

.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
}

.card-desc {
    color: #94a3b8;
    font-size: 1.02rem;
    line-height: 1.6;
    flex-grow: 1;
}

/* Interactive Dropdown Styles */
details { margin-top: 20px; text-align: left; }
details summary {
    cursor: pointer; color: #ff5c5c; font-weight: 600; font-size: 0.95rem;
    padding: 10px 14px;
    background: rgba(255, 92, 92, 0.08); border: 1px solid rgba(255, 92, 92, 0.15);
    border-radius: 12px; transition: all 0.3s ease; text-align: center;
    list-style: none;
}
details summary::-webkit-details-marker { display: none; }
details summary:hover { background: rgba(255, 92, 92, 0.18); border-color: rgba(255, 92, 92, 0.3); }
details ul { color: #cbd5e1; padding-left: 15px; margin-top: 10px; line-height: 1.7; list-style-type: none; }
details ul li { position: relative; margin-bottom: 10px; padding-left: 15px; }
details ul li::before { content: "•"; color: #00cfff; font-weight: bold; position: absolute; left: -5px; }

/* Why Choose Us Section */
.why-box {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(0, 207, 255, 0.2);
    border-radius: 24px;
    padding: 50px 40px;
    margin-top: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.why-box h3 { color: #ffffff; text-align: center; margin-bottom: 15px; font-size: 2rem; }
.why-box > p { color: #cbd5e1; text-align: center; font-size: 1.15rem; margin-bottom: 45px; max-width: 800px; margin-left: auto; margin-right: auto; }
.feature-grid { display: flex; gap: 25px; justify-content: space-between; flex-wrap: wrap; }
.feat-item {
    flex: 1; min-width: 280px;
    background: rgba(0, 0, 0, 0.25); padding: 30px; border-radius: 16px;
    border-top: 4px solid #ff5c5c; transition: transform 0.3s ease, border-color 0.3s ease;
}
.feat-item:hover { transform: translateY(-8px); border-top-color: #00cfff; background: rgba(0, 0, 0, 0.4); }
.feat-item h4 { color: #ffffff; margin-bottom: 15px; font-size: 1.3rem; display: flex; align-items: center; gap: 10px; }
.feat-item p { color: #94a3b8; font-size: 1.05rem; line-height: 1.6; }

/* Development Process Section */
.process-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 20px;
}

.process-step {
    background: rgba(255, 255, 255, 0.02);
    border: 1px dashed rgba(0, 207, 255, 0.4);
    border-radius: 16px;
    padding: 25px;
    width: 260px;
    text-align: center;
    transition: all 0.3s ease;
}

.process-step:hover {
    background: rgba(0, 207, 255, 0.05);
    border-style: solid;
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 207, 255, 0.1);
}

.process-icon { font-size: 2.5rem; margin-bottom: 15px; }
.process-title { color: #ffffff; font-size: 1.2rem; font-weight: bold; margin-bottom: 10px; }
.process-desc { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; }

/* ----------------------------------------------------
   UPGRADED & FIXES: MODERN DESIGN FOR PRICING SECTION
------------------------------------------------------- */
.pricing-container {
    display: flex;
    justify-content: center;
    gap: 25px;
    flex-wrap: wrap;
    margin-top: 40px;
    padding-bottom: 40px;
}

.pricing-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 40px 25px;
    width: 280px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.pricing-card:hover {
    transform: translateY(-12px);
    border-color: #00cfff;
    box-shadow: 0 30px 60px rgba(0, 207, 255, 0.15);
    background: rgba(30, 41, 59, 0.7);
}

/* Premium Highlight Ribbon */
.pricing-card.premium-card {
    border: 1px solid rgba(255, 92, 92, 0.4);
    box-shadow: 0 20px 40px rgba(255, 92, 92, 0.1);
}
.pricing-card.premium-card:hover {
    border-color: #ff5c5c;
    box-shadow: 0 30px 60px rgba(255, 92, 92, 0.25);
}

.plan-badge {
    position: absolute;
    top: 18px;
    right: -33px;
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white;
    padding: 4px 35px;
    font-size: 0.75rem;
    font-weight: bold;
    transform: rotate(45deg);
    letter-spacing: 0.5px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.plan-badge.green-badge { background: linear-gradient(135deg, #11998e, #38ef7d); }
.plan-badge.blue-badge { background: linear-gradient(135deg, #00cfff, #0072ff); }

.pricing-title {
    font-size: 1.4rem;
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 5px;
}
.pricing-sub {
    font-size: 0.9rem;
    color: #94a3b8;
    margin-bottom: 15px;
}
.pricing-price {
    font-size: 2.6rem;
    font-weight: 800;
    color: #ffffff;
    margin: 10px 0;
}
.pricing-price span {
    color: #00cfff;
}
.pricing-card.premium-card .pricing-price span {
    color: #ff5c5c;
}

.plan-features {
    text-align: left;
    list-style: none;
    padding: 0;
    margin: 20px 0 30px 0;
    flex-grow: 1;
}
.plan-features li {
    color: #cbd5e1;
    font-size: 0.95rem;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.plan-features li::before {
    content: "✓";
    color: #00cfff;
    font-weight: bold;
}
.pricing-card.premium-card .plan-features li::before {
    color: #ff5c5c;
}

.wa-btn {
    display: block;
    padding: 12px;
    background: linear-gradient(135deg, #00f2fe, #4facfe);
    color: #030712 !important;
    text-decoration: none;
    border-radius: 12px;
    font-weight: 700;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(79, 172, 254, 0.2);
}
.pricing-card.premium-card .wa-btn {
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white !important;
    box-shadow: 0 4px 15px rgba(221, 36, 118, 0.25);
}
.wa-btn:hover {
    transform: scale(1.03);
    filter: brightness(1.1);
}

/* Global Elements Overrides */
div.stButton > button {
    width: 100%;
    background-color: #1e293b !important;
    color: white !important;
    border: 1px solid #334155 !important;
    padding: 20px !important;
    text-align: left !important;
    font-size: 18px !important;
    font-weight: bold !important;
    border-radius: 10px !important;
    margin-bottom: 5px !important;
    transition: all 0.3s ease !important;
}

div.stButton > button:hover {
    background-color: #334155 !important;
    border-color: #00cfff !important;
}

.answer-box {
    background: #0f172a;
    padding: 20px;
    border-left: 5px solid #00cfff;
    border-right: 1px solid #334155;
    border-bottom: 1px solid #334155;
    border-radius: 0 0 10px 10px;
    color: #e2e8f0;
    margin-bottom: 15px;
    font-size: 16px;
    line-height: 1.6;
}

label { color: #ffffff !important; font-weight: 600 !important; }
div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > textarea {
    background-color: #1e293b !important;
    border: 1px solid #374151 !important;
    border-radius: 10px !important;
    transition: all 0.3s ease !important;
}
input, textarea { color: #ffffff !important; font-weight: 500 !important; }
::placeholder { color: #94a3b8 !important; }
div[data-baseweb="input"] > div:focus-within, div[data-baseweb="textarea"] > textarea:focus {
    transform: scale(1.015);
    box-shadow: 0 0 15px #00cfff !important;
    border-color: #00cfff !important;
    outline: none !important;
}

div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #ff512f, #dd2476) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 10px 30px !important;
    font-weight: bold !important;
    transition: transform 0.3s ease !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(221, 36, 118, 0.4);
}

.contact-box {
    text-align: center;
    padding: 60px 30px; margin-top: 80px;
    background: rgba(255, 255, 255, 0.02); backdrop-filter: blur(15px); border-radius: 28px;
    border: 1px solid rgba(255, 255, 255, 0.06); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 40px rgba(255, 92, 92, 0.03);
}
.call-btn {
    display: inline-block; padding: 16px 40px; font-size: 1.05rem; font-weight: 700; color: white !important;
    background: linear-gradient(135deg, #ff512f, #dd2476); border-radius: 50px; text-decoration: none;
    transition: all 0.3s; box-shadow: 0 8px 24px rgba(221, 36, 118, 0.25);
}
.call-btn:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 12px 30px rgba(221, 36, 118, 0.45); }

/* Responsive Design */
@media (max-width: 850px) {
    .navbar { gap: 15px; font-size: 0.9rem; padding: 10px 0; }
    .hero-container { flex-direction: column; text-align: center; gap: 30px; padding-top: 60px; }
    .hero-text { text-align: center; }
    .hero-text h1 { font-size: 3.5rem; }
    .hero-image { width: 250px; height: 250px; }
    .pricing-card { width: 100%; }
}
</style>

<nav class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#tech">Tech Stack</a>
    <a href="#services">Services</a>
    <a href="#ledger">Khata Ledger</a>  
    <a href="#process">Process</a>
    <a href="#pricing">Pricing</a>
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
        <p>High-Quality POS & Custom Software Solutions</p>
    </div>
    <div class="hero-image-wrapper">
        <img src="https://raw.githubusercontent.com/freefire445879-spec/mz-software-portfolio/main/1767490334321.jpg" alt="Muhammad Zubair" class="hero-image">
    </div>
</div>
""", unsafe_allow_html=True)

# About Developer Section
st.markdown('<div id="about" class="section-title section-anchor">About The Developer</div>', unsafe_allow_html=True)
st.markdown("""
<div class="about-box">
    <div class="about-header">Transforming Ideas into Digital Reality</div>
    <div class="about-text">
        <strong>Muhammad Zubair</strong> from <strong>Daska</strong> is a dedicated Software Developer specializing in building robust, scalable, and high-performance business solutions.<br><br>
        With a strong focus on modern UI/UX and seamless backend functionality, I bridge the gap between complex business logic and intuitive software. Whether it's a high-speed Retail POS, a secure Pharmacy system, or a complete custom data application, my mission is to empower your business with digital tools that drive growth, accuracy, and efficiency.
    </div>
    <div class="stats-row">
        <div class="stat-item"><h4>100%</h4><p>Client Satisfaction</p></div>
        <div class="stat-item"><h4>Custom</h4><p>Logic & Workflows</p></div>
        <div class="stat-item"><h4>24/7</h4><p>Priority Support</p></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Tech Stack Section
st.markdown('<div id="tech" class="section-title section-anchor">Technologies & Expertise</div>', unsafe_allow_html=True)
st.markdown("""
<div class="tech-container">
    <div class="tech-badge">🐍 Python</div>
    <div class="tech-badge">📊 Streamlit</div>
    <div class="tech-badge">🗄️ SQL Databases</div>
    <div class="tech-badge">💻 Custom UI/UX</div>
    <div class="tech-badge">🐙 GitHub Integration</div>
    <div class="tech-badge">⚙️ API Development</div>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown('<div id="services" class="section-title section-anchor">Services</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<div class="card-icon">🛒</div>
<div class="card-title">Retail POS</div>
<div class="card-desc">Modern Billing & Inventory management solutions designed for retail businesses.<br>
<details><summary>View Features</summary><ul><li>Automate complex discounts.</li><li>Track exact inventory levels in real time.</li><li>Prevent employee theft with tracking.</li><li>Scan barcodes quickly.</li></ul></details>
</div></div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<div class="card-icon">💊</div>
<div class="card-title">Pharmacy POS</div>
<div class="card-desc">Smart Expiry & Stock management system built specifically for pharmacies and medical stores.<br>
<details><summary>View Features</summary><ul><li>Track medicine expiry dates easily.</li><li>Manage batch numbers for compliance.</li><li>Alert staff when critical medicines run low.</li><li>Look up drug substitutes instantly.</li></ul></details>
</div></div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<div class="card-icon">⚙️</div>
<div class="card-title">Custom Solutions</div>
<div class="card-desc">Tailor-made applications developed according to your business workflow and requirements.<br>
<details><summary>View Features</summary><ul><li>Build custom tailored features.</li><li>Scale easily as your business grows.</li><li>Own software completely (no monthly fees).</li><li>Integrate with existing tools.</li></ul></details>
</div></div>""", unsafe_allow_html=True)

# Testimonials Section
st.markdown('<div id="testimonials" class="section-title section-anchor">What Our Clients Say</div>', unsafe_allow_html=True)
st.markdown("""
<div class="why-box" style="border-top: 4px solid #00cfff;">
<div style="display: flex; gap: 20px; overflow-x: auto; padding: 20px;">
    <div class="feat-item" style="min-width: 300px;">
        <p>"MZ Professional Tools ka POS system use kar raha hoon. Mera stock aur profit manage karna ab baccho ka khel hai. Highly recommended!"</p>
        <h4 style="margin-top:15px;">— Malik General Store, Daska</h4>
    </div>
    <div class="feat-item" style="min-width: 300px;">
        <p>"Pharmacy POS ne meri zindagi asaan kar di. Expiry date tracking aur medicine management behtareen hai."</p>
        <h4 style="margin-top:15px;">— City Pharmacy</h4>
    </div>
</div>
</div>""", unsafe_allow_html=True)

# Why Choose Us Section
st.markdown('<div class="section-title">Why You Need Our Software</div>', unsafe_allow_html=True)
st.markdown("""
<div class="why-box">
<h3>Take Complete Control of Your Business Performance</h3>
<p>Don't just track sales—maximize your profitability. Our premium systems provide the deep insights needed to scale your operations safely and efficiently.</p>
<div class="feature-grid">
<div class="feat-item"><h4>📈 Advanced Profit Dashboard</h4><p>Stop guessing. See your exact daily, weekly, and monthly profit margins in real-time. Identify your highest-earning products instantly so you know where to invest.</p></div>
<div class="feat-item"><h4>💰 Advanced Collection Reports</h4><p>Never lose track of outstanding balances. Get detailed, automated reports on credit, pending payments, and cash flow history to keep your finances secure.</p></div>
<div class="feat-item"><h4>🛠️ 100% Custom Software Choice</h4><p>Get a system built entirely around <i>your</i> rules. Don't force your business to fit a generic template; we tailor the logic and workflows specifically to you.</p></div>
</div>
</div>""", unsafe_allow_html=True)

# Khata Ledger Section
st.markdown('<div id="ledger" class="section-title section-anchor">Customer Ledger (Khata) System</div>', unsafe_allow_html=True)
st.markdown("""
<div class="why-box">
<h3 style="color: #00cfff;">Advanced Digital Khata & Points Management</h3>
<p>Replace manual notebooks with a secure digital ledger built directly into the POS. Track credit, reward loyal customers, and view sale histories instantly.</p>
<div class="feature-grid">
<div class="feat-item"><h4>📖 Custom Ledger Summary</h4><p>Instantly view complete records of credit (udhaar), total cash received, and remaining balances for specific customers on a unified dashboard.</p></div>
<div class="feat-item"><h4>🎁 Points Reward System</h4><p>Automatically save and calculate loyalty points on every customer purchase to encourage repeat business and easily apply future discounts.</p></div>
<div class="feat-item"><h4>📜 Complete Sale History</h4><p>Track exactly what each customer bought, the date of purchase, and the payment method used. Never lose a transaction record again.</p></div>
</div>
</div>""", unsafe_allow_html=True)

# Process Section
st.markdown('<div id="process" class="section-title section-anchor">Our Development Process</div>', unsafe_allow_html=True)
st.markdown("""
<div class="process-container">
<div class="process-step"><div class="process-icon">📝</div><div class="process-title">1. Requirement Analysis</div><div class="process-desc">Understanding your core business needs and defining the essential software logic.</div></div>
<div class="process-step"><div class="process-icon">🎨</div><div class="process-title">2. UI/UX Design</div><div class="process-desc">Crafting a modern, easy-to-use interface tailored specifically to your daily workflow.</div></div>
<div class="process-step"><div class="process-icon">💻</div><div class="process-title">3. Custom Development</div><div class="process-desc">Writing secure, clean, and robust code using the latest modern technologies.</div></div>
<div class="process-step"><div class="process-icon">🚀</div><div class="process-title">4. Deployment & Support</div><div class="process-desc">Successfully launching your system with ongoing 24/7 priority technical support.</div></div>
</div>""", unsafe_allow_html=True)


# ----------------------------------------------------
# FIXED & UPGRADED: PREMIUM COMPLIANT PRICING LAYOUT
# ----------------------------------------------------
st.markdown('<div id="pricing" class="section-title section-anchor">Our Sales Plans</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pricing-container">
    <div class="pricing-card">
        <div>
            <div class="plan-badge green-badge">Demo</div>
            <div class="pricing-title">Free Trial</div>
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
<div style="font-size: 2.6rem; font-weight: 800; color: #ff5c5c; margin-bottom: 20px;">Get In Touch</div>
<div style="font-size: 1.6rem; color: #ffffff; margin: 15px 0 20px; font-weight: 700;">📞 03476712269</div>
<div style="font-size: 1.3rem; margin-bottom: 35px; font-weight: 600; color: #cbd5e1;">📍 Pull Nehar, Daska</div>
<a class="call-btn" href="https://wa.me/923476712269" target="_blank">Chat on WhatsApp</a>
</div>
""", unsafe_allow_html=True)

# Footer Layout Elements
st.markdown("""
<div style="text-align: center; padding: 40px 0 20px 0; color: #64748b; font-size: 0.9rem; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 50px;">
    © 2026 MZ Professional Tools. All Rights Reserved. <br>
    <span style="color: #00cfff;">Developed with ❤️ by Muhammad Zubair (Daska)</span>
</div>
""", unsafe_allow_html=True)

# Close Main Container Wrapper Tag
st.markdown("</div>", unsafe_allow_html=True)