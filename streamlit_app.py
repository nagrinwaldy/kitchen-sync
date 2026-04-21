import streamlit as st

# Force High-Contrast Light Mode
st.set_page_config(page_title="Rooted & Ready", page_icon="🌱", layout="wide")

st.markdown("""
    <style>
    /* Force Light Mode - No more washed out green-on-green */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Strict Typography for Readability */
    h1, h2, h3, p, li, span, label { 
        color: #121212 !important; /* Deep Ink Charcoal */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Professional Card Styling */
    .data-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        border: 2px solid #E5E7EB; /* Distinct light-grey border */
        margin-bottom: 20px;
    }

    /* Chef Secret - High Contrast Fix */
    .secret-callout {
        background-color: #F9FAFB;
        border-left: 6px solid #2D5A27;
        padding: 15px;
        margin: 15px 0;
        font-weight: 500;
        line-height: 1.6;
    }

    .pop-label {
        color: #854D0E !important; /* High-contrast Dark Gold */
        font-weight: 800;
        font-size: 11px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Button - Force Visibility */
    .stButton>button {
        background-color: #2D5A27 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER: Wellness & Impact ---
c1, c2 = st.columns([2, 1])
with c1:
    st.markdown('<h1 style="font-size: 44px; margin-bottom:0;">Rooted & Ready</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 18px; color: #4B5563 !important;">Wellness Logistics for Sheboygan Families</p>', unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div style="background:#F3F4F6; padding:15px; border-radius:10px; border:1px solid #D1D5DB; text-align:center;">
            <p style="margin:0; font-size:11px; font-weight:800; color:#854D0E !important;">CHARITY EARNED</p>
            <p style="margin:0; font-size:24px; font-weight:900;">$1,240.00</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- APP TABS ---
tab_plan, tab_chef, tab_cart = st.tabs(["📅 Weekly Blueprint", "👨‍🍳 Chef Cards", "🛒 Logistics"])

with tab_plan:
    st.subheader("Your 5-Day Meal Blueprint")
    st.markdown("**Constraint Targets:** 1,575 kcal | 135g Protein | 140g Carb [cite: 65, 66, 67]")
    
    plan_cols = st.columns(5)
    days = ["SUN", "MON", "TUE", "WED", "THU"]
    # Integrating your specific plan [cite: 4]
    meals = [
        "Herb-Roasted Chicken", 
        "Zesty Beef & Cabbage", 
        "Smoky BBQ Chicken", 
        "Savory Beef Tips", 
        "Lemon-Garlic Chicken"
    ]

    for i, col in enumerate(plan_cols):
        with col:
            st.markdown(f"""
                <div class="data-card" style="min-height: 150px;">
                    <p style="font-weight: 800; color: #2D5A27 !important; margin-bottom: 10px;">{days[i]}</p>
                    <p style="font-size: 15px; font-weight: 600;">{meals[i]}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Swap", key=f"sw_{i}"):
                st.toast(f"Swapping {days[i]}...")

with tab_chef:
    st.subheader("Culinary Secrets & Texture Pops")
    
    # Sunday Card [cite: 10, 11, 14]
    st.markdown("""
        <div class="data-card">
            <span class="pop-label">Sunday Pop: The Shatter</span>
            <h3 style="margin: 5px 0;">Herb-Roasted "Golden Bird"</h3>
            <div class="secret-callout">
                <b>Chef Secret:</b> "Dry-brine" and spatchcock to ensure the skin shatters while the meat stays juicy.
            </div>
            <p style="font-size: 14px; color: #4B5563 !important;"><b>Ingredients:</b> Whole Chickens, Avocado Oil, Rosemary, Thyme, Lemon[cite: 12].</p>
        </div>
    """, unsafe_allow_html=True)

    # Monday Card [cite: 15, 16, 20]
    st.markdown("""
        <div class="data-card" style="margin-top: 20px;">
            <span class="pop-label">Monday Pop: High-Acid Finish</span>
            <h3 style="margin: 5px 0;">Zesty "Crack" Cabbage & Beef</h3>
            <div class="secret-callout">
                <b>Chef Secret:</b> Flash-sear cabbage in a "smoking hot" skillet for zero mush and caramelized crunch.
            </div>
            <p style="font-size: 14px; color: #4B5563 !important;"><b>The Logic:</b> Kill the heat and squeeze fresh lime to cut the beef fat perfectly.</p>
        </div>
    """, unsafe_allow_html=True)

with tab_cart:
    st.subheader("Automated Logistics Mapping")
    st.markdown("15 unique items mapped to **Walmart Plymouth, WI**[cite: 38].")
    if st.button("🚀 Sync Blueprint to Walmart Cart", use_container_width=True):
        st.success("Successfully synchronized items!")
