# Show Services
st.subheader("Available Services")
if filtered_services:
    for idx, s in enumerate(filtered_services):
        st.write(f"**{s['service']}**")
        st.write(f"👨‍🔧 Provider: {s['name']}")
        st.write(f"💸 Price: {s['price']}")
        st.write(f"📍 DGPIN: {s['dgpin']}")
        st.write(f"📞 Contact: {s['contact']}")

        # Show feedbacks + average rating
        if s['service'] in st.session_state["feedbacks"]:
            feedback_list = st.session_state["feedbacks"][s['service']]
            if feedback_list:
                avg_rating = sum(fb['rating'] for fb in feedback_list) / len(feedback_list)
                stars = "⭐" * int(round(avg_rating))  # star display
                st.write(f"⭐ Average Rating: {avg_rating:.1f}/5 {stars}")
                st.write("💬 Feedback:")
                for fb in feedback_list:
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
