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

/* Service Tabs Styling */
div[data-baseweb="tab-list"] {
    justify-content: center;
    gap: 20px;
}

div[data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 10px 20px;
}

/* Feature List Style */
.feature-list {
    background: rgba(255,255,255,0.03);
    padding: 25px;
    border-radius: 15px;
    border-left: 4px solid #00cfff;
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

# Implementing Tabs to switch between services
tab1, tab2, tab3 = st.tabs(["🛒 Retail POS", "💊 Pharmacy POS", "⚙️ Custom Solutions"])

with tab1:
    st.markdown("""
    <div class="feature-list">
        <ul>
            <li>Automate complex discounts without manual cashier math.</li>
            <li>Reward repeat buyers to keep them coming back.</li>
            <li>Track exact inventory levels in real time effortlessly.</li>
            <li>Get automatic alerts before popular items sell out.</li>
            <li>Prevent employee theft and shoplifting with exact tracking.</li>
            <li>Scan barcodes quickly to shorten busy checkout lines.</li>
            <li>Eliminate costly human calculation mistakes at the register.</li>
            <li>See exactly which products make the most money.</li>
            <li>Schedule staff efficiently based on busiest store hours.</li>
            <li>Email digital receipts to build customer marketing lists.</li>
            <li>Securely back up all business data automatically.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.write("Pharmacy POS features coming soon...")

with tab3:
    st.write("Custom Solutions features coming soon...")

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