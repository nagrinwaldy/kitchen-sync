import streamlit as st

# Set Page Config
st.set_page_config(page_title="KitchenSync", page_icon="🍳", layout="wide")

# Custom CSS for the "Premium Natural" Look
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    h1 { color: #2D5A27; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        border: 1px solid #EAEAEA;
        text-align: center;
    }
    .charity-banner {
        background-color: #D4AF37;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Charity Header
st.markdown('<div class="charity-banner">❤️ 100% of profits today support the Sheboygan County Food Bank</div>', unsafe_allow_html=True)

st.title("🍳 KitchenSync")
st.write("Optimizing your health, your wallet, and your time.")

# 2. The Efficiency Dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card">🥦<br><b>Wellness Score</b><br><h2>A-</h2></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">💰<br><b>Monthly Savings</b><br><h2>$42.10</h2></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">⏱️<br><b>Time Saved</b><br><h2>3.5 hrs</h2></div>', unsafe_allow_html=True)

st.write("---")

# 3. Input Section
with st.container():
    st.subheader("Plan Your Next Meal")
    meal = st.text_input("What are we eating?", placeholder="e.g., Grass-fed beef stir fry with local greens")
    
    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        if st.button("Sync to Cart"):
            st.balloons()
            st.success("Analyzing for Wellness & Savings...")
