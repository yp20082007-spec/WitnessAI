import streamlit as st
from datetime import date

from ai_engine import extract_basic_facts, find_missing_information
from timeline import build_timeline


# =========================================================
# PAGE
# =========================================================

st.set_page_config(
    page_title="WitnessAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# COLORFUL UI
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #faf9fc;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ================= HERO ================= */

.hero {
    background: linear-gradient(
        135deg,
        #ddd4f7,
        #cfc3f2,
        #e5dff8
    );

    padding: 42px 45px;
    border-radius: 30px;

    border: 1px solid #d4c9ef;

    box-shadow: 0 12px 30px rgba(105, 85, 150, 0.12);

    margin-bottom: 28px;
}

.hero h1 {
    color: #51406f;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #66577d;
    font-size: 20px;
}

.hero-tagline {
    color: #74678a;
    font-size: 15px;
    margin-top: 14px;
}


/* ================= SECTION TITLE ================= */

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #4c5263;

    margin-top: 32px;
    margin-bottom: 18px;
}


/* ================= INTRO ================= */

.intro-card {
    background: linear-gradient(
        135deg,
        #ffeaf2,
        #f9e8f1
    );

    padding: 28px;

    border-radius: 24px;

    border: 1px solid #f0cedc;

    box-shadow: 0 8px 22px rgba(150, 90, 110, 0.07);
}

.intro-title {
    color: #8a526b;
    font-size: 27px;
    font-weight: 800;
}

.intro-text {
    color: #735f69;
    font-size: 15px;
    line-height: 1.7;
}


/* ================= FEATURE CARDS ================= */

.feature-card {
    padding: 24px;

    border-radius: 22px;

    min-height: 165px;

    border: 1px solid rgba(0,0,0,0.05);

    box-shadow: 0 8px 20px rgba(60,60,70,0.07);

    transition: transform .2s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

.feature-icon {
    font-size: 34px;
}

.feature-title {
    font-size: 18px;
    font-weight: 800;
    margin-top: 9px;
}

.feature-text {
    font-size: 13px;
    margin-top: 8px;
    line-height: 1.5;
}


/* INDIVIDUAL COLORS */

.capture-card {
    background: #e8f4ff;
    color: #426987;
}

.ai-card {
    background: #e9f7ef;
    color: #4e7661;
}

.timeline-feature {
    background: #fff0e6;
    color: #8a654f;
}

.privacy-feature {
    background: #f3edff;
    color: #66558a;
}


/* ================= INPUT ================= */

.input-card {
    background: #eaf5ff;

    padding: 25px;

    border-radius: 23px;

    border: 1px solid #cfe5f7;

    margin-top: 10px;
}


/* ================= FACT CARDS ================= */

.fact-card {
    padding: 20px;

    border-radius: 19px;

    min-height: 135px;

    box-shadow: 0 6px 18px rgba(60,60,70,0.06);

    border: 1px solid rgba(0,0,0,0.04);
}

.fact-time {
    background: #eee8ff;
}

.fact-location {
    background: #e7f4ff;
}

.fact-people {
    background: #e9f8ef;
}

.fact-object {
    background: #fff0e7;
}

.fact-event {
    background: #fff8d9;
}

.fact-title {
    font-weight: 800;
    margin-top: 8px;
}

.fact-value {
    font-size: 14px;
    margin-top: 6px;
    color: #667085;
}


/* ================= TIMELINE ================= */

.timeline-card {
    background: #fff0e5;

    padding: 20px 23px;

    margin: 12px 0;

    border-radius: 18px;

    border-left: 5px solid #e5a875;

    box-shadow: 0 6px 18px rgba(120,80,50,0.06);
}

.timeline-time {
    color: #9b6841;
    font-weight: 800;
}

.timeline-description {
    color: #6f6259;
    margin-top: 7px;
}


/* ================= WARNING ================= */

.warning-card {
    background: #fff7cf;

    border: 1px solid #eadb8b;

    color: #806d24;

    padding: 17px;

    margin: 9px 0;

    border-radius: 17px;
}


/* ================= VERIFICATION ================= */

.verify-card {
    background: #eee8ff;

    border: 1px solid #d9ccf5;

    padding: 23px;

    border-radius: 21px;

    color: #63537f;
}


/* ================= PRIVACY ================= */

.privacy-card {
    background: linear-gradient(
        135deg,
        #e4f7ed,
        #e9f8f4
    );

    border: 1px solid #cce8da;

    padding: 28px;

    border-radius: 23px;

    margin-top: 30px;
}

.privacy-title {
    color: #4b765e;
    font-size: 23px;
    font-weight: 800;
}

.privacy-text {
    color: #5f7168;
    line-height: 1.7;
}


/* ================= HOW IT WORKS ================= */

.step-card {
    padding: 22px;

    border-radius: 20px;

    min-height: 130px;

    box-shadow: 0 6px 18px rgba(60,60,70,0.06);
}

.step1 {
    background: #e7f3ff;
}

.step2 {
    background: #e9f7ef;
}

.step3 {
    background: #fff0e5;
}

.step4 {
    background: #eee8ff;
}


/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #f1edfa,
        #f8eef4
    );
}

