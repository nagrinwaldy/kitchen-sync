import streamlit as st

# Set page config
st.set_page_config(page_title="KitchenSync", page_icon="🍳", layout="wide")

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.markdown("## ⚙️ App Settings")
    persona = st.radio("Style Profile", ["The Hearth (Wellness)", "The Blueprint (Efficiency)"])
    st.write("---")
    st.markdown("### ❤️ Sheboygan Impact")
    st.metric("Donated to Food Bank", "$1,240")

# --- DYNAMIC THEMING LOGIC ---
if persona == "The Hearth (Wellness)":
    bg_color = "#FDFBF7"    # Warm Parchment
    text_color = "#2D5A27"  # Deep Forest Green
    accent_color = "#4F6F52"
    border_color = "#E0D7C6"
else:
    bg_color = "#121212"    # Slate Black
    text_color = "#E0E0E0"  # Crisp White/Silver
    accent_color = "#81C784" # Mint Green
    border_color = "#333333"

# --- AGGRESSIVE CSS INJECTION ---
st.markdown(f"""
    <style>
    /* Force the main background */
    .stApp {{
        background-color: {bg_color} !important;
    }}
    
    /* Force all text inside our 'cards' to be legible */
    .metric-card {{
        background-color: {bg_color};
        padding: 20px;
        border-radius: 12px;
        border: 2px solid {border_color};
        text-align: center;
        margin-bottom: 10px;
    }}

    .main-title {{
        color: {text_color} !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 0px;
    }}

    .sub-title {{
        color: {accent_color} !important;
        font-size: 20px;
        margin-bottom: 30px;
    }}

    /* Fix Streamlit's default metric labels which get washed out */
    [data-testid="stMetricLabel"] p {{
        color: {accent_color} !important;
        font-weight: bold !important;
    }}
    [data-testid="stMetricValue"] div {{
        color: {text_color} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- THE PAGE CONTENT ---
st.markdown(f'<p class="main-title">🍳 KitchenSync</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">Intelligent Wellness for Sheboygan County</p>', unsafe_allow_html=True)

# Metrics Row
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Wellness Score", "94%", "↑ 2%")
with m2:
    st.metric("Saved This Month", "$42.10")
with m3:
    st.metric("Charity Earned", "$8.40")

st.write("---")

# The "Action" Area
left, right = st.columns([1, 1])

with left:
    st.subheader("Plan Your Meal")
    meal = st.text_input("What are we eating?", placeholder="e.g. Grass-fed beef stir fry")
    if st.button("Generate Wellness Cart"):
        st.success("Optimizing for Nutrition & Local Impact...")

with right:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color:{text_color};">🛒 Live Preview</h3>
        <p style="color:{accent_color};">Your Walmart cart will be optimized for:<br>
        <b>Nutritional Value | Best Price | Time Saved</b></p>
    </div>
    """, unsafe_allow_html=True)
