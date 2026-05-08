# llm.py

import os
import json

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =========================================================
# LOAD ENV
# =========================================================

load_dotenv()

# =========================================================
# LLM
# =========================================================

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.3
)

# =========================================================
# ANALYSIS PROMPT
# =========================================================

analysis_prompt = PromptTemplate.from_template("""

You are an advanced AI News Intelligence System.

Analyze the following news article.

Return ONLY valid JSON.

FORMAT:

{{
    "headline": "...",
    "summary": "...",
    "insights": [
        "...",
        "...",
        "..."
    ],
    "category": "...",
    "sentiment": "...",
    "bias": "...",
    "bias_confidence": "...",
    "bias_reason": "..."
}}

Analyze:
- political leaning
- emotional framing
- sensationalism
- neutrality
- propaganda tone
- one-sided reporting

ARTICLE:
{article}

""")
# =========================================================
# ANALYSIS CHAIN
# =========================================================

analysis_chain = (
    analysis_prompt
    | llm
    | StrOutputParser()
)

# =========================================================
# ANALYZE ARTICLE
# =========================================================

def analyze_article(article_text):

    try:

        response = analysis_chain.invoke({
            "article": article_text
        })

        # Remove markdown formatting
        response = response.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        result = json.loads(response)

        return result

    except Exception as e:

        return {
            "headline": "Parsing Error",
            "summary": str(e),
            "insights": [],
            "category": "Unknown",
            "sentiment": "Unknown",
            "bias": "Unknown",
            "bias_confidence": "0%",
            "bias_reason": str(e)
        }

# =========================================================
# CHAT WITH ARTICLE
# =========================================================

def chat_with_article(article, question):

    chat_prompt = PromptTemplate.from_template("""

You are an AI News Assistant.

Answer the question ONLY
using the article below.

ARTICLE:
{article}

QUESTION:
{question}

ANSWER:

""")

    chat_chain = (
        chat_prompt
        | llm
        | StrOutputParser()
    )

    response = chat_chain.invoke({
        "article": article,
        "question": question
    })

    return response
