import streamlit as st

# Force High-Contrast Adaptive Look
st.set_page_config(page_title="KitchenSync PoC", page_icon="🍳", layout="wide")

# --- DYNAMIC ADAPTIVE CSS ---
st.markdown("""
    <style>
    /* 1. Default (Light Mode) Variables */
    :root {
        --bg-color: #FDFBF7; /* Warm Parchment */
        --card-bg: #FFFFFF;
        --text-main: #2D5A27; /* Forest Green */
        --text-sub: #444444;
        --accent-charity: #D4AF37; /* Gold */
        --border-color: #E0D7C6;
    }

    /* 2. Dark Mode Variables (Automatic Toggle) */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #0F1116; /* Deep Slate */
            --card-bg: #1A1D23;
            --text-main: #81C784; /* Mint Green readability */
            --text-sub: #BBBBBB;
            --accent-charity: #FFD54F; /* Brighter Gold readability */
            --border-color: #333333;
        }
    }

    .stApp { background-color: var(--bg-color) !important; }
    
    /* Dynamic Typography using var() */
    h1, h2, h3, h4, p, span, label, .stMarkdown {
        color: var(--text-sub) !important;
    }

    /* Master Brand Header (Text-based placeholder until URL provided) */
    .brand-logo-text {
        font-family: 'Arial Black', sans-serif;
        font-size: 55px;
        color: var(--text-main) !important;
        margin-bottom: 0px;
    }

    /* Adaptive Verified Badge */
    .verified-badge {
        color: var(--accent-charity) !important;
        background-color: var(--card-bg);
        padding: 5px 12px;
        border-radius: 50px;
        border: 2px solid var(--accent-charity);
        font-weight: 700;
        font-size: 14px;
        display: inline-block;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    /* Impact Bar Fix (Now dynamic) */
    .impact-bar-adaptive {
        background-color: var(--card-bg);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid var(--accent-charity);
        color: var(--text-sub) !important;
        margin-bottom: 30px;
        font-size: 14px;
    }
    
    /* eMeals Legit Meal Card */
    .meal-card {
        background-color: var(--card-bg);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid var(--border-color);
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
        min-height: 250px;
        margin-bottom: 15px;
    }
    
    .stButton>button {
        background-color: var(--text-main) !important;
        color: var(--bg-color) !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px 30px !important;
        font-weight: 700 !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- THE PAGE CONTENT ---

header_col, impact_col = st.columns([1, 1])

with header_col:
    # Logo Placeholder: Provide a public URL to make this the actual image.
    st.markdown('<p class="brand-logo-text">KitchenSync PoC</p>', unsafe_allow_html=True)
    st.markdown('<div class="verified-badge">✅ Social Enterprise | Sheboygan County</div>', unsafe_allow_html=True)

with impact_col:
    # Adaptive Impact Bar
    st.markdown('<div class="impact-bar-adaptive">❤️ Your use of this app funded **14 meals** at the Sheboygan County Food Bank today.</div>', unsafe_allow_html=True)

st.write("---")

# --- MEAL DISCOVERY SECTION ---
st.header("Weekly Meal Curations")
st.write("AI-optimized meal flows based on peak wellness, budget logistics, and local availability.")

col1, col2, col3 = st.columns(3)

# Mock Curations
curations = [
    {
        "title": "Quick & Healthy (5 Days)", 
        "id": "qh_week1"
    },
    {
        "title": "Budget Logistics (3 Days)", 
        "id": "bl_week1"
    },
    {
        "title": "Wellness Upgrade (5 Days)", 
        "id": "wu_week1"
    }
]

for i, col in enumerate([col1, col2, col3]):
    with col:
        st.markdown(f"""
            <div class="meal-card">
                <div style="font-size: 50px; text-align:center;">🍳</div>
                <h3 style="color: var(--text-main) !important; text-align:center;">{curations[i]['title']}</h3>
                <p style="font-size: 14px; text-align:center;">Includes: Lemon Chicken, Power Bowl, Chili (local beef)...</p>
            </div>
        """, unsafe_allow_html=True)
        # Using a native button underneath for functionality
        if st.button("Select Plan", key=f"select_{curations[i]['id']}"):
            st.session_state.current_choice = curations[i]['title']
