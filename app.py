import streamlit as st
from datetime import date

from ai_engine import extract_basic_facts, find_missing_information
from timeline import build_timeline


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="WitnessAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #f5f7ff 0%, #eef7ff 45%, #f8f5ff 100%);
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Hero section */
.hero {
    padding: 35px 40px;
    border-radius: 28px;
    background: linear-gradient(135deg, #172554, #2563eb, #7c3aed);
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 15px 40px rgba(37, 99, 235, 0.25);
}

.hero h1 {
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
    color: #e0e7ff;
    margin-bottom: 0;
}

/* Feature cards */
.feature-card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.07);
    min-height: 145px;
}

.feature-icon {
    font-size: 32px;
}

.feature-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
    color: #172554;
}

.feature-text {
    font-size: 14px;
    color: #64748b;
}

/* Section title */
.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #172554;
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Fact cards */
.fact-card {
    background: white;
    border-radius: 18px;
    padding: 18px;
    border-left: 5px solid #2563eb;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06);
    margin-bottom: 12px;
}

.fact-title {
    font-weight: 700;
    color: #172554;
    font-size: 15px;
}

.fact-value {
    color: #475569;
    margin-top: 5px;
}

/* Timeline */
.timeline-card {
    background: white;
    padding: 18px 22px;
    margin: 12px 0;
    border-radius: 16px;
    border-left: 5px solid #7c3aed;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06);
}

.timeline-time {
    font-weight: 800;
    color: #7c3aed;
}

/* Missing info */
.warning-card {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    border-radius: 16px;
    padding: 18px;
    margin: 10px 0;
    color: #9a3412;
}

