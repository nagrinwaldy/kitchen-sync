import streamlit as st

# Force High-Contrast Neutral (Fixes Dark/Light adaptive issue)
st.set_page_config(page_title="KitchenSync PoC", page_icon="🍳", layout="wide")

# --- PREMIUM eMEALS-STYLE CSS ---
st.markdown("""
    <style>
    /* Default (Light Mode) Variables */
    :root {
        --bg-color: #FFFFFF;
        --card-bg: #FDFBF7; /* Warm Parchment */
        --text-main: #2D5A27; /* Deep Forest Green */
        --text-sub: #444444;
        --border-color: #E0D7C6;
    }

    /* Dark Mode Variables (Automatic Toggle) */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #0F1116;
            --card-bg: #1A1D23;
            --text-main: #81C784; /* Mint Green for readability */
            --text-sub: #BBBBBB;
            --border-color: #333333;
        }
    }

    .stApp { background-color: var(--bg-color) !important; }
    
    /* Logo Font: Professional but warm */
    .brand-logo {
        color: var(--text-main) !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 55px;
        letter-spacing: -3px;
        margin-bottom: 0px;
    }
    .brand-subtitle {
        color: #D4AF37 !important; /* Gold accent for charity */
        font-weight: 700;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    /* The 'eMeals' Style Meal Card */
    .meal-card {
        background-color: var(--card-bg);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid var(--border-color);
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
        text-align: center;
        min-height: 250px;
        margin-bottom: 15px;
    }
    
    .meal-card:hover { transform: translateY(-3px); }

    .meal-title {
        color: var(--text-main);
        font-weight: 800;
        font-size: 24px;
        margin-top: 15px;
    }
    
    .meal-meta {
        color: #D4AF37; /* Gold for wellness status */
        font-weight: 600;
        font-size: 13px;
        text-transform: uppercase;
        margin-top: 5px;
    }

    /* Clean Buttons */
    .stButton>button {
        background-color: var(--text-main) !important;
        color: var(--bg-color) !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px 30px !important;
        font-weight: 700 !important;
        width: 100%;
    }

    /* The Impact Tracker (Now integrated on the main page) */
    .impact-bar {
        background-color: var(--card-bg);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #D4AF37;
        color: var(--text-sub);
        margin-bottom: 30px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- THE PAGE CONTENT (Isolation Strategy) ---

# We use columns to put the logo and the impact tracker side-by-side
logo_col, impact_col = st.columns([1, 1])

with logo_col:
    # We will swap this text for the actual logo image URL once you have it uploaded
    st.markdown('<p class="brand-logo">KitchenSync</p>', unsafe_allow_html=True)
    st.markdown('<p class="brand-subtitle">Wellness & Logistics | Sheboygan County</p>', unsafe_allow_html=True)

with impact_col:
    # This bar replaces the washed-out sidebar
    st.markdown('<div class="impact-bar">❤️ <b>Verified Community Impact:</b> Your clicks today supported 14 meals at the Sheboygan County Food Bank.</div>', unsafe_allow_html=True)

st.write("---")

# --- MEAL DISCOVERY (The Pick-List) ---
st.header("Weekly Meal Curations")
st.write("AI-optimized meal flows based on peak wellness, budget logistics, and Sheboygan County availability.")

col1, col2, col3 = st.columns(3)

# Mock Data (Soon to be AI-driven)
meals = [
    {
        "title": "Zesty Lemon Chicken", 
        "tag": "High Protein | Wellness Boost", 
        "id": "zl_chicken"
    },
    {
        "title": "Quinoa & Black Bean Power Bowls", 
        "tag": "Max Fiber | Budget Win", 
        "id": "qbb_bowls"
    },
    {
        "title": "Pan-Seared Salmon & Asparagus", 
        "tag": "Omega-3 Focus | Seasonal Pick", 
        "id": "psa_salmon"
    }
]

for i, col in enumerate([col1, col2, col3]):
    with col:
        # eMeals-style card injection
        st.markdown(f"""
            <div class="meal-card">
                <div style="font-size: 50px;">🍳</div> # Placeholder for image/emoji
                <div class="meal-title">{meals[i]['title']}</div>
                <div class="meal-meta">{meals[i]['tag']}</div>
            </div>
        """, unsafe_allow_html=True)
        # Using a native button underneath for functionality
        if st.button("Select Option", key=f"select_{meals[i]['id']}"):
            st.session_state.choice = meals[i]['title']

# --- RESULT AREA ---
if 'choice' in st.session_state:
    st.write("---")
    st.success(f"**Excellent Choice.** Syncing ingredients for **{st.session_state.choice}**...")
    
    # Placeholders for the Multi-Item API Link
    st.link_button("🛒 One-Click to Walmart Cart", "https://www.walmart.com")
