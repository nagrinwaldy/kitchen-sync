import streamlit as st

st.set_page_config(page_title="KitchenSync", page_icon="🍳")
st.title("🍳 KitchenSync")

meal_choice = st.text_input("What are we eating this week?", "Chicken and Broccoli")

if st.button("Sync to Cart"):
    # Using a real ID for Whole Milk (10450114) for testing
    items = [
        {"name": "Whole Milk", "id": "10450118", "qty": 1}, 
    ]
    
    # Try the 'checkout' redirect pattern
    # It’s often more reliable for external deep-linking
    base_url = "https://www.walmart.com/cart/checkout?items="
    item_strings = [f"{item['id']}:{item['qty']}" for item in items]
    final_url = base_url + ",".join(item_strings)
    
    st.success("Test: Syncing 1 Gallon of Milk...")
    st.link_button("🛒 Open Walmart Cart", final_url)
