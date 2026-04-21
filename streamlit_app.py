import streamlit as st

# 1. Force Clean Light Theme & Strict Accessibility
st.set_page_config(page_title="Hearth | Logistics", page_icon="🔥", layout="wide")

# --- PROFESSIONAL ACCESSIBILITY CSS ---
st.markdown("""
    <style>
    /* Force high-contrast Light Mode - Pure White Background */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Strict Text Colors - No more washing out */
    h1, h2, h3, p, li, span, label { 
        color: #1A1A1B !important; /* Deep Charcoal */
        font-family: 'Inter', -apple-system, sans-serif; 
    }

    /* Professional Card Styling with Borders for Definition */
    .plan-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #D1D5DB; /* Clean Grey Border */
        margin-bottom: 10px;
    }

    /* Chef Secret Box - High Contrast Fix */
    .chef-secret-box {
        background-color: #F3F4F6; /* Light Grey instead of Green */
        border-left: 5px solid #2D5A27; /* Deep Forest Green Accent */
        padding: 15px;
        margin: 15px 0;
        color: #1A1A1B !important;
        font-style: italic;
        font-size: 15px;
    }

    .flavor-pop-label {
        color: #92400E !important; /* Deep Amber/Gold */
        font-weight: 800;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Metric Colors for Readability */
    [data-testid="stMetricLabel"] p { color: #4B5563 !important; font-weight: 600 !important; }
    [data-testid="stMetricValue"] div { color: #2D5A27 !important; font-weight: 800 !important; }

    /* Button Styling - High Contrast */
    .stButton>button {
        background-color: #2D5A27 !important;
        color: #FFFFFF !important;
        border-radius: 4px !important;
        border: none !important;
        font-weight: 700 !important;
        padding: 10px 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col_logo, col_impact = st.columns([2, 1])

with col_logo:
    st.markdown('<h1 style="margin-bottom:0; font-size: 48px;">Hearth</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:18px; color:#4B5563 !important; font-weight:500;">Intelligent Wellness Logistics</p>', unsafe_allow_html=True)

with col_impact:
    st.markdown("""
        <div style="background:#F9FAFB; padding:15px; border-radius:8px; border:1px solid #D1D5DB; text-align:center;">
            <p style="margin:0; font-size:11px; font-weight:bold; color:#92400E !important; letter-spacing:1px;">COMMUNITY IMPACT</p>
            <p style="margin:0; font-size:22px; font-weight:800; color:#1A1A1B;">$1,240.00 Earned</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- PRODUCT WORKFLOW TABS ---
tab_plan, tab_cards, tab_logistics = st.tabs(["📅 Weekly Blueprint", "👨‍🍳 Chef's Recipe Cards", "🛒 Shopping Cart"])

# TAB 1: THE BLUEPRINT (Using your Source 4 Data)
with tab_plan:
    st.subheader("Your 5-Day Meal Blueprint")
    st.markdown("**Core Constraints:** 1,575 kcal | 135g Protein | Sheboygan Seasonal")
    
    plan_cols = st.columns(5)
    days = ["SUN", "MON", "TUE", "WED", "THU"]
    meals = [
        "Herb-Roasted Chicken [cite: 10]", 
        "Zesty Beef & Cabbage [cite: 15]", 
        "Smoky BBQ Chicken [cite: 21]", 
        "Savory Beef Tips [cite: 27]", 
        "Lemon-Garlic Chicken [cite: 4]"
    ]

    for i, col in enumerate(plan_cols):
        with col:
            st.markdown(f"""
                <div class="plan-card">
                    <p style="color:#2D5A27 !important; font-weight:bold; margin-bottom:8px;">{days[i]}</p>
                    <p style="font-size:14px; font-weight:500; color:#1A1A1B;">{meals[i]}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Swap Meal", key=f"swap_{i}"):
                st.toast(f"Requesting new option for {days[i]} from Gemini...")

# TAB 2: RECIPE CARDS (Using your Source 9-37 Data)
with tab_cards:
    st.subheader("Chef Instructions & Flavor Pops")
    
    # Recipe Card 1: The Golden Bird
    st.markdown(f"""
        <div class="plan-card" style="border-left: 8px solid #2D5A27;">
            <span class="flavor-pop-label">Sunday: The Golden Bird [cite: 10]</span>
            <h3 style="margin:5px 0;">Herb-Roasted Chicken</h3>
            <div class="chef-secret-box">
                <b>The Chef's Secret:</b> "Dry-brining" and high-heat finishing for paper-crisp skin. [cite: 11]
            </div>
            <p><b>The Pop:</b> Spatchcocking ensures the skin "shatters" while the meat stays juicy. [cite: 14]</p>
            <p style="font-size:13px; color:#4B5563 !important;"><b>Key Ingredients:</b> Whole Chickens, Avocado Oil, Rosemary, Thyme, Lemon. [cite: 12]</p>
        </div>
    """, unsafe_allow_html=True)

    # Recipe Card 2: Zesty Cabbage
    st.markdown(f"""
        <div class="plan-card" style="border-left: 8px solid #2D5A27; margin-top:20px;">
            <span class="flavor-pop-label">Monday: The Zesty Pop [cite: 15]</span>
            <h3 style="margin:5px 0;">"Crack" Cabbage & Beef Skillet</h3>
            <div class="chef-secret-box">
                <b>The Chef's Secret:</b> Flash-searing cabbage for a nutty, caramelized crunch—zero mush. [cite: 16]
            </div>
            <p><b>The Pop:</b> Kill heat and squeeze fresh lime at the very end to cut the beef fat perfectly. [cite: 20]</p>
        </div>
    """, unsafe_allow_html=True)

# TAB 3: LOGISTICS (Using your Source 38-61 Data)
with tab_logistics:
    st.subheader("Automated Fulfillment")
    st.write("Mapping 15 unique ingredients to your nearest Walmart.")
    
    if st.button("🚀 Sync Blueprint to Walmart Cart", use_container_width=True):
        st.success("Successfully mapped 15 items. Cart is ready for checkout!")

# --- FOUNDATIONAL TARGETS (Using Source 65-68 Data) ---
st.write("---")
st.markdown("### 📊 Nutritional Foundation")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Daily Calories", "1,575 [cite: 65]")
m2.metric("Protein Foundation", "135g [cite: 66]")
m3.metric("Energy Carbs", "140g [cite: 67]")
m4.metric("Support Fats", "55g [cite: 68]")
