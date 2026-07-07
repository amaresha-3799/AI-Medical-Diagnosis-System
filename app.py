import streamlit as st
from Utils.Agents import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam

# Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="AI Medical Diagnosis System",
    page_icon="🩺",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }
    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #2563eb 100%);
        padding: 1.5rem 1.5rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 1rem;
    }
    .card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1rem 1rem;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06);
    }
    .stButton > button {
        border-radius: 999px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("🩺 AI Doctor System")
st.sidebar.write("Upload medical reports and receive AI specialist analysis in a polished workspace.")
st.sidebar.divider()
st.sidebar.caption("This view only changes the interface presentation.")

# Main content
st.markdown(
    """
    <div class="hero-box">
        <h1 style="margin:0; font-size:2rem;">AI Medical Diagnosis System</h1>
        <p style="margin:0.35rem 0 0; font-size:1rem; opacity:0.95;">Upload a medical report and let medical specialists analyze it with AI.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("Choose a text report and review the findings in a cleaner, structured layout.")

uploaded_file = st.file_uploader(
    "Upload Medical Report (.txt)",
    type=["txt"],
    help="Upload a plain text medical report to analyze.",
)

if uploaded_file is not None:
    medical_report = uploaded_file.read().decode("utf-8")

    col1, col2 = st.columns([1.4, 0.8])
    with col1:
        st.markdown("<div class='card'><h4>Medical Report Preview</h4></div>", unsafe_allow_html=True)
        st.text_area("", medical_report, height=220, disabled=True)
    with col2:
        st.markdown("<div class='card'><h4>Report Details</h4></div>", unsafe_allow_html=True)
        st.metric("Filename", uploaded_file.name)
        st.metric("Characters", f"{len(medical_report):,}")
        st.metric("Status", "Ready for analysis")

    if st.button("Analyze Report", use_container_width=True):
        with st.spinner("AI specialists analyzing the report..."):
            cardiologist = Cardiologist(medical_report)
            psychologist = Psychologist(medical_report)
            pulmonologist = Pulmonologist(medical_report)

            cardiologist_report = cardiologist.run()
            psychologist_report = psychologist.run()
            pulmonologist_report = pulmonologist.run()

        st.markdown("---")
        st.success("Analysis complete. Review each specialist perspective below.")

        tab1, tab2, tab3, tab4 = st.tabs([
            "Overview",
            "Cardiologist",
            "Psychologist",
            "Pulmonologist",
        ])

        with tab1:
            st.markdown("<div class='card'><h4>Final Diagnosis</h4></div>", unsafe_allow_html=True)
            team = MultidisciplinaryTeam(
                cardiologist_report,
                psychologist_report,
                pulmonologist_report
            )
            final_diagnosis = team.run()
            st.write(final_diagnosis)

        with tab2:
            st.markdown("<div class='card'><h4>Cardiologist Analysis</h4></div>", unsafe_allow_html=True)
            st.write(cardiologist_report)

        with tab3:
            st.markdown("<div class='card'><h4>Psychologist Analysis</h4></div>", unsafe_allow_html=True)
            st.write(psychologist_report)

        with tab4:
            st.markdown("<div class='card'><h4>Pulmonologist Analysis</h4></div>", unsafe_allow_html=True)
            st.write(pulmonologist_report)