import streamlit as st
from article_extractor import extract_article
from llm import analyze_article, chat_with_article

from streamlit_lottie import st_lottie

import requests
import time

# 🚀 PAGE CONFIG
st.set_page_config(
    page_title="AI News Intelligence",
    page_icon="🧠",
    layout="wide"
)

# 🎨 CUSTOM CSS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #111827);
    color: white;
}

/* Spacing */
.block-container {
    padding-top: 2rem;
}

/* Title */
.main-title {
    font-size: 4rem;
    font-weight: 800;
    text-align: center;

    background: linear-gradient(
        to right,
        #38bdf8,
        #8b5cf6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

/* Card */
.card {
    background: rgba(30,41,59,0.7);

    backdrop-filter: blur(12px);

    padding: 25px;

    border-radius: 20px;

    margin-bottom: 20px;

    border: 1px solid rgba(255,255,255,0.08);

    transition: 0.3s;
}

/* Hover */
.card:hover {
    transform: translateY(-4px);

    box-shadow: 0px 0px 25px rgba(59,130,246,0.3);
}

/* Section title */
.section-title {
    font-size: 1.6rem;
    font-weight: bold;

    color: #60a5fa;

    margin-top: 15px;
    margin-bottom: 15px;
}

/* Headline */
.headline {
    font-size: 2rem;

    color: #22c55e;

    font-weight: bold;

    line-height: 1.5;
}

/* Summary */
.summary {
    font-size: 1rem;

    line-height: 1.8;

    color: #e2e8f0;
}

/* Insight */
.insight {
    background: rgba(15,23,42,0.7);

    border-left: 4px solid #3b82f6;

    padding: 12px;

    border-radius: 10px;

    margin-bottom: 10px;

    color: white;
}

/* Input */
.stTextInput > div > div > input {
    background-color: rgba(30,41,59,0.8);

    color: white;

    border-radius: 12px;

    border: 1px solid #334155;
}

/* Button */
.stButton > button {
    width: 100%;

    height: 3.2em;

    border-radius: 12px;

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    color: white;

    font-size: 1rem;

    font-weight: bold;

    border: none;

    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);

    box-shadow: 0px 0px 20px rgba(124,58,237,0.4);
}

/* Metrics */
[data-testid="metric-container"] {
    background: rgba(17,24,39,0.8);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 20px;

    border-radius: 18px;
}

/* Chat */
.chat-box {
    background: rgba(17,24,39,0.8);

    padding: 18px;

    border-radius: 15px;

    margin-bottom: 10px;

    border-left: 4px solid #8b5cf6;
}

</style>
""", unsafe_allow_html=True)

# 🎬 LOTTIE
def load_lottie(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

lottie_ai = load_lottie(
    "https://assets9.lottiefiles.com/packages/lf20_x62chJ.json"
)

# 🧠 HEADER
st.markdown(
    '<div class="main-title">🧠 AI News Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze and Chat with News using LLMs</div>',
    unsafe_allow_html=True
)

st_lottie(
    lottie_ai,
    height=250,
    key="ai"
)

# 🔗 URL INPUT
st.markdown("## 🔗 Enter News Article URL")

url = st.text_input(
    "",
    placeholder="Paste article URL here..."
)

# 🚀 ANALYZE
if st.button("🚀 Analyze Article"):

    if not url:

        st.warning("Please enter a valid URL")
        st.stop()

    progress = st.progress(0)

    for i in range(30):
        time.sleep(0.01)
        progress.progress(i + 1)

    # 📰 Extract
    article_text = extract_article(url)

    if article_text.startswith("ERROR"):

        st.error(article_text)
        st.stop()

    # 🧠 Analyze
    for i in range(30, 100):
        time.sleep(0.01)
        progress.progress(i + 1)

    result = analyze_article(article_text)

    progress.empty()

    # 💾 Store article in session
    st.session_state.article_text = article_text

    # 📰 HEADLINE
    st.markdown("---")

    st.markdown(
        '<div class="section-title">📰 Headline</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="card">
        <div class="headline">
            {result.get("headline", "N/A")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 📄 SUMMARY
    st.markdown(
        '<div class="section-title">📄 Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="card">
        <div class="summary">
            {result.get("summary", "N/A")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 🔍 INSIGHTS
    st.markdown(
        '<div class="section-title">🔍 Key Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    insights = result.get("insights", [])

    if isinstance(insights, str):
        insights = insights.split("\n")

    for insight in insights:

        if insight.strip():

            st.markdown(f"""
            <div class="insight">
                • {insight}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # 📊 METRICS
    st.markdown(
        '<div class="section-title">📊 AI Analysis</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🏷 Category",
            result.get("category", "N/A")
        )

    with col2:
        st.metric(
            "💡 Sentiment",
            result.get("sentiment", "N/A")
        )

# 💬 CHATBOT
if "article_text" in st.session_state:

    st.markdown("---")

    st.markdown(
        "## 💬 Chat with this News Article"
    )

    user_question = st.text_input(
        "Ask anything about this article"
    )

    if st.button("🤖 Ask Question"):

        if user_question.strip():

            with st.spinner("AI Thinking..."):

                answer = chat_with_article(
                    st.session_state.article_text,
                    user_question
                )

            st.markdown(f"""
            <div class="chat-box">
                <b>🙋 You:</b><br>
                {user_question}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="chat-box">
                <b>🤖 AI:</b><br>
                {answer}
            </div>
            """, unsafe_allow_html=True)