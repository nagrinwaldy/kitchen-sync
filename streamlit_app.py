import streamlit as st

# Force Light Mode & Layout
st.set_page_config(page_title="KitchenSync", page_icon="🍳", layout="wide")

# --- PREMIUM eMEALS-STYLE CSS ---
st.markdown("""
    <style>
    /* Force a clean, professional white background */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Main Branding */
    .brand-header {
        color: #2D5A27;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        font-size: 50px;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    
    .mission-statement {
        color: #666;
        font-size: 18px;
        margin-bottom: 40px;
    }

    /* The 'eMeals' Style Card */
    .meal-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #EAEAEA;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
        text-align: center;
        min-height: 250px;
    }
    
    .meal-card:hover {
        transform: translateY(-5px);
        border: 1px solid #2D5A27;
    }

    .meal-title {
        color: #333;
        font-weight: 700;
        font-size: 22px;
        margin-top: 15px;
    }

    .meal-meta {
        color: #2D5A27;
        font-weight: 600;
        font-size: 14px;
        text-transform: uppercase;
        margin-top: 10px;
    }

    /* Clean Buttons */
    .stButton>button {
        background-color: #2D5A27 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px 30px !important;
        font-weight: 600 !important;
        width: 100%;
    }

    /* Impact Bar */
    .impact-bar {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #D4AF37;
        color: #444;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="brand-header">KitchenSync</p>', unsafe_allow_html=True)
st.markdown('<p class="mission-statement">Wellness-led meal logistics for Sheboygan County families.</p>', unsafe_allow_html=True)

st.markdown('<div class="impact-bar">❤️ <b>Community Impact:</b> Your clicks today supported 14 meals at the Sheboygan County Food Bank.</div>', unsafe_allow_html=True)

# --- MEAL SELECTION GRID ---
st.subheader("Choose Your Plan")
st.write("Pick a meal and we'll handle the recipes, the nutrition, and the Walmart cart.")

col1, col2, col3 = st.columns(3)

# Mock Data (Soon to be AI-driven)
meals = [
    {"title": "Zesty Lemon Chicken", "tag": "High Protein | 20m", "icon": "🍋"},
    {"title": "Harvest Power Bowl", "tag": "Plant-Based | 15m", "icon": "🥗"},
    {"title": "Plymouth Pan Salmon", "tag": "Omega-3 Focus | 25m", "icon": "🐟"}
]

for i, col in enumerate([col1, col2, col3]):
    with col:
        st.markdown(f"""
            <div class="meal-card">
                <div style="font-size: 50px;">{meals[i]['icon']}</div>
                <div class="meal-title">{meals[i]['title']}</div>
                <div class="meal-meta">{meals[i]['tag']}</div>
            </div>
        """, unsafe_allow_html=True)
        # Using a native button underneath for functionality
        if st.button("Select Plan", key=f"select_{i}"):
            st.session_state.choice = meals[i]['title']

# --- RESULT AREA ---
if 'choice' in st.session_state:
    st.write("---")
    st.success(f"**Perfect.** We are building the wellness plan for **{st.session_state.choice}**.")
    st.link_button("🛒 One-Click to Walmart Cart", "https://www.walmart.com")
