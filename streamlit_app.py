import streamlit as st

# Force High-Contrast UI
st.set_page_config(page_title="Hearth | Logistics", page_icon="🔥", layout="wide")

# --- THE "HEARTH" PROFESSIONAL CSS ---
st.markdown("""
    <style>
    /* Force Dark Slate Theme - No more washed out text */
    .stApp { background-color: #111418 !important; }
    
    /* Premium Card Design */
    .recipe-card {
        background-color: #1A1D23;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #2D333B;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    .chef-secret {
        background-color: #2D5A27;
        color: white;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 14px;
        font-style: italic;
        margin: 10px 0;
    }

    .flavor-pop {
        color: #D4AF37;
        font-weight: 800;
        text-transform: uppercase;
        font-size: 12px;
        letter-spacing: 1px;
    }

    h1, h2, h3, p, li { color: #FFFFFF !important; font-family: 'Inter', sans-serif; }
    
    .metric-box {
        text-align: center;
        padding: 15px;
        background: #1A1D23;
        border-radius: 12px;
        border-top: 4px solid #D4AF37;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<h1 style="font-size: 42px; margin-bottom:0;">🔥 Hearth</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#81C784 !important; font-weight:600;">Wellness Logistics | Sheboygan County</p>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-box">
            <span style="color:#D4AF37; font-weight:bold;">COMMUNITY IMPACT</span><br>
            <span style="font-size:24px; font-weight:800;">$1,240 Donated</span>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- THE WORKFLOW: REFINEMENT ---
tab1, tab2, tab3 = st.tabs(["📅 Weekly Blueprint", "👨‍🍳 Chef's Recipe Cards", "🛒 Automated Cart"])

with tab1:
    st.subheader("Your 5-Day Homestead Harvest [cite: 2, 70]")
    
    # Mocking the interaction: In the real app, Gemini would fill these
    cols = st.columns(5)
    days = ["SUN", "MON", "TUE", "WED", "THU"]
    meals = ["Herb-Roasted Chicken", "Zesty Beef & Cabbage", "Smoky BBQ Chicken", "Savory Beef Tips", "Lemon-Garlic Chicken"] [cite: 4]
    
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"""
                <div style="background:#1A1D23; padding:15px; border-radius:10px; border:1px solid #2D333B;">
                    <p style="color:#D4AF37 !important; font-weight:bold; margin-bottom:5px;">{days[i]}</p>
                    <p style="font-size:14px; min-height:40px;">{meals[i]}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Swap", key=f"swp_{i}"):
                st.toast("Gemini is finding an alternative...")

with tab2:
    st.subheader("The 'Flavor Pop' Collection [cite: 9]")
    
    # Recipe 1: Roasted Chicken
    with st.container():
        st.markdown(f"""
            <div class="recipe-card">
                <span class="flavor-pop">The Golden Bird [cite: 10]</span>
                <h3 style="margin-top:5px;">Herb-Roasted Chicken</h3>
                <div class="chef-secret">"Dry-brining" and high-heat finishing for paper-crisp skin.</div>
                <p><b>Technique:</b> Spatchcocking ensures the skin "shatters" while meat stays juicy[cite: 14].</p>
                <p style="font-size:13px; color:#AAA !important;">Ingredients: 2 Whole Chickens, Avocado Oil, Rosemary, Thyme, Lemon[cite: 12].</p>
            </div>
        """, unsafe_allow_html=True)

    # Recipe 2: Cabbage & Beef
    with st.container():
        st.markdown(f"""
            <div class="recipe-card">
                <span class="flavor-pop">The Zesty Pop </span>
                <h3 style="margin-top:5px;">"Crack" Cabbage & Beef Skillet</h3>
                <div class="chef-secret">Flash-searing cabbage for a nutty, caramelized crunch—zero mush[cite: 16].</div>
                <p><b>Technique:</b> Kill heat and squeeze fresh lime at the very end to cut the beef fat perfectly.</p>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.subheader("Logistics & Cart Mapping")
    st.info("Mapping to your Sheboygan Walmart: 15 items identified[cite: 38].")
    if st.button("🚀 Sync Complete Plan to Walmart Cart"):
        st.success("Successfully mapped all ingredients to your cart!")

# --- WIFE'S MACRO TRACKER (Visual Footer) ---
st.write("---")
st.markdown("### 📊 Foundation Targets [cite: 63]")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Calories", "1,575", "[cite: 65]")
c2.metric("Protein", "135g", "[cite: 66]")
c3.metric("Carbs", "140g", "[cite: 67]")
c4.metric("Fats", "55g", "[cite: 68]")
