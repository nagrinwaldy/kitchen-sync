import streamlit as st

# Page Branding & Neutral Theme
st.set_page_config(page_title="KitchenSync", page_icon="🍳", layout="wide")

# Bulletproof Neutral CSS (Works for Light & Dark)
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

# --- HEADER ---
st.markdown('# 🍳 KitchenSync')
st.markdown('### Wellness. Savings. Time. | Supporting Sheboygan County')

st.write("---")

# --- MEAL DISCOVERY SECTION ---
st.header("Suggested for You")
st.write("AI-curated meals based on local availability and peak nutrition.")

col1, col2, col3 = st.columns(3)

# Mock Data for Discovery
meals = [
    {"title": "Lemon Herb Roast Chicken", "desc": "High Protein | 25 min prep", "savings": "$4.50"},
    {"title": "Quinoa & Black Bean Power Bowls", "desc": "Fiber Rich | 15 min prep", "savings": "$2.10"},
    {"title": "Pan-Seared Salmon & Asparagus", "desc": "Omega-3 Focus | 20 min prep", "savings": "$3.80"}
]

for i, col in enumerate([col1, col2, col3]):
    with col:
        st.markdown(f"""
            <div class="option-card">
                <h3>{meals[i]['title']}</h3>
                <p>{meals[i]['desc']}</p>
                <p class="metric-text">Potential Savings: {meals[i]['savings']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Select Option {i+1}", key=f"btn_{i}"):
            st.session_state.selected_meal = meals[i]['title']
            st.balloons()

# --- THE EXECUTION ---
if 'selected_meal' in st.session_state:
    st.write("---")
    st.success(f"**Excellent Choice!** Syncing ingredients for **{st.session_state.selected_meal}** to your Walmart cart...")
    
    # Placeholder for the future Walmart Link
    st.link_button("🛒 Finalize & Add to Walmart Cart", "https://www.walmart.com/cart")
