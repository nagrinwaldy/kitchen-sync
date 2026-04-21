import streamlit as st

# 1. Force Clean Light Theme & Accessibility
st.set_page_config(page_title="Hearth | Logistics", page_icon="🔥", layout="wide")

# --- PREMIUM 'PAPER & INK' CSS ---
st.markdown("""
    <style>
    /* Force high-contrast Light Mode */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Global Typography Fixes */
    h1, h2, h3, p, li, span, label { 
        color: #1A1A1B !important; 
        font-family: 'Inter', -apple-system, sans-serif; 
    }

    /* Professional Card Styling */
    .recipe-card {
        background-color: #F9F9FB;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #E1E4E8;
        margin-bottom: 20px;
    }

    .chef-secret-box {
        background-color: #E7F3E2;
        border-left: 4px solid #2D5A27;
        padding: 12px;
        margin: 15px 0;
        font-style: italic;
        font-size: 14px;
    }

    .flavor-tag {
        color: #B28B15;
        font-weight: 800;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Metric Overrides for Visibility */
    [data-testid="stMetricLabel"] p { color: #586069 !important; font-weight: 600 !important; }
    [data-testid="stMetricValue"] div { color: #2D5A27 !important; font-weight: 800 !important; }

    /* Button Styling */
    .stButton>button {
        background-color: #2D5A27 !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col_logo, col_impact = st.columns([2, 1])

with col_logo:
    st.markdown('<h1 style="margin-bottom:0;">🔥 Hearth</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:18px; color:#586069 !important;">Wellness Logistics for Sheboygan Families</p>', unsafe_allow_html=True)

with col_impact:
    st.markdown("""
        <div style="background:#F6F8FA; padding:15px; border-radius:8px; border:1px solid #E1E4E8; text-align:center;">
            <p style="margin:0; font-size:12px; font-weight:bold; color:#B28B15 !important;">COMMUNITY IMPACT</p>
            <p style="margin:0; font-size:20px; font-weight:800;">$1,240 Generated</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- THE PRODUCT WORKFLOW ---
tab_plan, tab_cook, tab_shop = st.tabs(["📅 The Blueprint", "👨‍🍳 Recipe Cards", "🛒 Cart Logistics"])

with tab_plan:
    st.subheader("Your 5-Day Meal Strategy")
    st.info("Goal: 1,575kcal | High Protein | Low Inflammation")
    
    # We use a cleaner column layout for the 5-day view
    d1, d2, d3, d4, d5 = st.columns(5)
    days = ["SUN", "MON", "TUE", "WED", "THU"]
    meals = ["Herb-Roasted Chicken", "Zesty Beef & Cabbage", "Smoky BBQ Chicken", "Savory Beef Tips", "Lemon-Garlic Chicken"]

    for i, col in enumerate([d1, d2, d3, d4, d5]):
        with col:
            st.markdown(f"""
                <div style="padding:15px; border:1px solid #E1E4E8; border-radius:8px; background:white; min-height:120px;">
                    <p style="font-weight:bold; color:#2D5A27 !important; margin-bottom:5px;">{days[i]}</p>
                    <p style="font-size:14px; line-height:1.4;">{meals[i]}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Swap Plan", key=f"btn_swap_{i}"):
                st.toast(f"Finding alternative for {days[i]}...")

with tab_cook:
    st.subheader("Chef Instructions & Flavor Pops")
    
    # Example Recipe Card 1
    st.markdown("""
        <div class="recipe-card">
            <span class="flavor-tag">The Golden Bird</span>
            <h3 style="margin:5px 0;">Herb-Roasted Chicken</h3>
            <div class="chef-secret-box">
                "Dry-brining" and high-heat finishing for paper-crisp skin.
            </div>
            <p style="font-size:14px;"><b>The Pop:</b> Spatchcocking ensures the skin "shatters" while the meat stays juicy.</p>
        </div>
    """, unsafe_allow_html=True)

    # Example Recipe Card 2
    st.markdown("""
        <div class="recipe-card">
            <span class="flavor-tag">The Zesty Pop</span>
            <h3 style="margin:5px 0;">"Crack" Cabbage & Beef Skillet</h3>
            <div class="chef-secret-box">
                Flash-searing cabbage for a nutty, caramelized crunch—zero mush.
            </div>
            <p style="font-size:14px;"><b>The Pop:</b> Kill heat and squeeze fresh lime at the very end to cut the fat perfectly.</p>
        </div>
    """, unsafe_allow_html=True)

with tab_shop:
    st.subheader("Automated Fulfillment")
    st.markdown("Mapping 15 ingredients to **Walmart Plymouth, WI**.")
    if st.button("🚀 Sync All to Walmart Cart", use_container_width=True):
        st.success("Mapping complete. Redirecting to cart...")

# --- FOUNDATIONAL TARGETS ---
st.write("---")
st.markdown("### 📊 Nutritional Foundation")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Target Calories", "1,575")
m2.metric("Protein Goal", "135g")
m3.metric("Carbs", "140g")
m4.metric("Fats", "55g")
