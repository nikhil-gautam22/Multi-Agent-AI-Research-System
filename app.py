import streamlit as st
from pipeline import run_research_pipeline

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="ResearchMind",
    page_icon="🤖",
    layout="wide",
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp{
    background:#0b0b12;
    color:white;
}
header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}
            
.block-container{
    padding-top:2rem;
    max-width:1400px;
    padding-top:0.5rem;
    padding-bottom:2rem
}

.title{
    text-align:center;
    font-size:84px;
    font-weight:900;
    margin-top:20px;
    margin-bottom:5px;
}

.title1{
    color:white;
}

.title2{
    color:#ff8a00;
}

.subtitle{
    text-align:center;
    color:#a8a8a8;
    font-size:18px;
    margin-bottom:50px;
}

.small{
    text-align:center;
    color:#ff8a00;
    letter-spacing:4px;
    font-size:13px;
    font-weight:bold;
}

.card{

    background:#17171f;
    padding:18px;
    border-radius:18px;
    margin-bottom:18px;
    border-left:5px solid #ff8a00;
    box-shadow:0px 0px 18px rgba(0,0,0,.35);

}

.pipeline-title{
    font-size:28px;
    font-weight:bold;
    margin-bottom:20px;
}

.report{

    background:#17171f;
    padding:25px;
    border-radius:15px;
    margin-top:25px;

}

.stTextInput input{

    background:#181820;
    color:white;
    border-radius:10px;
    border:1px solid #333;

}

div.stButton > button{

    width:100%;
    background:linear-gradient(90deg,#ff8a00,#ff5c35);
    color:white;
    border:none;
    border-radius:10px;
    height:55px;
    font-size:18px;
    font-weight:bold;

}

div.stButton > button:hover{

    background:linear-gradient(90deg,#ff9d24,#ff734f);

}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
"""
<div class='small'>
MULTI AGENT AI SYSTEM
</div>

<h1 class='title'>
<span class='title1'>Research</span><span class='title2'>Mind</span>
</h1>

<p class='subtitle'>
Four specialized AI agents collaborate — searching, scraping,
writing and critiquing to generate a complete research report.
</p>
""",
unsafe_allow_html=True
)

# ---------------- LAYOUT ---------------- #

left, right = st.columns([3,2], gap="large")

with left:

    topic=st.text_input(
        "Research Topic",
        placeholder="Quantum Computing Breakthroughs"
    )

    run=st.button("⚡ Run Research Pipeline")

with right:

    st.markdown("<div class='pipeline-title'>Pipeline</div>",unsafe_allow_html=True)

    search_status=st.empty()
    reader_status=st.empty()
    writer_status=st.empty()
    critic_status=st.empty()

    search_status.markdown(
        "<div class='card'>🔍 <b>Search Agent</b><br>Waiting...</div>",
        unsafe_allow_html=True
    )

    reader_status.markdown(
        "<div class='card'>📖 <b>Reader Agent</b><br>Waiting...</div>",
        unsafe_allow_html=True
    )

    writer_status.markdown(
        "<div class='card'>✍ <b>Writer Agent</b><br>Waiting...</div>",
        unsafe_allow_html=True
    )

    critic_status.markdown(
        "<div class='card'>🧐 <b>Critic Agent</b><br>Waiting...</div>",
        unsafe_allow_html=True
    )

# ---------------- RUN ---------------- #

if run:

    if topic=="":

        st.warning("Enter a research topic.")
        st.stop()

    progress=st.progress(0)

    search_status.markdown(
        "<div class='card'>🔍 <b>Search Agent</b><br>Running...</div>",
        unsafe_allow_html=True
    )
    progress.progress(20)

    with st.spinner("Running Research Pipeline..."):
        result=run_research_pipeline(topic)

    search_status.markdown(
        "<div class='card'>✅ <b>Search Agent</b><br>Completed</div>",
        unsafe_allow_html=True
    )
    progress.progress(40)

    reader_status.markdown(
        "<div class='card'>✅ <b>Reader Agent</b><br>Completed</div>",
        unsafe_allow_html=True
    )
    progress.progress(65)

    writer_status.markdown(
        "<div class='card'>✅ <b>Writer Agent</b><br>Completed</div>",
        unsafe_allow_html=True
    )
    progress.progress(85)

    critic_status.markdown(
        "<div class='card'>✅ <b>Critic Agent</b><br>Completed</div>",
        unsafe_allow_html=True
    )
    progress.progress(100)

    st.success("Research Pipeline Completed Successfully!")

    tab1,tab2,tab3,tab4=st.tabs(
        [
            "🔍 Search Result",
            "📖 Scraped Content",
            "📝 Final Report",
            "🧐 Critic Feedback"
        ]
    )

    with tab1:
        st.write(result["search_results"])

    with tab2:
        st.write(result["scrape_content"])

    with tab3:
        st.markdown(result["report"])

        st.download_button(
            "⬇ Download Report",
            result["report"],
            file_name="research_report.md"
        )

    with tab4:
        st.markdown(result["feedback"])