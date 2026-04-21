import streamlit as st

# Page Branding
st.set_page_config(page_title="KitchenSync | Sheboygan", page_icon="🍳", layout="wide")

# Custom Styles for the PoC
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    .main-header { color: #2D5A27; font-size: 40px; font-weight: 800; margin-bottom: 0px; }
    .sub-text { color: #666; font-size: 18px; margin-bottom: 30px; }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #EEE;
        margin-bottom: 10px;
    }
    .wellness-tag { color: #2D5A27; font-weight: bold; background: #E8F5E9; padding: 4px 8px; border-radius: 5px; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: Profile & Settings ---
with st.sidebar:
    st.image("https://www.gstatic.com/lamda/images/gemini_sparkle_v002.svg", width=50) # Placeholder Logo
    st.markdown("## KitchenSync Controls")
    persona = st.selectbox("View Profile", ["The Hearth (Wellness/Family)", "The Blueprint (Efficiency/Pro)"])
    st.slider("Target Budget ($/week)", 50, 500, 150)
    st.checkbox("Prioritize Organic (Walmart)", value=True)
    
    st.write("---")
    st.markdown("### ❤️ Local Impact")
    st.info("**Beneficiary:** Sheboygan County Food Bank\n\n**Total Generated:** $1,240.00")

# --- MAIN SECTION: The Dashboard ---
st.markdown('<p class="main-header">🍳 KitchenSync</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Feeding Sheboygan County families with precision and heart.</p>', unsafe_allow_html=True)

# Horizontal Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Weekly Wellness", "92%", "↑ 4%")
m2.metric("Projected Savings", "$18.50", "-12%")
m3.metric("Time Saved", "42 min", "High")
m4.metric("Charity Credit", "$4.20", "Active")

st.write("---")

# --- TWO COLUMN LAYOUT: Planning & Preview ---
left_col, right_col = st.columns([1, 1.2])

with left_col:
    st.subheader("📝 Meal Plan Entry")
    meal_input = st.text_area("What are we eating this week?", 
                              placeholder="Monday: Taco Night with extra veggies\nTuesday: Sheet pan salmon and asparagus...",
                              height=150)
    
    if st.button("🚀 Sync Everything to Walmart", use_container_width=True):
        st.toast("Optimizing for Wellness & Price...")
        st.balloons()

with right_col:
    st.subheader("🛒 Cart Preview (Live Logic)")
    
    # Mock Item 1
    with st.container():
        st.markdown("""
        <div class="card">
            <span class="wellness-tag">WELLNESS UPGRADE</span>
            <p><b>Great Value Organic Black Beans</b><br>
            <small>Swapped from regular to reduce sodium | Saved: $0.15</small></p>
        </div>
        """, unsafe_allow_html=True)
        
    # Mock Item 2
    with st.container():
        st.markdown("""
        <div class="card">
            <span class="wellness-tag">TIME SAVER</span>
            <p><b>Pre-Washed Organic Kale Medley (12oz)</b><br>
            <small>Optimized for 15-min prep time | Price: $3.98</small></p>
        </div>
        """, unsafe_allow_html=True)

    st.button("Checkout at Walmart (Plymouth, WI)")
