import streamlit as st
from datetime import date

from ai_engine import extract_basic_facts, find_missing_information
from timeline import build_timeline


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="WitnessAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SOFT PASTEL DESIGN
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        linear-gradient(
            135deg,
            #f7faf8 0%,
            #f5f7fb 45%,
            #faf7fb 100%
        );
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    padding: 38px 45px;
    border-radius: 28px;

    background:
        linear-gradient(
            120deg,
            #dfeee7,
            #e7e3f5,
            #dfeef4
        );

    border: 1px solid #d9e3df;

    box-shadow:
        0 15px 35px rgba(60, 70, 80, 0.08);

    margin-bottom: 28px;
}

.hero h1 {
    font-size: 46px;
    font-weight: 800;
    color: #354052;
    margin-bottom: 6px;
}

.hero-subtitle {
    font-size: 19px;
    color: #667085;
}

.hero-tagline {
    font-size: 15px;
    color: #6f7185;
    margin-top: 14px;
}


/* =========================================================
   INTRO CARD
   ========================================================= */

.intro-card {
    background: #ffffff;

    padding: 28px;

    border-radius: 22px;

    border: 1px solid #e7e9ee;

    box-shadow:
        0 8px 25px rgba(60, 70, 80, 0.06);

    margin-bottom: 30px;
}

.intro-title {
    color: #465266;
    font-size: 27px;
    font-weight: 750;
}

.intro-text {
    color: #687386;
    font-size: 15px;
    line-height: 1.7;
}


/* =========================================================
   SECTION TITLE
   ========================================================= */

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #465266;

    margin-top: 32px;
    margin-bottom: 18px;
}


/* =========================================================
   FEATURE CARDS
   ========================================================= */

.feature-card {

    background: rgba(255,255,255,0.92);

    padding: 22px;

    border-radius: 20px;

    border: 1px solid #e5e8ec;

    box-shadow:
        0 7px 22px rgba(70,80,90,0.06);

    min-height: 150px;

    transition: transform 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
}

.feature-icon {
    font-size: 30px;
}

.feature-title {
    font-size: 17px;
    font-weight: 750;

    color: #4d5868;

    margin-top: 8px;
}

.feature-text {
    font-size: 13px;

    color: #7a8391;

    margin-top: 7px;

    line-height: 1.5;
}


/* =========================================================
   FACT CARDS
   ========================================================= */

.fact-card {

    background: #ffffff;

    padding: 19px;

    border-radius: 18px;

    border: 1px solid #e6e8ec;

    box-shadow:
        0 6px 18px rgba(60,70,80,0.05);

    min-height: 120px;
}

.fact-title {
    font-weight: 700;
    color: #566174;

    margin-top: 7px;
}

.fact-value {
    color: #7a8391;

    font-size: 14px;

    margin-top: 5px;
}


/* =========================================================
   TIMELINE
   ========================================================= */

.timeline-card {

    background: #ffffff;

    padding: 20px 23px;

    margin: 13px 0;

    border-radius: 18px;

    border-left: 5px solid #a99bc7;

    box-shadow:
        0 6px 18px rgba(70,70,80,0.05);
}

.timeline-time {
    font-weight: 800;

    color: #8174a5;

    font-size: 14px;
}

.timeline-description {
    color: #697386;

    margin-top: 7px;

    line-height: 1.6;
}


/* =========================================================
   WARNING
   ========================================================= */

.warning-card {

    background: #fffaf1;

    border: 1px solid #f1dfb8;

    border-radius: 16px;

    padding: 17px;

    margin: 9px 0;

    color: #866d3d;
}


/* =========================================================
   PRIVACY
   ========================================================= */

.privacy-card {

    background:
        linear-gradient(
            135deg,
            #edf7f2,
            #f1eef8
        );

    border: 1px solid #d8e4df;

    padding: 27px;

    border-radius: 22px;

    margin-top: 30px;
}

.privacy-title {
    color: #53655d;

    font-size: 22px;

    font-weight: 750;
}

.privacy-text {
    color: #68766f;

    line-height: 1.7;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #f1f5f3,
            #f5f2f7
        );

    border-right: 1px solid #e1e5e3;
}

.sidebar-title {
    color: #4d5868;

    font-size: 22px;

    font-weight: 800;
}

.sidebar-text {
    color: #737d89;

    line-height: 1.6;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    text-align: center;

    color: #8a929e;

    padding: 40px 0 20px;

    font-size: 13px;
}


/* =========================================================
   BUTTON
   ========================================================= */

.stButton > button {

    border-radius: 12px;

    border: 1px solid #cfd8d3;

    background:
        linear-gradient(
            135deg,
            #dbece4,
            #e6e0f2
        );

    color: #4d5965;

    font-weight: 700;

    padding: 11px 20px;

    transition: all 0.2s ease;
}

.stButton > button:hover {

    border-color: #b7c8c0;

    background:
        linear-gradient(
            135deg,
            #d3e6dd,
            #ddd5eb
        );

    transform: translateY(-1px);
}


