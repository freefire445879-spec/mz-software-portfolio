# portfolio.py
# Professional Business Portfolio Website using Streamlit

import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="MZ Professional Tools",
    page_icon="💼",
    layout="wide",
)

# ---------------- CUSTOM CSS ---------------- #
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

/* Global Typography Tweaks */
html, body, [class*="css"] {
    color: #f3f4f6;
}

/* Main Container */
.main-container {
    padding: 4rem 6% 2rem; /* Added top padding for navbar */
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
.hero {
    text-align: center;
    padding: 60px 20px 40px;
}

.hero h1 {
    font-size: 4.5rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 12px;
    letter-spacing: -0.5px;
    background: linear-gradient(to right, #ffffff, #93c5fd, #00cfff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.4rem;
    color: #00cfff;
    margin-top: 0;
    font-weight: 500;
    letter-spacing: 0.5px;
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

/* About Section */
.about-box {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 40px;
    border-radius: 24px;
    line-height: 1.8;
    font-size: 1.15rem;
    box-shadow: 0 10px 40px rgba(0, 207, 255, 0.04);
    margin-bottom: 60px;
    color: #cbd5e1;
    text-align: center;
}

.about-box strong {
    color: #ffffff;
    font-size: 1.25rem;
}

/* Service Cards */
.card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
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
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
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

/* Pricing Section (New) */
.pricing-container {
    display: flex;
    justify-content: center;
    gap: 40px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.pricing-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(0, 207, 255, 0.2);
    border-radius: 24px;
    padding: 50px 30px;
    width: 320px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}

.pricing-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 207, 255, 0.2);
    border-color: #00cfff;
}

.pricing-card.premium {
    border-color: #ff5c5c;
    background: rgba(255, 92, 92, 0.05);
}

.pricing-card.premium:hover {
    box-shadow: 0 15px 40px rgba(255, 92, 92, 0.2);
}

.badge {
    position: absolute;
    top: 15px;
    right: -35px;
    background: #ff5c5c;
    color: white;
    padding: 5px 40px;
    font-size: 0.8rem;
    font-weight: bold;
    transform: rotate(45deg);
}

.pricing-title {
    font-size: 1.5rem;
    color: #ffffff;
    font-weight: 700;
}

.pricing-price {
    font-size: 3rem;
    font-weight: 800;
    color: #00cfff;
    margin: 20px 0;
}

.pricing-card.premium .pricing-price {
    color: #ff5c5c;
}

.pricing-duration {
    font-size: 1rem;
    color: #94a3b8;
    font-weight: normal;
}

/* Dropdown Elements */
details { margin-top: 20px; text-align: left; }
details summary {
    cursor: pointer; color: #ff5c5c; font-weight: 600; font-size: 0.95rem;
    padding: 10px 14px; background: rgba(255, 92, 92, 0.08); border: 1px solid rgba(255, 92, 92, 0.15);
    border-radius: 12px; transition: all 0.3s ease; list-style: none; text-align: center;
}
details summary::-webkit-details-marker { display: none; }
details summary:hover { background: rgba(255, 92, 92, 0.18); border-color: rgba(255, 92, 92, 0.3); }
details ul { color: #cbd5e1; padding-left: 15px; margin-top: 10px; line-height: 1.7; list-style-type: none; }
details ul li { position: relative; margin-bottom: 10px; padding-left: 15px; }
details ul li::before { content: "•"; color: #00cfff; font-weight: bold; position: absolute; left: -5px; }

/* Contact Section */
.contact-box {
    text-align: center;
    padding: 60px 30px;
    margin-top: 80px;
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(15px);
    border-radius: 28px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 40px rgba(255, 92, 92, 0.03);
}

.call-btn {
    display: inline-block;
    padding: 16px 40px;
    font-size: 1.05rem;
    font-weight: 700;
    color: white !important;
    background: linear-gradient(135deg, #ff512f, #dd2476);
    border-radius: 50px;
    text-decoration: none;
    transition: all 0.3s;
    box-shadow: 0 8px 24px rgba(221, 36, 118, 0.25);
}

.call-btn:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 12px 30px rgba(221, 36, 118, 0.45); }

/* Responsive Design */
@media (max-width: 768px) {
    .navbar { gap: 15px; font-size: 0.9rem; padding: 10px 0; }
    .hero h1 { font-size: 2.8rem; }
}

</style>

<nav class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#pricing">Pricing</a>
    <a href="#contact">Contact</a>
</nav>

""", unsafe_allow_html=True)

# ---------------- MAIN CONTAINER ---------------- #
st.markdown('<div id="home" class="main-container section-anchor">', unsafe_allow_html=True)

# ---------------- WELCOME ANIMATION ---------------- #
st.markdown("""
<div class="welcome-overlay">
✨ Welcome to Muhammad Zubair Officials ✨
</div>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("""
<div class="hero">
<h1>MZ Professional Tools</h1>
<p>High-Quality POS & Custom Software Solutions</p>
</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT SECTION ---------------- #
st.markdown('<div id="about" class="section-title section-anchor">About</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-box">
<strong>Muhammad Zubair</strong> from <strong>Daska</strong> specializes in building
robust and professional software solutions for modern businesses.
<br><br>
From advanced Point of Sale systems to tailor-made business applications,
the focus is always on performance, reliability, and user-friendly design.
High-quality digital tools are crafted to help businesses operate smarter,
faster, and more efficiently.
</div>
""", unsafe_allow_html=True)

# ---------------- SERVICES SECTION ---------------- #
st.markdown('<div id="services" class="section-title section-anchor">Services</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">
<div class="card-icon">🛒</div>
<div class="card-title">Retail POS</div>
<div class="card-desc">
Modern Billing & Inventory management solutions designed
for retail businesses.
<br>
<details>
<summary>View Features</summary>
<ul>
<li>Automate complex discounts.</li>
<li>Track exact inventory levels in real time.</li>
<li>Prevent employee theft with tracking.</li>
<li>Scan barcodes quickly.</li>
</ul>
</details>
</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<div class="card-icon">💊</div>
<div class="card-title">Pharmacy POS</div>
<div class="card-desc">
Smart Expiry & Stock management system built specifically
for pharmacies and medical stores.
<br>
<details>
<summary>View Features</summary>
<ul>
<li>Track medicine expiry dates easily.</li>
<li>Manage batch numbers for compliance.</li>
<li>Alert staff when critical medicines run low.</li>
<li>Look up drug substitutes instantly.</li>
</ul>
</details>
</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">
<div class="card-icon">⚙️</div>
<div class="card-title">Custom Solutions</div>
<div class="card-desc">
Tailor-made applications developed according to your
business workflow and requirements.
<br>
<details>
<summary>View Features</summary>
<ul>
<li>Build custom tailored features.</li>
<li>Scale easily as your business grows.</li>
<li>Own software completely (no monthly fees).</li>
<li>Integrate with existing tools.</li>
</ul>
</details>
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SALES PLAN / PRICING SECTION ---------------- #
st.markdown('<div id="pricing" class="section-title section-anchor">Our Sales Plan</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pricing-container">
    
    <div class="pricing-card">
        <div class="pricing-title">Yearly License</div>
        <div class="pricing-price">Rs 2,000<span class="pricing-duration"> / year</span></div>
        <p style="color: #cbd5e1; margin-bottom: 20px;">Perfect for businesses wanting to test out our premium features at a low cost.</p>
        <ul style="text-align: left; color: #94a3b8; list-style: none; padding: 0;">
            <li>✔️ Full POS Functionality</li>
            <li>✔️ Standard Updates</li>
            <li>✔️ Email Support</li>
        </ul>
    </div>

    <div class="pricing-card premium">
        <div class="badge">BEST VALUE</div>
        <div class="pricing-title">Lifetime Access</div>
        <div class="pricing-price">Rs 20,000<span class="pricing-duration"> / once</span></div>
        <p style="color: #cbd5e1; margin-bottom: 20px;">Continuous access forever with zero renewal fees. Buy it once, own it for life.</p>
        <ul style="text-align: left; color: #94a3b8; list-style: none; padding: 0;">
            <li>✔️ Lifetime POS Access</li>
            <li>✔️ Priority WhatsApp Support</li>
            <li>✔️ Free Future Updates</li>
            <li>✔️ No Monthly/Yearly Fees</li>
        </ul>
    </div>

</div>
""", unsafe_allow_html=True)


# ---------------- CONTACT SECTION ---------------- #
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">
<div style="font-size: 2.6rem; font-weight: 800; color: #ff5c5c; margin-bottom: 20px;">Get In Touch</div>
<div style="font-size: 1.6rem; color: #ffffff; margin: 15px 0 20px; font-weight: 700;">
📞 03476712269
</div>
<div style="font-size: 1.3rem; margin-bottom: 35px; font-weight: 600; color: #cbd5e1;">
📍 Pull Nehar, Daska
</div>
<a class="call-btn" href="https://wa.me/923476712269" target="_blank">
Chat on WhatsApp
</a>
</div>
""", unsafe_allow_html=True)

# Close Main Container
st.markdown("</div>", unsafe_allow_html=True)