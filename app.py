import streamlit as st
from datetime import datetime

from ai_engine import extract_basic_facts, find_missing_information


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="WitnessAI",
    page_icon="🛡️",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("🛡️ WitnessAI")

st.subheader(
    "Privacy-Preserving AI Digital Witness"
)

st.write(
    "Capture, organize and verify factual information "
    "about an incident."
)

st.info(
    "WitnessAI is a documentation assistant. "
    "It does not replace emergency services, legal advice, "
    "or professional investigation."
)


# -----------------------------
# Incident Input
# -----------------------------

st.header("📝 Describe the Incident")

incident_text = st.text_area(
    "What happened?",
    placeholder=(
        "Example: Around 7:30 PM, I was near the college gate. "
        "I saw a motorcycle hit a parked car. "
        "There were two people on the motorcycle."
    ),
    height=200
)


incident_date = st.date_input(
    "Date of incident",
    value=datetime.today()
)


# -----------------------------
# Analyze Button
# -----------------------------

if st.button("🔍 Analyze Incident", type="primary"):

    if not incident_text.strip():

        st.warning(
            "Please describe the incident before analyzing it."
        )

    else:

        # Extract basic facts
        facts = extract_basic_facts(incident_text)

        # Find missing information
        missing = find_missing_information(facts)

        st.success(
            "Incident analyzed successfully."
        )

        # -----------------------------
        # Extracted Facts
        # -----------------------------

        st.header("📋 Extracted Information")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📅 Date")

            st.write(
                str(incident_date)
            )

            st.subheader("🕐 Time")

            if facts["time"]:
                for item in facts["time"]:
                    st.write("•", item)
            else:
                st.write("Not provided")

            st.subheader("📍 Location")

            if facts["location"]:
                for item in facts["location"]:
                    st.write("•", item)
            else:
                st.write("Not provided")

        with col2:

            st.subheader("👥 People")

            if facts["people"]:
                for item in facts["people"]:
                    st.write("•", item)
            else:
                st.write("Not provided")

            st.subheader("🚗 Objects / Vehicles")

            if facts["objects"]:
                for item in facts["objects"]:
                    st.write("•", item)
            else:
                st.write("Not provided")

            st.subheader("⚡ Events")

            if facts["events"]:
                for item in facts["events"]:
                    st.write("•", item)
            else:
                st.write("Not provided")


        # -----------------------------
        # Missing Information
        # -----------------------------

        st.header("⚠️ Missing Information")

        if missing:

            st.write(
                "The following information was not identified "
                "in the description:"
            )

            for item in missing:
                st.write("•", item)

        else:

            st.success(
                "No major missing information was detected "
                "by the current extraction layer."
            )


        # -----------------------------
        # User Verification
        # -----------------------------

        st.header("✅ User Verification")

        st.checkbox(
            "I have reviewed the extracted information."
        )

        st.caption(
            "The extracted information should be verified "
            "by the user before creating a final report."
        )


        # -----------------------------
        # Current Status
        # -----------------------------

        st.header("🚧 AI Development Status")

        st.info(
            "The current version uses a basic local fact-extraction "
            "layer. A dedicated AI model will be integrated in "
            "the next development stage."
        )
