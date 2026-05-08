# app.py

import streamlit as st
from article_extractor import extract_article
from llm import analyze_article, chat_with_article

from streamlit_lottie import st_lottie

import requests
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI News Intelligence",
    page_icon="@",
    layout="wide",
    initial_sidebar_state="expanded"
)


# SESSION STATE

if "article_text" not in st.session_state:
    st.session_state.article_text = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# LOTTIE

def load_lottie(url):

    try:

        r = requests.get(url)

        if r.status_code != 200:
            return None

        return r.json()

    except:
        return None

ai_animation = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json"
)

# CSS

st.markdown("""
<style>

.stApp {

    background:
    radial-gradient(circle at top left, #1e3a8a 0%, transparent 25%),
    radial-gradient(circle at top right, #7c3aed 0%, transparent 25%),
    linear-gradient(135deg, #020617, #0f172a);

    color: white;
}

.block-container {
    padding-top: 2rem;
}

.main-title {

    font-size: 5rem;

    font-weight: 900;

    text-align: center;

    background: linear-gradient(
        to right,
        #38bdf8,
        #8b5cf6,
        #ec4899
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.subtitle {

    text-align: center;

    font-size: 1.2rem;

    color: #cbd5e1;

    margin-top: 10px;

    margin-bottom: 40px;
}

.glass {

    background: rgba(15,23,42,0.55);

    backdrop-filter: blur(14px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 28px;

    margin-bottom: 22px;

    transition: 0.4s ease;
}

.glass:hover {

    transform: translateY(-5px);

    box-shadow:
    0px 0px 30px rgba(59,130,246,0.35);
}

.section-title {

    font-size: 1.8rem;

    font-weight: 800;

    margin-bottom: 18px;

    color: #60a5fa;
}

.headline {

    font-size: 2.2rem;

    font-weight: 800;

    line-height: 1.5;

    color: #f8fafc;
}

.summary {

    font-size: 1.05rem;

    line-height: 2;

    color: #e2e8f0;
}

.insight {

    background: rgba(30,41,59,0.7);

    border-left: 4px solid #3b82f6;

    padding: 18px;

    border-radius: 14px;

    margin-bottom: 14px;

    color: #f8fafc;
}

.chat-user {

    background: linear-gradient(
        90deg,
        rgba(37,99,235,0.3),
        rgba(124,58,237,0.3)
    );

    padding: 18px;

    border-radius: 18px;

    margin-bottom: 10px;
}

.chat-ai {

    background: rgba(30,41,59,0.7);

    padding: 18px;

    border-radius: 18px;

    margin-bottom: 18px;

    border-left: 4px solid #8b5cf6;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR

with st.sidebar:

    st.title("🧠 AI News")

    st.markdown("---")

    st.markdown("## 🚀 Features")

    st.write("AI Summarization")
    st.write(" AI Chatbot")
    st.write(" Sentiment Detection")
    st.write(" News Bias Detection")
    st.write(" Political Leaning Analysis")

# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="main-title"> AI News Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze • Detect Bias • Chat with News using AI</div>',
    unsafe_allow_html=True
)

if ai_animation:

    st_lottie(
        ai_animation,
        height=280,
        key="ai"
    )

# INPUT

st.markdown("## 🔗 Enter News Article URL")

url = st.text_input(
    "",
    placeholder="Paste article URL here..."
)

# ANALYZE

if st.button("🚀 Analyze Article"):

    if not url:

        st.warning("Please enter a valid URL")
        st.stop()

    progress = st.progress(0)

    for i in range(25):

        time.sleep(0.01)

        progress.progress(i + 1)

    # Extract article
    with st.spinner("📰 Extracting article..."):

        article_text = extract_article(url)

    if article_text.startswith("ERROR"):

        st.error(article_text)

        st.stop()

    # Analyze article
    with st.spinner("🧠 AI analyzing article..."):

        result = analyze_article(article_text)

    for i in range(25, 100):

        time.sleep(0.01)

        progress.progress(i + 1)

    progress.empty()

    # Save session
    st.session_state.article_text = article_text
    st.session_state.analysis_result = result
    st.session_state.chat_history = []

# SHOW RESULTS

if st.session_state.analysis_result:

    result = st.session_state.analysis_result

    tab1, tab2 = st.tabs([
        "📰 News Analysis",
        "💬 AI Chat"
    ])

    # ANALYSIS TAB

    with tab1:

        # HEADLINE
        st.markdown(
            '<div class="section-title">📰 Headline</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="glass">
            <div class="headline">
                {result.get("headline", "N/A")}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # SUMMARY
        st.markdown(
            '<div class="section-title">📄 Summary</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="glass">
            <div class="summary">
                {result.get("summary", "N/A")}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # INSIGHTS
        st.markdown(
            '<div class="section-title">🔍 Key Insights</div>',
            unsafe_allow_html=True
        )

        insights = result.get("insights", [])

        for insight in insights:

            st.markdown(f"""
            <div class="insight">
                • {insight}
            </div>
            """, unsafe_allow_html=True)

        # METRICS
        st.markdown(
            '<div class="section-title">📊 AI Analysis</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🏷 Category",
                result.get("category", "N/A")
            )

        with col2:

            st.metric(
                " Sentiment",
                result.get("sentiment", "N/A")
            )

        with col3:

            st.metric(
                " Bias",
                result.get("bias", "N/A")
            )

        # BIAS SECTION
        st.markdown(
            '<div class="section-title">⚖️ Bias Analysis</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="glass">

        <h3> AI Bias Detection</h3>

        <b>Bias Type:</b><br>
        {result.get("bias", "N/A")}

        <br><br>

        <b>Confidence:</b><br>
        {result.get("bias_confidence", "N/A")}

        <br><br>

        <b>Reason:</b><br>
        {result.get("bias_reason", "N/A")}

        </div>
        """, unsafe_allow_html=True)

    # CHAT TAB

    with tab2:

        st.markdown("## 💬 Chat with this Article")

        user_question = st.text_input(
            "Ask anything about this article"
        )

        if st.button("Ask AI"):

            if user_question.strip():

                with st.spinner(" Thinking..."):

                    answer = chat_with_article(
                        st.session_state.article_text,
                        user_question
                    )

                st.session_state.chat_history.append(
                    ("user", user_question)
                )

                st.session_state.chat_history.append(
                    ("ai", answer)
                )

        # SHOW CHAT
        for role, msg in st.session_state.chat_history:

            if role == "user":

                st.markdown(f"""
                <div class="chat-user">
                    <b> You:</b><br><br>
                    {msg}
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown(f"""
                <div class="chat-ai">
                    <b> AI:</b><br><br>
                    {msg}
                </div>
                """, unsafe_allow_html=True)