/* =========================================================
   TEXT AREA
   ========================================================= */

textarea {

    border-radius: 16px !important;

    border: 1px solid #dfe3e7 !important;

    background: #ffffff !important;
}


/* =========================================================
   DIVIDER
   ========================================================= */

hr {
    border-color: #e6e8eb;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🛡️ WitnessAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-text">

        <b>Privacy-Preserving AI Digital Witness</b>

        <br><br>

        Capture facts.<br>
        Reconstruct events.<br>
        Preserve privacy.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🔐 Privacy First")

    st.info(
        "WitnessAI is designed to minimize unnecessary "
        "exposure of sensitive incident information."
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

<div class="hero-subtitle">
Privacy-Preserving AI Digital Witness
</div>

<div class="hero-tagline">
Capture facts&nbsp;&nbsp;•&nbsp;&nbsp;
Reconstruct events&nbsp;&nbsp;•&nbsp;&nbsp;
Preserve privacy
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRODUCTION
# =========================================================

st.markdown("""
<div class="intro-card">

<div class="intro-title">
📌 What is WitnessAI?
</div>

<br>

<div class="intro-text">

WitnessAI helps users document important incidents by transforming
their description into structured factual information, an event
timeline, and a list of missing details.

<br><br>

The system is designed to assist documentation and does not replace
emergency services, legal advice, or professional investigation.

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">✨ What WitnessAI Does</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

features = [
    (
        "📝",
        "Capture",
        "Describe what happened using your own words."
    ),
    (
        "🧠",
        "Understand",
        "Extract important factual information."
    ),
    (
        "⏱️",
        "Reconstruct",
        "Organize events into a clear timeline."
    ),
    (
        "🔒",
        "Protect",
        "Follow a privacy-first documentation approach."
    )
]

for column, feature in zip(
    [c1, c2, c3, c4],
    features
):

    icon, title, description = feature

    with column:

        st.markdown(
            f"""
            <div class="feature-card">

            <div class="feature-icon">{icon}</div>

            <div class="feature-title">
            {title}
            </div>

            <div class="feature-text">
            {description}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


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
# ANALYZE
# =========================================================

if st.button(
    "🔍 Analyze Incident",
    type="primary",
    use_container_width=True
):

    if not incident_text.strip():

        st.warning(
            "Please describe the incident before analyzing it."
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

                value = (
                    ", ".join(values)
                    if values
                    else "Not provided"
                )

                st.markdown(
                    f"""
                    <div class="fact-card">

                    <div style="font-size:27px;">
                    {icon}
                    </div>

                    <div class="fact-title">
                    {title}
                    </div>

                    <div class="fact-value">
                    {value}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # =================================================
        # DATE
        # =================================================

        st.markdown(
            '<div class="section-title">📅 Incident Date</div>',
            unsafe_allow_html=True
        )

        st.info(
            f"Recorded incident date: "
            f"**{incident_date.strftime('%d %B %Y')}**"
        )


        # =================================================
        # TIMELINE
        # =================================================

        st.markdown(
            '<div class="section-title">⏱️ Incident Timeline</div>',
            unsafe_allow_html=True
        )

        for index, event in enumerate(
            timeline,
            start=1
        ):

            st.markdown(
                f"""
                <div class="timeline-card">

                <div class="timeline-time">
                EVENT {index} • {event["time"]}
                </div>

                <div class="timeline-description">
                {event["description"]}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # =================================================
        # MISSING INFORMATION
        # =================================================

        st.markdown(
            '<div class="section-title">'
            '⚠️ Information That May Be Missing'
            '</div>',
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
                "All basic information categories were detected."
            )


        # =================================================
        # VERIFICATION
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

        <div class="privacy-title">
        🔐 Privacy by Design
        </div>

        <br>

        <div class="privacy-text">

        WitnessAI is designed around a privacy-first principle:
        sensitive incident information should not be unnecessarily
        exposed or shared.

        <br><br>

        The current prototype demonstrates the documentation and
        verification workflow. Future versions will integrate
        dedicated on-device AI models for stronger local processing.

        </div>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown(
    '<div class="section-title">🚀 How WitnessAI Works</div>',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    **01 — 📝 Capture**

    User describes the incident.
    """)

with s2:
    st.markdown("""
    **02 — 🧠 Analyze**

    Important facts are extracted.
    """)

with s3:
    st.markdown("""
    **03 — ⏱️ Reconstruct**

    Events are organized into a timeline.
    """)

with s4:
    st.markdown("""
    **04 — ✅ Verify**

    User reviews the generated record.
    """)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

🛡️ <b>WitnessAI</b>

<br>

Privacy-Preserving AI Digital Witness

<br><br>

Capture Facts • Reconstruct Events • Preserve Privacy

<br><br>

Prototype • 2026

</div>
""", unsafe_allow_html=True)