/* Privacy card */
.privacy-card {
    background: linear-gradient(135deg, #ecfdf5, #eff6ff);
    border: 1px solid #bfdbfe;
    padding: 25px;
    border-radius: 22px;
    margin-top: 30px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    padding: 35px 0 15px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🛡️ WitnessAI")

    st.markdown(
        """
        **Privacy-Preserving AI Digital Witness**

        Capture facts.  
        Reconstruct events.  
        Preserve privacy.
        """
    )

    st.divider()

    st.markdown("### 🔐 Privacy First")

    st.info(
        "WitnessAI is designed to minimize unnecessary exposure "
        "of sensitive incident information."
    )

    st.markdown("### ✨ Core Features")

    st.markdown("""
    📝 Incident Capture  
    🧠 Fact Extraction  
    ⏱️ Event Timeline  
    ⚠️ Missing Information  
    ✅ User Verification  
    🔒 Privacy-Aware Design
    """)

    st.divider()

    st.caption("WitnessAI • Prototype 2026")


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<h1>🛡️ WitnessAI</h1>

<p>
Privacy-Preserving AI Digital Witness
</p>

<p style="margin-top:12px;">
Capture facts • Reconstruct events • Preserve privacy
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRODUCTION
# =========================================================

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:20px;
box-shadow:0 6px 20px rgba(15,23,42,0.06);
margin-bottom:25px;
">

<h3 style="color:#172554;">📌 What is WitnessAI?</h3>

<p style="color:#475569;font-size:16px;">
WitnessAI helps users document important incidents by transforming
their description into structured factual information, an event
timeline, and a list of missing details.
</p>

<p style="color:#64748b;">
The system is designed to assist documentation and does not replace
emergency services, legal advice, or professional investigation.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FEATURE CARDS
# =========================================================

st.markdown(
    '<div class="section-title">✨ What WitnessAI Does</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <div class="feature-title">Capture</div>
        <div class="feature-text">
        Describe what happened in your own words.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Understand</div>
        <div class="feature-text">
        Extract important facts from the description.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⏱️</div>
        <div class="feature-title">Reconstruct</div>
        <div class="feature-text">
        Organize the incident into a timeline.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <div class="feature-title">Protect</div>
        <div class="feature-text">
        Keep the design privacy-focused.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# INCIDENT INPUT
# =========================================================

st.markdown(
    '<div class="section-title">📝 Document an Incident</div>',
    unsafe_allow_html=True
)

st.markdown(
    "Describe what happened using as much factual detail as you remember."
)

incident_text = st.text_area(
    "Incident description",
    height=190,
    placeholder=(
        "Example:\n"
        "Around 7:30 PM, I was near the college gate. "
        "I saw a motorcycle hit a parked car. "
        "There were two people on the motorcycle. "
        "The driver stopped after the collision."
    ),
    label_visibility="collapsed"
)

incident_date = st.date_input(
    "📅 Date of incident",
    value=date.today()
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🔍 Analyze Incident",
    type="primary",
    use_container_width=True
):

    if not incident_text.strip():

        st.warning(
            "⚠️ Please describe the incident before analyzing it."
        )

    else:

        with st.spinner("Analyzing incident..."):

            facts = extract_basic_facts(incident_text)

            missing = find_missing_information(facts)

            timeline = build_timeline(incident_text)


        st.success("✅ Incident analysis completed.")


        # =================================================
        # FACTS
        # =================================================

        st.markdown(
            '<div class="section-title">🧠 Extracted Facts</div>',
            unsafe_allow_html=True
        )

        fact_columns = st.columns(5)

        categories = [
            ("🕐", "Time", facts["time"]),
            ("📍", "Location", facts["location"]),
            ("👥", "People", facts["people"]),
            ("🚗", "Objects", facts["objects"]),
            ("⚡", "Events", facts["events"])
        ]

        for column, (icon, title, values) in zip(
            fact_columns,
            categories
        ):

            with column:

                if values:
                    value = ", ".join(values)
                else:
                    value = "Not provided"

                st.markdown(
                    f"""
                    <div class="fact-card">
                        <div style="font-size:26px;">{icon}</div>
                        <div class="fact-title">{title}</div>
                        <div class="fact-value">{value}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # =================================================
        # INCIDENT DATE
        # =================================================

        st.markdown(
            '<div class="section-title">📅 Incident Date</div>',
            unsafe_allow_html=True
        )

        st.info(
            f"Recorded incident date: **{incident_date.strftime('%d %B %Y')}**"
        )


        # =================================================
        # TIMELINE
        # =================================================

        st.markdown(
            '<div class="section-title">⏱️ Incident Timeline</div>',
            unsafe_allow_html=True
        )

        if timeline:

            for index, event in enumerate(timeline, start=1):

                st.markdown(
                    f"""
                    <div class="timeline-card">

                    <div class="timeline-time">
                    EVENT {index} • {event["time"]}
                    </div>

                    <div style="
                    margin-top:7px;
                    color:#475569;
                    font-size:15px;
                    ">
                    {event["description"]}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info("No timeline events were detected.")


        # =================================================
        # MISSING INFORMATION
        # =================================================

        st.markdown(
            '<div class="section-title">⚠️ Information That May Be Missing</div>',
            unsafe_allow_html=True
        )

        if missing:

            for item in missing:

                st.markdown(
                    f"""
                    <div class="warning-card">
                    ⚠️ <b>{item}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "The basic information categories were detected."
            )


        # =================================================
        # USER VERIFICATION
        # =================================================

        st.markdown(
            '<div class="section-title">✅ Verify Your Record</div>',
            unsafe_allow_html=True
        )

        st.checkbox(
            "I have reviewed the extracted information and understand that I should verify all details before using this record."
        )


        # =================================================
        # PRIVACY
        # =================================================

        st.markdown("""
        <div class="privacy-card">

        <h3>🔐 Privacy by Design</h3>

        <p style="color:#475569;">
        WitnessAI is designed around a privacy-first principle:
        sensitive incident information should not be unnecessarily
        exposed or shared.
        </p>

        <p style="color:#475569;">
        The current prototype demonstrates the documentation and
        verification workflow. Future versions will integrate
        dedicated on-device AI models for stronger local processing.
        </p>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown(
    '<div class="section-title">🚀 How WitnessAI Works</div>',
    unsafe_allow_html=True
)

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.markdown("""
    **01 — 📝 Capture**

    User describes the incident.
    """)

with step2:
    st.markdown("""
    **02 — 🧠 Analyze**

    Important facts are extracted.
    """)

with step3:
    st.markdown("""
    **03 — ⏱️ Reconstruct**

    Events are organized into a timeline.
    """)

with step4:
    st.markdown("""
    **04 — ✅ Verify**

    User reviews and verifies the information.
    """)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

🛡️ <b>WitnessAI</b> — Privacy-Preserving AI Digital Witness

<br>

Capture Facts • Reconstruct Events • Preserve Privacy

<br><br>

Prototype developed for the Snapdragon AI Lab Build & Present Challenge

</div>
""", unsafe_allow_html=True)
