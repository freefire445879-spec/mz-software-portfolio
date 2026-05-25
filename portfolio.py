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

/* New Section: Tech Stack */
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
    padding: 10px 14px; background: rgba(255, 92, 92, 0.08); border: 1px solid rgba(255, 92, 92, 0.15);
    border-radius: 12px; transition: all 0.3s ease; text-align: center; list-style: none;
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
    flex: 1; min-width: 280px; background: rgba(0, 0, 0, 0.25); padding: 30px; border-radius: 16px;
    border-top: 4px solid #ff5c5c; transition: transform 0.3s ease, border-color 0.3s ease;
}
.feat-item:hover { transform: translateY(-8px); border-top-color: #00cfff; background: rgba(0, 0, 0, 0.4); }
.feat-item h4 { color: #ffffff; margin-bottom: 15px; font-size: 1.3rem; display: flex; align-items: center; gap: 10px; }
.feat-item p { color: #94a3b8; font-size: 1.05rem; line-height: 1.6; }

/* Development Process Section (NEW) */
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

.process-icon {
    font-size: 2.5rem;
    margin-bottom: 15px;
}

.process-title {
    color: #ffffff;
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.process-desc {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.5;
}

/* Pricing Section */
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
    color: white;
    padding: 5px 40px;
    font-size: 0.8rem;
    font-weight: bold;
    transform: rotate(45deg);
}

/* Badge Color Modifiers */
.badge.orange { background: #ff9800; }
.badge.green { background: #2ecc71; }
.badge.red { background: #ff5c5c; }

.pricing-title { font-size: 1.5rem; color: #ffffff; font-weight: 700; }
.pricing-price { font-size: 3rem; font-weight: 800; color: #00cfff; margin: 20px 0; }
.pricing-card.premium .pricing-price { color: #ff5c5c; }
.pricing-duration { font-size: 1rem; color: #94a3b8; font-weight: normal; }

/* Contact Section */
.contact-box {
    text-align: center; padding: 60px 30px; margin-top: 80px;
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
@media (max-width: 768px) {
    .navbar { gap: 15px; font-size: 0.9rem; padding: 10px 0; }
    .hero h1 { font-size: 2.8rem; }
    .pricing-card { width: 100%; }
}

</style>

<nav class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#tech">Tech Stack</a>
    <a href="#services">Services</a>
    <a href="#ledger">Khata Ledger</a>  <a href="#process">Process</a>
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
# ---------------- CUSTOM CSS FOR HERO SECTION ---------------- #
st.markdown("""
<style>
/* Professional Hero Section */
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
    border: none; /* Border khatam kar diya */
    box-shadow: none; /* Shadow khatam kar di */
    transition: transform 0.4s ease;
}
.hero-image:hover {
    transform: scale(1.05);
}

/* Mobile Responsiveness */
@media (max-width: 850px) {
    .hero-container {
        flex-direction: column;
        text-align: center;
        gap: 30px;
        padding-top: 60px;
    }
    .hero-text {
        text-align: center;
    }
    .hero-text h1 {
        font-size: 3.5rem;
    }
    .hero-image {
        width: 250px;
        height: 250px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
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

# ---------------- ABOUT SECTION (UPGRADED) ---------------- #
st.markdown('<div id="about" class="section-title section-anchor">About The Developer</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-box">
    <div class="about-header">Transforming Ideas into Digital Reality</div>
    <div class="about-text">
        <strong>Muhammad Zubair</strong> from <strong>Daska</strong> is a dedicated Software Developer specializing in building robust, scalable, and high-performance business solutions. 
        <br><br>
        With a strong focus on modern UI/UX and seamless backend functionality, I bridge the gap between complex business logic and intuitive software. Whether it's a high-speed Retail POS, a secure Pharmacy system, or a complete custom data application, my mission is to empower your business with digital tools that drive growth, accuracy, and efficiency.
    </div>
    <div class="stats-row">
        <div class="stat-item">
            <h4>100%</h4>
            <p>Client Satisfaction</p>
        </div>
        <div class="stat-item">
            <h4>Custom</h4>
            <p>Logic & Workflows</p>
        </div>
        <div class="stat-item">
            <h4>24/7</h4>
            <p>Priority Support</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- NEW SECTION: TECH STACK ---------------- #
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

# ---------------- TRUST ---------------- #
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
</div>
""", unsafe_allow_html=True)
# ---------------- WHY CHOOSE US SECTION ---------------- #
st.markdown('<div class="section-title">Why You Need Our Software</div>', unsafe_allow_html=True)

st.markdown("""
<div class="why-box">
<h3>Take Complete Control of Your Business Performance</h3>
<p>Don't just track sales—maximize your profitability. Our premium systems provide the deep insights needed to scale your operations safely and efficiently.</p>
<div class="feature-grid">
<div class="feat-item">
<h4>📈 Advanced Profit Dashboard</h4>
<p>Stop guessing. See your exact daily, weekly, and monthly profit margins in real-time. Identify your highest-earning products instantly so you know where to invest.</p>
</div>
<div class="feat-item">
<h4>💰 Advanced Collection Reports</h4>
<p>Never lose track of outstanding balances. Get detailed, automated reports on credit, pending payments, and cash flow history to keep your finances secure.</p>
</div>
<div class="feat-item">
<h4>🛠️ 100% Custom Software Choice</h4>
<p>Get a system built entirely around <i>your</i> rules. Don't force your business to fit a generic template; we tailor the logic and workflows specifically to you.</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- CUSTOMER LEDGER (KHATA) SECTION ---------------- #
st.markdown('<div id="ledger" class="section-title section-anchor">Customer Ledger (Khata) System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="why-box">
<h3 style="color: #00cfff;">Advanced Digital Khata & Points Management</h3>
<p>Replace manual notebooks with a secure digital ledger built directly into the POS. Track credit, reward loyal customers, and view sale histories instantly.</p>
<div class="feature-grid">
<div class="feat-item">
<h4>📖 Custom Ledger Summary</h4>
<p>Instantly view complete records of credit (udhaar), total cash received, and remaining balances for specific customers on a unified dashboard.</p>
</div>
<div class="feat-item">
<h4>🎁 Points Reward System</h4>
<p>Automatically save and calculate loyalty points on every customer purchase to encourage repeat business and easily apply future discounts.</p>
</div>
<div class="feat-item">
<h4>📜 Complete Sale History</h4>
<p>Track exactly what each customer bought, the date of purchase, and the payment method used. Never lose a transaction record again.</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SOFTWARE DEVELOPMENT PROCESS (NEW SECTION) ---------------- #
st.markdown('<div id="process" class="section-title section-anchor">Our Development Process</div>', unsafe_allow_html=True)

st.markdown("""
<div class="process-container">
<div class="process-step">
<div class="process-icon">📝</div>
<div class="process-title">1. Requirement Analysis</div>
<div class="process-desc">Understanding your core business needs and defining the essential software logic.</div>
</div>
<div class="process-step">
<div class="process-icon">🎨</div>
<div class="process-title">2. UI/UX Design</div>
<div class="process-desc">Crafting a modern, easy-to-use interface tailored specifically to your daily workflow.</div>
</div>
<div class="process-step">
<div class="process-icon">💻</div>
<div class="process-title">3. Custom Development</div>
<div class="process-desc">Writing secure, clean, and robust code using the latest modern technologies.</div>
</div>
<div class="process-step">
<div class="process-icon">🚀</div>
<div class="process-title">4. Deployment & Support</div>
<div class="process-desc">Successfully launching your system with ongoing 24/7 priority technical support.</div>
</div>
</div>
""", unsafe_allow_html=True)


# ---------------- SALES PLAN / PRICING SECTION (UPDATED) ---------------- #
# ----------------================---------------------------------- #
#                  👑 UPDATED PREMIUM PRICING SECTION                 #
# ----------------================---------------------------------- #

st.markdown('<div id="pricing" class="section-title section-anchor">Our Sales Plan</div>', unsafe_allow_html=True)

# CSS for interactive hover effect and premium buttons
st.markdown("""
<style>
/* Base container styling */
.pricing-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 25px;
    padding: 20px 0;
}

/* Card basic design and smooth transition */
.pricing-card {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 30px;
    width: 280px;
    text-align: center;
    position: relative;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Premium Card specific extra borders */
.pricing-card.premium {
    border: 1px solid #ff5c5c;
    background: linear-gradient(180deg, rgba(255,92,92,0.05), rgba(15,23,42,0.8));
}

/* 🔥 CURSOR HOVER EFFECT - SIZE BARHA HO JAYEGA */
.pricing-card:hover {
    transform: translateY(-12px) scale(1.05); /* Size increase smoothly */
    border-color: #00cfff;
    box-shadow: 0 20px 40px rgba(0, 207, 255, 0.15);
    background: rgba(15, 23, 42, 0.85);
}

.pricing-card.premium:hover {
    border-color: #ff5c5c;
    box-shadow: 0 20px 40px rgba(255, 92, 92, 0.2);
}

/* List Item styling for crisp look */
.pricing-features-list {
    text-align: left; 
    color: #cbd5e1; 
    list-style: none; 
    padding: 0;
    margin: 20px 0 30px 0;
}

.pricing-features-list li {
    margin-bottom: 12px;
    font-size: 0.95rem;
    line-height: 1.4;
}

/* Ultra premium call to action buttons */
.plan-btn {
    display: block;
    padding: 12px 24px;
    background: linear-gradient(90deg, #1e293b, #0f172a);
    color: #00cfff !important;
    text-decoration: none !important;
    font-weight: 700;
    border-radius: 8px;
    border: 1px solid rgba(0, 207, 255, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    margin-top: auto;
}

.plan-btn:hover {
    background: linear-gradient(90deg, #00cfff, #008ecc);
    color: #ffffff !important;
    box-shadow: 0 5px 15px rgba(0, 207, 255, 0.4);
    transform: translateY(-2px);
}

.premium-btn {
    display: block;
    padding: 12px 24px;
    background: linear-gradient(90deg, #ff5c5c, #d93838);
    color: #ffffff !important;
    text-decoration: none !important;
    font-weight: 700;
    border-radius: 8px;
    transition: all 0.3s ease;
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    margin-top: auto;
}

.premium-btn:hover {
    background: linear-gradient(90deg, #ff7a7a, #ff5c5c);
    box-shadow: 0 5px 15px rgba(255, 92, 92, 0.4);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pricing-container">

    <div class="pricing-card">
        <div>
            <div class="pricing-title">Free Trial</div>
            <div class="pricing-price">Rs 0</div>
            <p style="color: #cbd5e1; margin-bottom: 20px;">Test out the core features of our POS system before buying.</p>
            <ul class="pricing-features-list">
                <li>⏱️ 7 Days Full Access</li>
                <li>✔️ Basic Invoice Generation</li>
                <li>✔️ Retail Billing System</li>
                <li>⚠️ Limited Bills & Entries</li>
                <li>❌ No Custom Receipt Logo</li>
                <li>❌ No Live Cloud Database</li>
            </ul>
        </div>
        <a class="plan-btn" href="https://wa.me/923476712269?text=Hi%20Zubair,%20mujhe%20POS%20Software%20ka%20Free%20Trial%20setup%20chahiye." target="_blank">Get Trial</a>
    </div>

    <div class="pricing-card">
        <div>
            <div class="badge orange">GOOD VALUE</div>
            <div class="pricing-title">Yearly License</div>
            <div class="pricing-price">Rs 2,000<span class="pricing-duration"> / year</span></div>
            <p style="color: #cbd5e1; margin-bottom: 20px;">Perfect for businesses wanting to test out our premium features at a low cost.</p>
            <ul class="pricing-features-list">
                <li>✔️ 100% Full POS Functionality</li>
                <li>✔️ Custom Business Logo Receipts</li>
                <li>✔️ Unlimited Invoices & Stock Entries</li>
                <li>✔️ Customer Khata Ledger Setup</li>
                <li>✔️ Standard Software Updates</li>
                <li>✔️ Secure Local SQLite Database</li>
            </ul>
        </div>
        <a class="plan-btn" href="https://wa.me/923476712269?text=Hi%20Zubair,%20main%20POS%20Software%20ka%20Yearly%20License%20(Rs%202000)%20buy%20krna%20chahta%20hoon." target="_blank">Buy Yearly</a>
    </div>

    <div class="pricing-card">
        <div>
            <div class="badge green">BETTER VALUE</div>
            <div class="pricing-title">2-Year License</div>
            <div class="pricing-price">Rs 3,500<span class="pricing-duration"> / 2 years</span></div>
            <p style="color: #cbd5e1; margin-bottom: 20px;">Save more with a multi-year plan for uninterrupted business operations.</p>
            <ul class="pricing-features-list">
                <li>✔️ Everything in Yearly License</li>
                <li>🔥 Save Rs 500 Extra Discount</li>
                <li>✔️ No Monthly/Hidden Charges</li>
                <li>✔️ Advanced Sales & Profit Reports</li>
                <li>✔️ Offline-First Zero Lag Syncing</li>
                <li>✔️ Priority Remote Support (AnyDesk)</li>
            </ul>
        </div>
        <a class="plan-btn" href="https://wa.me/923476712269?text=Hi%20Zubair,%20main%20POS%20Software%20ka%202-Year%20License%20(Rs%203500)%20buy%20krna%20chahta%20hoon." target="_blank">Buy 2-Years</a>
    </div>

    <div class="pricing-card premium">
        <div>
            <div class="badge red">BEST VALUE</div>
            <div class="pricing-title">Lifetime Access</div>
            <div class="pricing-price">Rs 20,000<span class="pricing-duration"> / once</span></div>
            <p style="color: #cbd5e1; margin-bottom: 20px;">Continuous access forever with zero renewal fees. Buy it once, own it for life.</p>
            <ul class="pricing-features-list">
                <li>💎 Lifetime Software Access Forever</li>
                <li>☁️ Live Firebase Cloud Auto-Sync</li>
                <li>🔄 Automatic Offline-First Database</li>
                <li>✔️ Complete Advanced Inventory Alert</li>
                <li>✔️ 100% Free Future Major Updates</li>
                <li>🚀 24/7 Priority WhatsApp Support</li>
            </ul>
        </div>
        <a class="premium-btn" href="https://wa.me/923476712269?text=Hi%20Zubair,%20main%20POS%20Software%20ka%20Lifetime%20Access%20Plan%20(Rs%2020000)%20buy%20krna%20chahta%20hoon." target="_blank">Buy Lifetime</a>
    </div>

</div>
""", unsafe_allow_html=True)


# ----------------================---------------------------------- #
#                  📬 REDESIGNED CONTACT DUAL SECTION                 #
# ----------------================---------------------------------- #

st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)

st.markdown("""
<style>
.contact-container-box {
    background: linear-gradient(145deg, #0f172a, #1e293b);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    max-width: 650px;
    margin: 40px auto;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
}
.contact-btn-wrapper {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 30px;
}
.dual-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px 28px;
    font-size: 1rem;
    font-weight: 700;
    text-decoration: none !important;
    border-radius: 10px;
    transition: all 0.3s ease;
}
.dual-btn.wa {
    background: #25d366;
    color: #ffffff !important;
}
.dual-btn.wa:hover {
    background: #20ba5a;
    box-shadow: 0 8px 20px rgba(37, 211, 102, 0.4);
    transform: translateY(-3px);
}
.dual-btn.mail {
    background: #ea4335;
    color: #ffffff !important;
}
.dual-btn.mail:hover {
    background: #d3382c;
    box-shadow: 0 8px 20px rgba(234, 67, 53, 0.4);
    transform: translateY(-3px);
}
</style>

<div class="contact-container-box">
    <div style="font-size: 2.6rem; font-weight: 800; color: #ff5c5c; margin-bottom: 10px;">Get In Touch</div>
    <p style="color: #94a3b8; font-size: 1.1rem; margin-bottom: 25px;">Choose your preferred method to contact us. Both links have pre-filled custom messages ready for you!</p>
    
    <div class="contact-btn-wrapper">
        <a class="dual-btn wa" href="https://wa.me/923476712269?text=Hi%20Zubair,%20main%20aapki%20website%20se%20aya%20hoon%20aur%20mujhe%20aapke%20POS%20Software/Tools%20ke%20baare%20mein%20details%20chahiyen." target="_blank">
            💬 Chat via WhatsApp
        </a>
        
        <a class="dual-btn mail" href="mailto:freefire445879@gmail.com?subject=Inquiry%20Regarding%20MZ%20Professional%20POS%20Software&body=Hi%20Zubair,%0A%0AI%20visited%20your%20portfolio%20website%20and%20I%20am%20interested%20in%20your%20POS%20Software%20solutions.%20Please%20provide%20more%20information%20regarding%20the%20pricing%20plans%20and%20setup%20process.%0A%0AThanks!">
            ✉️ Send an Email
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
# ---------------- FAQs SECTION ---------------- #
import streamlit as st

# --- MODERN CSS FOR FAQ ACCORDION ---
st.markdown("""
<style>
    /* FAQ Button Styling - Makes it look like a Question Header */
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

    /* Answer box styling */
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
</style>
""", unsafe_allow_html=True)

# --- FAQ DATA ---
faq_data = {
    "1. Can I test the software before buying?": "Yes, absolutely! We understand that trust is built through experience. We provide a full-featured Free Demo/Trial version that allows you to explore all the modules, including the Point of Sale (POS) and Khata Ledger management. You can test it with your real-world scenarios to ensure it meets your business requirements before making any financial commitment. / Ji bilkul! Hum Free Demo version dete hain taake aap purchase karne se pehle poora software test kar sakein. Aap POS aur Khata Ledger ke tamam features khud chala kar dekh sakte hain taake aapko tasalli ho jaye.",
    "2. Is this a lifetime license or subscription?": "This is a Lifetime Access license. Unlike other software providers who charge recurring monthly or annual fees, our model is one-time payment based. Once you purchase the software, you own it forever. There are no hidden charges, no subscription renewals, and no 'per-user' extra costs. / Ye Lifetime Access hai. Hum koi monthly ya yearly fees nahi lete. Aap ek baar pay karte hain aur software aapka ho jata hai. Isme koi hidden charges ya monthly subscription ka chakkar nahi hai.",
    "3. What happens to my data if my PC crashes or formats?": "We have designed the system with data security as the top priority. The software creates automated local backups on your hard drive. Additionally, we provide guidance on how to sync your database with cloud storage (like Google Drive or OneDrive). Even if your PC crashes or is formatted, your business records can be restored in minutes using your backup file. / Hamara system automatic local backup banata hai. Hum aapko ye bhi sikhayenge ke data ko Cloud (Google Drive) par kaise sync karna hai. Agar PC kharab ya format bhi ho jaye, to aapka data sirf chand minute mein restore ho jayega.",
    "4. Is technical support available after purchase?": "Your purchase includes 24/7 priority support. We believe in building long-term relationships, not just selling products. Whether you face a technical glitch, need help with installation, or have questions about using the software, our team is available via WhatsApp, Phone, and Email to assist you immediately. / Hum apne har client ko 24/7 priority support dete hain. Aapko kabhi bhi koi masla aaye, ya installation mein madad chahiye ho, hum WhatsApp aur Email par hamesha aapke sath hain.",
    "5. Can I get free updates and new features?": "Yes! All our clients receive free lifetime updates. As we continue to develop new features, modules, or improve security based on user feedback, you will receive these updates at no extra cost. We believe in constantly improving our software to help your business grow. / Ji, jitni bhi nayi updates aur features software mein aayenge, wo aapko bilkul free milenge. Hum apne software ko hamesha behtar banate rehte hain taake aapka business modernize ho sake.",
    "6. How secure is my business data?": "Security is our core promise. All your business transactions, customer credit history, and ledger data are stored locally on your machine. This means your data never leaves your control and is not uploaded to any third-party server without your permission. It is 100% private and protected. / Aapka data 100% secure aur private hai. Sab kuch aapke computer mein local save hota hai, kisi third-party server par nahi. Isliye aapka data aapke control mein hai aur kisi aur ki access nahi hai."
}

# --- LOGIC FOR ACCORDION ---
st.markdown("### ❓ Frequently Asked Questions")

# Initialize session state to track which question is open
if 'active_faq' not in st.session_state:
    st.session_state.active_faq = None

# Loop to create buttons
for i, (question, answer) in enumerate(faq_data.items()):
    # Button as a Question Header
    if st.button(question, key=f"faq_{i}"):
        # Toggle: If clicked again, close it; otherwise, open it
        if st.session_state.active_faq == i:
            st.session_state.active_faq = None
        else:
            st.session_state.active_faq = i

    # Show Answer if this is the active one
    if st.session_state.active_faq == i:
        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
import streamlit as st
import requests

# --- CUSTOM CSS FOR FORM STYLING ---
st.markdown("""
<style>
    /* Labels ko white karna */
    label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Input boxes aur Textarea ki styling (background aur color) */
    div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > textarea {
        background-color: #1e293b !important;
        border: 1px solid #374151 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }

    /* Typed text ka color bright white karna */
    input, textarea {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Placeholder text ka color halka rakhna taake focus ho */
    ::placeholder {
        color: #94a3b8 !important;
    }

    /* Focus effect: Box bara hoga aur shadow aayegi */
    div[data-baseweb="input"] > div:focus-within, div[data-baseweb="textarea"] > textarea:focus {
        transform: scale(1.015); /* Size bara karne ke liye */
        box-shadow: 0 0 15px #00cfff !important;
        border-color: #00cfff !important;
        outline: none !important;
    }

    /* Submit Button styling */
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #ff512f, #dd2476) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        font-weight: bold !important;
        transition: transform 0.3s ease !important;
    }
    
    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(221, 36, 118, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- FORM SECTION ---
FORMSPREE_URL = "https://formspree.io/f/xaqkdqep"

st.markdown("### 📝 Leave a Review")

with st.form("review_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
    with col2:
        email = st.text_input("Email Address")
    
    rating = st.radio(
        "Rate Our Service", 
        ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], 
        horizontal=True
    )
    
    comment = st.text_area("Your Comment")
    
    submit = st.form_submit_button("Submit Review")

    if submit:
        if name and email and comment:
            data = {
                "Name": name,
                "Email": email,
                "Rating": rating,
                "Comment": comment
            }
            
            try:
                response = requests.post(FORMSPREE_URL, data=data)
                if response.status_code == 200:
                    st.success("Thank you! Your feedback has been sent.")
                else:
                    st.error("Something went wrong. Please try again.")
            except Exception as e:
                st.error("Error connecting to server.")
        else:
            st.warning("Please fill all the fields (Name, Email, and Comment).")
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
st.markdown("""
<div style="text-align: center; padding: 40px 0 20px 0; color: #64748b; font-size: 0.9rem; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 50px;">
    © 2026 MZ Professional Tools. All Rights Reserved. <br>
    <span style="color: #00cfff;">Developed with ❤️ by Muhammad Zubair (Daska)</span>
</div>
""", unsafe_allow_html=True)

# Close Main Container
st.markdown("</div>", unsafe_allow_html=True)