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

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #050816, #0a0f1f, #111827);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Remove Streamlit Default Header/Footer */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Global Text */
html, body, [class*="css"] {
    color: white;
}

/* Main Container */
.main-container {
    padding: 2rem 5%;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 90px 20px 60px;
}

.hero h1 {
    font-size: 4rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.hero p {
    font-size: 1.3rem;
    color: #00cfff;
    margin-top: 0;
}

/* Section Titles */
.section-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #ff5c5c;
    margin-bottom: 25px;
    text-align: center;
}

/* About Section */
.about-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 18px;
    line-height: 1.8;
    font-size: 1.08rem;
    box-shadow: 0 0 25px rgba(0, 207, 255, 0.08);
    margin-bottom: 50px;
}

/* Service Cards */
.card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 30px 25px;
    text-align: center;
    transition: 0.3s ease-in-out;
    height: 100%;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}

.card:hover {
    transform: translateY(-8px);
    border-color: #00cfff;
    box-shadow: 0 0 25px rgba(0, 207, 255, 0.25);
}

.card-icon {
    font-size: 3rem;
    margin-bottom: 15px;
}

.card-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
}

.card-desc {
    color: #cbd5e1;
    font-size: 1rem;
    margin-bottom: 15px;
}

/* Contact Section */
.contact-box {
    text-align: center;
    padding: 50px 20px;
    margin-top: 70px;
    background: rgba(255,255,255,0.04);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 25px rgba(255, 92, 92, 0.1);
}

.contact-title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #ff5c5c;
}

.phone {
    font-size: 1.5rem;
    color: #ffffff;
    margin: 15px 0 25px;
    font-weight: 600;
}

/* Call Button */
.call-btn {
    display: inline-block;
    padding: 14px 30px;
    font-size: 1rem;
    font-weight: bold;
    color: white;
    background: linear-gradient(90deg, #ff512f, #dd2476);
    border-radius: 50px;
    text-decoration: none;
    transition: 0.3s ease;
}

.call-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(255, 81, 47, 0.4);
}

/* Responsive */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.5rem;
    }

    .hero p {
        font-size: 1rem;
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

# Initialize Session State
if 'show_retail' not in st.session_state: st.session_state.show_retail = False
if 'show_pharmacy' not in st.session_state: st.session_state.show_pharmacy = False
if 'show_custom' not in st.session_state: st.session_state.show_custom = False

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🛒</div>
        <div class="card-title">Retail POS</div>
        <div class="card-desc">Modern Billing & Inventory management solutions.</div>
    """, unsafe_allow_html=True)
    if st.button("Show Retail Features", key="btn1"):
        st.session_state.show_retail = not st.session_state.show_retail
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">💊</div>
        <div class="card-title">Pharmacy POS</div>
        <div class="card-desc">Smart Expiry & Stock management for pharmacies.</div>
    """, unsafe_allow_html=True)
    if st.button("Show Pharmacy Features", key="btn2"):
        st.session_state.show_pharmacy = not st.session_state.show_pharmacy
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">⚙️</div>
        <div class="card-title">Custom Solutions</div>
        <div class="card-desc">Tailor-made applications for your business.</div>
    """, unsafe_allow_html=True)
    if st.button("Show Custom Features", key="btn3"):
        st.session_state.show_custom = not st.session_state.show_custom
    st.markdown("</div>", unsafe_allow_html=True)

# Display content based on button clicks
if st.session_state.show_retail:
    st.subheader("Retail POS Features")
    st.markdown("""
    - Automate complex discounts without manual cashier math.
    - Reward repeat buyers to keep them coming back.
    - Track exact inventory levels in real time effortlessly.
    - Get automatic alerts before popular items sell out.
    - Prevent employee theft with exact item tracking.
    - Scan barcodes quickly to shorten busy checkout lines.
    - Eliminate calculation mistakes at the cash register.
    - See exactly which products make the most money.
    - Schedule staff efficiently based on busiest store hours.
    - Email digital receipts to build customer marketing lists.
    - Securely back up all business data automatically.
    """)

if st.session_state.show_pharmacy:
    st.subheader("Pharmacy POS Features")
    st.markdown("""
    - Track medicine expiry dates automatically to reduce waste.
    - Manage batch numbers easily for strict safety compliance.
    - Alert staff instantly when critical medicines run low.
    - Handle prescriptions securely with integrated patient profiles.
    - Control restricted drugs using secure digital access logs.
    - Look up drug substitutes instantly during customer checkouts.
    """)

if st.session_state.show_custom:
    st.subheader("Custom Software Development")
    st.markdown("""
    - Build custom features tailored to your unique workflow.
    - Scale your system easily as your business grows.
    - Own software completely without paying monthly user licenses.
    - Integrate seamlessly with your existing tools and apps.
    - Gain a competitive edge over local business rivals.
    - Modify the system anytime your business model changes.
    """)

# ---------------- CONTACT SECTION ---------------- #
st.markdown("""
<div class="contact-box">
    <div class="contact-title">Get In Touch</div>
    <div class="phone">📞 03476712269</div>

    <a class="call-btn" href="tel:03476712269">
        Call Now
    </a>
</div>
""", unsafe_allow_html=True)

# Close Main Container
st.markdown("</div>", unsafe_allow_html=True)