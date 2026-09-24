import streamlit as st
from datetime import datetime

from ai_engine import extract_basic_facts, find_missing_information
from timeline import build_timeline


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
        "There were two people on the motorcycle. "
        "The driver stopped after the collision."
    ),
    height=200
)

incident_date = st.date_input(
    "Date of incident",
    value=datetime.today()
)


# -----------------------------
# Analyze Incident
# -----------------------------

if st.button("🔍 Analyze Incident", type="primary"):

    if not incident_text.strip():

        st.warning(
            "Please describe the incident before analyzing it."
        )

    else:

        # -----------------------------
        # Fact Extraction
        # -----------------------------

        facts = extract_basic_facts(
            incident_text
        )

        # -----------------------------
        # Missing Information
        # -----------------------------

        missing = find_missing_information(
            facts
        )

        # -----------------------------
        # Timeline
        # -----------------------------

        timeline = build_timeline(
            incident_text
        )

        st.success(
            "Incident analyzed successfully."
        )

        # -----------------------------
        # Extracted Information
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
        # Timeline
        # -----------------------------

        st.header("🕐 Incident Timeline")

        if timeline:

            for index, event in enumerate(
                timeline,
                start=1
            ):

                st.markdown(
                    f"**{index}. {event['time']}**"
                )

                st.write(
                    event["description"]
                )

                st.divider()

        else:

            st.write(
                "No timeline events could be identified."
            )


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

                st.write(
                    "•", item
                )

        else:

            st.success(
                "No major missing information was detected."
            )


        # -----------------------------
        # User Verification
        # -----------------------------

        st.header("✅ User Verification")

        verified = st.checkbox(
            "I have reviewed the extracted information."
        )

        if verified:

            st.success(
                "Information marked as reviewed by the user."
            )

        st.caption(
            "The user should verify all extracted information "
            "before creating a final incident report."
        )


        # -----------------------------
        # AI Development Status
        # -----------------------------

        st.header("🚧 Current Development Stage")

        st.info(
            "The current version contains a basic local "
            "fact-extraction and timeline layer. "
            "A dedicated AI model will be integrated in "
            "the next stage."
        )
