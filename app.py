import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="WitnessAI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------

st.title("🛡️ WitnessAI")
st.subheader("Privacy-Preserving AI Digital Witness")

st.write(
    "Capture, organize and verify factual information about an incident."
)

st.info(
    "WitnessAI is designed to assist with documentation. "
    "It does not replace emergency services, legal advice, or professional investigation."
)

# -----------------------------
# Incident Input
# -----------------------------

st.header("Describe the Incident")

incident_text = st.text_area(
    "What happened?",
    placeholder=(
        "Describe the incident in your own words. "
        "Include any details you remember such as time, location, "
        "people, objects and sequence of events."
    ),
    height=200
)

incident_date = st.date_input(
    "Date of incident",
    value=datetime.today()
)

if st.button("Analyze Incident", type="primary"):

    if not incident_text.strip():
        st.warning("Please describe the incident first.")

    else:
        st.success("Incident received successfully.")

        st.header("Incident Information")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📅 Date")
            st.write(str(incident_date))

        with col2:
            st.subheader("📝 User Description")
            st.write(incident_text)

        st.header("AI Analysis")

        st.info(
            "AI analysis will be connected in the next development stage."
        )

        st.header("Timeline")

        st.write(
            "Timeline generation will be added after the AI fact-extraction module."
        )

        st.header("Missing Information")

        st.write(
            "Missing-detail detection will be added in the next stage."
        )

        st.header("Incident Report")

        st.write(
            "The verified structured report will be generated here."
        )
