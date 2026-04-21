import streamlit as st

# Force High-Contrast Light Mode
st.set_page_config(page_title="KitchenSync", page_icon="🍳", layout="wide")

# --- eMEALS-STYLE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    
    /* Logo Font: Professional but warm */
    .logo-font {
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        font-size: 55px;
        letter-spacing: -2px;
        color: #2D5A27 !important;
        margin-bottom: 0px;
    }
    
    .logo-subtitle {
        color: #D4AF37 !important; /* Gold accent for charity */
        font-weight: 700;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    .plan-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #EAEAEA;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
        min-height: 280px;
    }
    
    .plan-card:hover { transform: translateY(-3px); }

    .plan-title { color: #333; font-weight: 800; font-size: 24px; margin-top: 15px; }
    .plan-wellness { color: #2D5A27; font-weight: 600; font-size: 13px; text-transform: uppercase; }

    /* The "Add to Cart" Button */
    .stButton>button {
        background-color: #2D5A27 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px 30px !important;
        font-weight: 700 !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: Restored Impact Trackers ---
with st.sidebar:
    st.markdown("### ❤️ Your Sheboygan Impact")
    st.metric("Donated to Food Bank", "$1,240")
    st.metric("Meals Provided", "4,960")
    st.write("---")
    st.info("**100% of KitchenSync proceeds support local needs.**")

# --- HEADER (Using Logo Text) ---
st.markdown('<p class="logo-font">KitchenSync</p>', unsafe_allow_html=True)
st.markdown('<p class="logo-subtitle">Wellness & Logistics | Sheboygan County</p>', unsafe_allow_html=True)

# --- WEEKLY PLAN SELECTION GRID ---
st.header("Weekly Meal Curations")
st.write("Choose a curated flow of meals optimized for nutrition, budget, and local Sheboygan County availability.")

col1, col2, col3 = st.columns(3)

# New Mock Data: Weekly Plans, not recipes
plans = [
    {
        "title": "Quick & Healthy (5 Days)", 
        "tag": "Wellness Upgrade | 20min Ave Prep", 
        "meals": "Lemon Chicken, Quinoa Power Bowl, Sheet Pan Salmon...",
        "id": "qh_week1"
    },
    {
        "title": "Plant-Powered Sheboygan (3 Days)", 
        "tag": "Max Nutrition | Farm-to-Table Focus", 
        "meals": "Local Veggie Stir Fry, Black Bean Tacos, Root Roast...",
        "id": "pp_week1"
    },
    {
        "title": "Budget Logistics (5 Days)", 
        "tag": "Walmart Smart Mapping | Save $45+", 
        "meals": "Beef Chili (Steer-Raised Beef), Ground Turkey Skillet, Pasta Bake...",
        "id": "bl_week1"
    }
]

for i, col in enumerate([col1, col2, col3]):
    with col:
        st.markdown(f"""
            <div class="plan-card">
                <div class="plan-wellness">{plans[i]['tag']}</div>
                <div class="plan-title">{plans[i]['title']}</div>
                <p style="color:#666; font-size: 15px; margin-top: 10px;">Includes: {plans[i]['meals']}</p>
            </div>
        """, unsafe_allow_html=True)
        # Unique key for each button
        if st.button("Select Weekly Plan", key=f"select_{plans[i]['id']}"):
            st.session_state.current_plan = plans[i]['title']
            st.session_state.current_plan_id = plans[i]['id']

# --- RESULT AREA ---
if 'current_plan' in st.session_state:
    st.write("---")
    st.success(f"**Excellent Choice!** Syncing the **{st.session_state.current_plan}** directly to your Walmart cart...")
    
    # Placeholders for the Multi-Item API Link we'll build later
    if st.session_state.current_plan_id == "qh_week1":
        st.link_button("🛒 One-Click: Add 15 Quick & Healthy Items", "https://www.walmart.com")
