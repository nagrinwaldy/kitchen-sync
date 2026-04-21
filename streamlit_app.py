import streamlit as st

st.set_page_config(page_title="KitchenSync", page_icon="🍳")
st.title("🍳 KitchenSync")

meal_choice = st.text_input("What are we eating this week?", "Chicken and Broccoli")

if st.button("Sync to Cart"):
    # REPLACE THIS ID with the one you found in Step 2 above
    # Example ID for Milk: 10450114
    test_id = "10450118" 
    
    # Use the 'Affiliate Bridge' URL pattern
    # Pattern: https://affil.walmart.com/cart/add-items?items=[ID]_[QTY]
    final_url = f"https://affil.walmart.com/cart/add-items?items={test_id}_1"
    
    st.success("Redirect link prepared!")
    st.link_button("🛒 Push to Walmart Cart", final_url)
