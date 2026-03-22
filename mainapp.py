import streamlit as st

# Page setup
st.set_page_config(page_title="Neighbor-Tech Support", page_icon="💻", layout="wide")

st.title("Neighbor-Tech Support")
st.write("Find affordable tech help right in your neighborhood!")

# Storage for services and feedbacks
if "services" not in st.session_state:
    st.session_state["services"] = []
if "feedbacks" not in st.session_state:
    st.session_state["feedbacks"] = {}

# --- Registration Form ---
st.header("📝 Register as a Service Provider")
with st.form("register_form", clear_on_submit=True):  # <-- clears form after submit
    name = st.text_input("Your Name")
    service = st.text_input("Service Offered")
    price = st.text_input("Price (₹)")
    dgpin = st.text_input("DGPIN Code")
    contact = st.text_input("Contact Number")
    submitted = st.form_submit_button("Register Service")
    if submitted and name and service and price and dgpin and contact:
        st.session_state["services"].append({
            "name": name,
            "service": service,
            "price": price,
            "dgpin": dgpin,
            "contact": contact
        })
        st.success(f"✅ {service} registered successfully!")

# --- Search & Location Filter ---
st.header("🔍 Find Services")
user_dgpin = st.text_input("Enter your DGPIN to search nearby services")
search_query = st.text_input("Search for a service")

filtered_services = []
for s in st.session_state["services"]:
    if (not search_query or search_query.lower() in s["service"].lower()):
        if (not user_dgpin or user_dgpin == s["dgpin"]):  # simple filter: same DGPIN
            filtered_services.append(s)

# --- Show Services ---
st.subheader("Available Services")
if filtered_services:
    for idx, s in enumerate(filtered_services):
        st.write(f"**{s['service']}**")
        st.write(f"👨‍🔧 Provider: {s['name']}")
        st.write(f"💸 Price: {s['price']}")
        st.write(f"📍 DGPIN: {s['dgpin']}")
        st.write(f"📞 Contact: {s['contact']}")

        # Show feedbacks if any
        if s['service'] in st.session_state["feedbacks"]:
            st.write("⭐ Feedback:")
            for fb in st.session_state["feedbacks"][s['service']]:
                st.write(f"- {fb['rating']} stars: {fb['comment']}")

        if st.button(f"Book Now - {s['service']}", key=f"book_{idx}"):
            st.success(f"✅ You booked {s['service']} from {s['name']}!")
            st.info(f"📞 Contact Number: {s['contact']}")

            # Feedback form
            rating = st.slider("Rate the service (1-5)", 1, 5, key=f"rating_{idx}")
            feedback = st.text_area("Leave feedback", key=f"fb_{idx}")
            if st.button("Submit Feedback", key=f"feedback_{idx}"):
                if s['service'] not in st.session_state["feedbacks"]:
                    st.session_state["feedbacks"][s['service']] = []
                st.session_state["feedbacks"][s['service']].append({
                    "rating": rating,
                    "comment": feedback
                })
                st.success("Thank you for your feedback!")
else:
    st.warning("No services found. Try registering or searching with another DGPIN.")
