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
    text_color = "#FFFFFF"  # Pure White
    accent_color = "#81C784" # Mint Green
    border_color = "#333333"

# --- GLOBAL CSS OVERRIDE ---
st.markdown(f"""
    <style>
    /* 1. The Main Background */
    .stApp {{
        background-color: {bg_color} !important;
    }}
    
    /* 2. Global Text Colors - This fixes the 'lost' text */
    h1, h2, h3, h4, p, span, label, .stMarkdown {{
        color: {text_color} !important;
    }}

    /* 3. Specific fix for Input Labels (like 'Plan Your Meal') */
    div[data-baseweb="form-control-container"] label {{
        color: {text_color} !important;
        font-weight: bold !important;
    }}

    /* 4. Metric Styling */
    [data-testid="stMetricLabel"] p {{
        color: {accent_color} !important;
        font-weight: bold !important;
    }}
    [data-testid="stMetricValue"] div {{
        color: {text_color} !important;
    }}

    /* 5. Custom Card Styling */
    .metric-card {{
        background-color: {bg_color};
        padding: 20px;
        border-radius: 12px;
        border: 2px solid {border_color};
        text-align: center;
        margin-bottom: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- THE PAGE CONTENT ---
st.markdown(f'<h1 style="color:{text_color};">🍳 KitchenSync</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color:{accent_color}; font-size:20px;">Intelligent Wellness for Sheboygan County</p>', unsafe_allow_html=True)

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
    st.subheader("Plan Your Meal") # This should now be white/green
    meal = st.text_input("What are we eating this week?", placeholder="e.g. Grass-fed beef stir fry")
    if st.button("Generate Wellness Cart"):
        st.success("Optimizing for Nutrition & Local Impact...")

with right:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin-top:0;">🛒 Live Preview</h3>
        <p>Your Walmart cart will be optimized for:<br>
        <b style="color:{accent_color};">Nutritional Value | Best Price | Time Saved</b></p>
    </div>
    """, unsafe_allow_html=True)
