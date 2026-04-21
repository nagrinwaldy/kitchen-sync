import streamlit as st

# Page Branding
st.set_page_config(page_title="KitchenSync | Sheboygan", page_icon="🍳", layout="wide")

# --- DYNAMIC ADAPTIVE CSS ---
st.markdown("""
    <style>
    /* Default (Light Mode) Variables */
    :root {
        --bg-color: #FDFBF7;
        --card-bg: #FFFFFF;
        --text-main: #2D5A27;
        --text-sub: #666666;
        --border-color: #EAEAEA;
    }

    /* Dark Mode Variables */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #121212;
            --card-bg: #1E1E1E;
            --text-main: #81C784; /* A lighter green for dark backgrounds */
            --text-sub: #BBBBBB;
            --border-color: #333333;
        }
    }

    .stApp { background-color: var(--bg-color); }
    
    .main-header { 
        color: var(--text-main); 
        font-size: 42px; 
        font-weight: 800; 
    }
    
    .sub-text { 
        color: var(--text-sub); 
        font-size: 18px; 
    }

    .card {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        color: var(--text-sub);
        margin-bottom: 10px;
    }
    
    b { color: var(--text-main); } /* Ensures bold text stays visible */
    </style>
""", unsafe_allow_html=True)

# --- RE-APPLYING THE LAYOUT ---
st.markdown('<p class="main-header">🍳 KitchenSync</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Intelligent meal planning for the Sheboygan community.</p>', unsafe_allow_html=True)

# Side-by-side metrics
m1, m2, m3 = st.columns(3)
m1.metric("Wellness Score", "94%")
m2.metric("Savings", "$12.40")
m3.metric("Charity Earned", "$3.10")

st.write("---")

# Demo Card
st.markdown("""
<div class="card">
    <p><b>Current Logic: Adaptive Mode Active</b><br>
    This card will now flip colors automatically based on your phone or computer settings.</p>
</div>
""", unsafe_allow_html=True)