.sidebar-title {
    color: #57466f;
    font-size: 23px;
    font-weight: 800;
}


/* ================= BUTTON ================= */

.stButton > button {
    border-radius: 14px;

    background: linear-gradient(
        135deg,
        #cbb9ed,
        #e0b9cf
    );

    color: #51425f;

    border: none;

    font-weight: 800;

    padding: 12px;

    box-shadow: 0 6px 15px rgba(120,90,140,0.12);
}

.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #bda8e5,
        #d9a9c3
    );
}


/* ================= FOOTER ================= */

.footer {
    text-align: center;

    color: #8a8492;

    padding: 45px 0 20px;

    font-size: 13px;
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

    st.markdown("""
    **Privacy-Preserving AI Digital Witness**

    Capture facts.

    Reconstruct events.

    Preserve privacy.
    """)

    st.divider()

    st.markdown("### 🔐 Privacy First")

    st.info(
        "Designed to minimize unnecessary exposure "
        "of sensitive incident information."
    )

    st.markdown("### ✨ Features")

    st.markdown("""
    📝 Incident Capture

    🧠 Fact Extraction

    ⏱️ Event Timeline

    ⚠️ Missing Information

    ✅ Verification

    🔒 Privacy
    """)

    st.divider()

    st.caption("WitnessAI • 2026")


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
Capture facts &nbsp;•&nbsp;
Reconstruct events &nbsp;•&nbsp;
Preserve privacy
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRO
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

The system assists documentation and does not replace emergency
services, legal advice, or professional investigation.

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

feature_data = [
    (
        "capture-card",
        "📝",
        "Capture",
        "Describe the incident in your own words."
    ),

    (
        "ai-card",
        "🧠",
        "Understand",
        "Extract important factual information."
    ),

    (
        "timeline-feature",
        "⏱️",
        "Reconstruct",
        "Organize events into a timeline."
    ),

    (
        "privacy-feature",
        "🔒",
        "Protect",
        "Follow a privacy-first documentation approach."
    )
]

for column, item in zip(
    [c1, c2, c3, c4],
    feature_data
):

    css_class, icon, title, text = item

    with column:

        st.markdown(
            f"""
            <div class="feature-card {css_class}">

            <div class="feature-icon">
            {icon}
            </div>

            <div class="feature-title">
            {title}
            </div>

            <div class="feature-text">
            {text}
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

st.markdown("""
<div class="input-card">

<b>Tell WitnessAI what happened.</b>

<br><br>

Describe the incident using the factual details you remember.

</div>
""", unsafe_allow_html=True)

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
            "⚠️ Please describe the incident first."
        )

    else:

        with st.spinner("Analyzing incident..."):

            facts = extract_basic_facts(incident_text)

            missing = find_missing_information(facts)

            timeline = build_timeline(incident_text)

        st.success("✅ Incident analysis completed!")


        # =================================================
        # FACTS
        # =================================================

        st.markdown(
            '<div class="section-title">🧠 Extracted Facts</div>',
            unsafe_allow_html=True
        )

        fact_columns = st.columns(5)

        categories = [
            ("fact-time", "🕐", "Time", facts["time"]),
            ("fact-location", "📍", "Location", facts["location"]),
            ("fact-people", "👥", "People", facts["people"]),
            ("fact-object", "🚗", "Objects", facts["objects"]),
            ("fact-event", "⚡", "Events", facts["events"])
        ]

        for column, item in zip(
            fact_columns,
            categories
        ):

            css_class, icon, title, values = item

            with column:

                value = (
                    ", ".join(values)
                    if values
                    else "Not provided"
                )

                st.markdown(
                    f"""
                    <div class="fact-card {css_class}">

                    <div style="font-size:28px;">
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
            f"Recorded date: "
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
        # MISSING
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

        st.markdown("""
        <div class="verify-card">

        <b>Before using this record:</b>

        <br><br>

        Review the extracted information and make sure
        the details accurately represent what you remember.

        </div>
        """, unsafe_allow_html=True)

        st.checkbox(
            "I have reviewed the information and will verify all details."
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

        WitnessAI follows a privacy-first approach for
        sensitive incident documentation.

        <br><br>

        The current prototype demonstrates the documentation
        and verification workflow. Future versions will integrate
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

steps = [
    ("step-card step1", "01", "📝 Capture",
     "User describes the incident."),

    ("step-card step2", "02", "🧠 Analyze",
     "Important facts are extracted."),

    ("step-card step3", "03", "⏱️ Reconstruct",
     "Events become a timeline."),

    ("step-card step4", "04", "✅ Verify",
     "User reviews the record.")
]

for column, step in zip(
    [s1, s2, s3, s4],
    steps
):

    css, number, title, text = step

    with column:

        st.markdown(
            f"""
            <div class="{css}">

            <div style="
                font-size:14px;
                font-weight:800;
                opacity:0.65;
            ">
            STEP {number}
            </div>

            <h4>
            {title}
            </h4>

            <div>
            {text}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


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
