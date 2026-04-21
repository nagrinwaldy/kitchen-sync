import streamlit as st

# Page Branding & Neutral Theme (Works for Light & Dark)
st.set_page_config(page_title="KitchenSync PoC", page_icon="🍳", layout="wide")

# Bulletproof Neutral CSS
st.markdown("""
    <style>
    .stApp { background-color: #0F1116 !important; } /* Deep Slate */
    h1, h2, h3, h4, p, span, label { color: #FFFFFF !important; }
    .stButton>button { 
        background-color: #2D5A27 !important; 
        color: white !important; 
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
    }
    .option-card {
        background-color: #1A1D23;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 20px;
    }
    .metric-text { color: #81C784 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: The Foundational Context ---
with st.sidebar:
    st.markdown('<h1 style="color:#2D5A27; font-weight:800;">KitchenSync</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#D4AF37; margin-top:-10px;">Wellness & Logistics | Sheboygan</p>', unsafe_allow_html=True)
    st.write("---")

    st.markdown("## ⚙️ Foundational Profile")
    st.caption("Context: Wife's Maco Goals (1,575kcal, 135g Protein, 140g Carbs, 55g Fat), Sheboygan Seasonality.")
    
    #🚀 Action
    if st.button("Generate My 5-Day Blueprint", use_container_width=True):
        st.session_state.data_loaded = True
        st.balloons()
        
    st.write("---")
    st.markdown("### ❤️ Local Impact")
    st.metric("Sheboygan Food Bank Support", "$1,240")

# --- MAIN SECTION ---
st.header("Home Culinary Operating System")

if 'data_loaded' in st.session_state:
    st.subheader("Your 5-Day Blueprint (Refinement)")
    
    # TAB VIEW: Layout & Refinement
    tab1, tab2 = st.tabs(["Overview & Refinement", "Recipe Cards"])

    # 1. THE REFINEMENT FLOW
    with tab1:
        st.write("This is your high-level view. Need a change? Hit the Swap button.")
        
        d1, d2, d3, d4, d5 = st.columns(5)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        # MOCK DATA from your source (We will automate this generation with Gemini)
        current_meals = [
            {"dinner": "Zesty Beef & Cabbage "},
            {"dinner": "Smoky BBQ Chicken Bowls "},
            {"dinner": "Savory Beef Tips "},
            {"dinner": "Lemon-Garlic Chicken"},
            {"dinner": "Sovereign Steak Hash "}
        ]

        for i, col in enumerate([d1, d2, d3, d4, d5]):
            with col:
                st.markdown(f"""
                    <div class="option-card" style="min-height:220px;">
                        <h4>{days[i]} Dinner</h4>
                        <p style="font-size:14px; color:#AAA;">{current_meals[i]['dinner']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # The 'Swap' Loop
                if st.button(f"🔄 Swap {days[i]}", key=f"swap_{days[i]}"):
                    st.toast(f"Generating alternative for {days[i]} Dinner ...")

        # 🚀 Final Execution
        st.write("---")
        st.subheader("Finalize & Cart (Sheboygan Logistics Mapping)")
        st.write("Consolidating 5 days, mapping to Master List & Red Potatoes...")
        
        if st.button("🛒 Generate Unified Walmart Add to Cart Link", use_container_width=True):
            st.success("Mapping 15 Items via Affiliate Bridge... [MOCK DONE]")

    # 2. THE RECIPE CARDS
    with tab2:
        st.subheader("Chef's Recipe Cards")
        
        # Displaying selected cards from your data
        with st.expander("1. The 'Golden Bird' (Sunday Dinner)"):
            st.markdown("""
            **Chef's Secret :** 'Dry-brining' for paper-crisp skin.
            *Ingredients :* 2 Chickens, Avocado Oil, Lemon, Herbs.
            *Pop:* Spatchcocking ensures skin 'shatters'.
            """)

        with st.expander("2. Zesty 'Crack' Cabbage & Beef (Monday Dinner)"):
            st.markdown("""
            **Chef's Secret :** Flash-searing cabbage for zero mush.
            *Ingredients :* 1.5lbs Sirloin, Cabbage, Onion, Limes, Garlic.
            *Method:* Return beef, kill heat, squeeze limes. Pop cuts the fat perfectly .
            """)
