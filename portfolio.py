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

/* Global Typography Tweaks */
html, body, [class*="css"] {
    color: #f3f4f6;
}

/* Main Container */
.main-container {
    padding: 2rem 6%;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 100px 20px 60px;
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
}

.about-box strong {
    color: #ffffff;
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

/* Custom Interactive Dropdown Styles */
details {
    margin-top: 20px;
    text-align: left;
}

details summary {
    cursor: pointer;
    color: #ff5c5c;
    font-weight: 600;
    font-size: 0.95rem;
    outline: none;
    padding: 10px 14px;
    background: rgba(255, 92, 92, 0.08);
    border: 1px solid rgba(255, 92, 92, 0.15);
    border-radius: 12px;
    transition: all 0.3s ease;
    list-style: none;
    text-align: center;
}

details summary::-webkit-details-marker {
    display: none;
}

details summary:hover {
    background: rgba(255, 92, 92, 0.18);
    border-color: rgba(255, 92, 92, 0.3);
    box-shadow: 0 4px 12px rgba(255, 92, 92, 0.1);
}

details[open] summary {
    background: rgba(255, 92, 92, 0.2);
    margin-bottom: 15px;
}

details ul {
    text-align: left;
    font-size: 0.92rem;
    color: #cbd5e1;
    padding-left: 15px;
    margin-top: 10px;
    line-height: 1.7;
    list-style-type: none;
}

details ul li {
    position: relative;
    margin-bottom: 10px;
    padding-left: 15px;
}

details ul li::before {
    content: "•";
    color: #00cfff;
    font-weight: bold;
    font-size: 1.2rem;
    position: absolute;
    left: -5px;
    top: -2px;
}

/* Contact Section */
.contact-box {
    text-align: center;
    padding: 60px 30px;
    margin-top: 80px;
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-radius: 28px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 40px rgba(255, 92, 92, 0.03);
}

.contact-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #ff5c5c;
    letter-spacing: -0.5px;
    margin-bottom: 20px;
}

.phone {
    font-size: 1.6rem;
    color: #ffffff;
    margin: 15px 0 20px;
    font-weight: 700;
}

.phone a {
    transition: color 0.3s ease;
}

.phone a:hover {
    color: #ff5c5c !important;
}

.location-link {
    font-size: 1.3rem; 
    margin-bottom: 35px; 
    font-weight: 600; 
    color: #cbd5e1;
}

.location-link a {
    transition: color 0.3s ease;
}

.location-link a:hover {
    color: #00cfff !important;
}

/* Call/Action Button */
.call-btn {
    display: inline-block;
    padding: 16px 40px;
    font-size: 1.05rem;
    font-weight: 700;
    color: white !important;
    background: linear-gradient(135deg, #ff512f, #dd2476);
    border-radius: 50px;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 8px 24px rgba(221, 36, 118, 0.25);
}

.call-btn:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 12px 30px rgba(221, 36, 118, 0.45);
}

/* Responsive Design Overrides */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.8rem;
    }
    .hero p {
        font-size: 1.1rem;
    }
    .main-container {
        padding: 1rem 3%;
    }
    .card {
        margin-bottom: 20px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTAINER ---------------- #
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("""
<div class="hero">
    <h1>MZ Professional Tools</h1>
    <p>High-Quality POS & Custom Software Solutions</p>
</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT SECTION ---------------- #
st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section-title">Services</div>', unsafe_allow_html=True)

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
                    <li>Automate complex discounts without manual cashier math.</li>
                    <li>Reward repeat buyers to keep them coming back.</li>
                    <li>Track exact inventory levels in real time effortlessly.</li>
                    <li>Get automatic alerts before popular items sell out.</li>
                    <li>Prevent employee theft with exact item tracking.</li>
                    <li>Scan barcodes quickly to shorten busy checkout lines.</li>
                    <li>Eliminate calculation mistakes at the cash register.</li>
                    <li>See exactly which products make the most money.</li>
                    <li>Schedule staff efficiently based on busiest store hours.</li>
                    <li>Email digital receipts to build customer marketing lists.</li>
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
                    <li>Track medicine expiry dates automatically to reduce waste.</li>
                    <li>Manage batch numbers easily for strict safety compliance.</li>
                    <li>Alert staff instantly when critical medicines run low.</li>
                    <li>Handle prescriptions securely with integrated patient profiles.</li>
                    <li>Control restricted drugs using secure digital access logs.</li>
                    <li>Look up drug substitutes instantly during customer checkouts.</li>
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
                    <li>Build custom features tailored to your unique workflow.</li>
                    <li>Scale your system easily as your business grows.</li>
                    <li>Own software completely without paying monthly user licenses.</li>
                    <li>Integrate seamlessly with your existing tools and apps.</li>
                    <li>Gain a competitive edge over local business rivals.</li>
                    <li>Modify the system anytime your business model changes.</li>
                </ul>
            </details>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT SECTION ---------------- #
st.markdown("""
<div class="contact-box">
    <div class="contact-title">Get In Touch</div>
    
    <div class="phone">
        <a href="https://wa.me/923476712269" target="_blank" style="color: white; text-decoration: none;">
            📞 03476712269
        </a>
    </div>

    <div class="location-link">
        <a href="https://www.google.com/maps/search/?api=1&query=Pull+Nehar+Daska" target="_blank" style="color: #cbd5e1; text-decoration: none;">
            📍 Pull Nehar, Daska
        </a>
    </div>

    <a class="call-btn" href="https://wa.me/923476712269" target="_blank">
        Chat on WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)

# Close Main Container
st.markdown("</div>", unsafe_allow_html=True)