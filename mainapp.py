import streamlit as st

st.set_page_config(page_title="Neighbor-Tech Support", page_icon="💻", layout="wide")

st.title("Neighbor-Tech Support")
st.write("Find affordable tech help right in your neighborhood!")

# Sample services
services = [
    {"name": "Windows Update", "provider": "Ravi Kumar", "price": "₹500"},
    {"name": "Screen Guard Installation", "provider": "Anita Sharma", "price": "₹150"},
    {"name": "Laptop Cleaning", "provider": "Suresh Patil", "price": "₹300"},
]

# Search bar
search_query = st.text_input("🔍 Search for a service")

# Filter services
if search_query:
    filtered = [s for s in services if search_query.lower() in s["name"].lower()]
else:
    filtered = services

# Show services
for service in filtered:
    st.subheader(service["name"])
    st.write(f"👨‍🔧 Provider: {service['provider']}")
    st.write(f"💸 Price: {service['price']}")
    if st.button(f"Book Now - {service['name']}"):
        st.success(f"✅ You booked {service['name']} from {service['provider']}!")
