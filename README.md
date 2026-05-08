# 🧠 AI-Powered News Intelligence & Conversational Analysis Platform

An advanced AI-powered News Intelligence platform that extracts real-time news articles, performs AI analysis, detects sentiment & media bias, and allows users to chat interactively with news articles using Large Language Models (LLMs).

This platform combines:
- Generative AI
- NLP (Natural Language Processing)
- Conversational AI
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Modern AI Dashboard UI

Built using:
- Streamlit
- LangChain
- Groq LLMs
- BeautifulSoup
- Hugging Face Embeddings
- FAISS Vector Database

---

# 🚀 Features

✅ Real-Time News Extraction  
✅ AI-Powered Summarization  
✅ Headline Generation  
✅ Key Insights Extraction  
✅ Sentiment Analysis  
✅ News Bias Detection  
✅ Political Leaning Analysis  
✅ Conversational AI Chatbot  
✅ RAG-based Semantic Retrieval  
✅ Modern AI Dashboard UI  
✅ Glassmorphism & Animations  
✅ Context-Aware Question Answering  

---

# 🧠 What This Project Does

The system takes a news article URL as input and automatically:

1. Extracts article content from the webpage  
2. Cleans and preprocesses the article text  
3. Sends the article to an LLM for analysis  
4. Generates:
   - headline
   - summary
   - insights
   - category
   - sentiment
   - bias analysis  
5. Allows users to interactively chat with the article using AI  

Instead of reading lengthy news articles manually, users can quickly understand important information and ask contextual questions interactively.

---

# 🏗️ System Architecture

User  
↓  
Streamlit Frontend  
↓  
Article URL Input  
↓  
Web Scraping Layer  
(requests + BeautifulSoup)  
↓  
Article Text Extraction  
↓  
LangChain Pipeline  
↓  
Groq LLM  
↓  
AI Analysis  
↓  
Frontend Rendering  
↓  
Conversational Chatbot  
↓  
(Optional) RAG Retrieval System  

---

# 🧠 AI Concepts Used

| Concept | Purpose |
|---|---|
| Generative AI | Summarization & reasoning |
| NLP | Text understanding |
| Prompt Engineering | Structured AI responses |
| Conversational AI | Interactive chatbot |
| RAG | Retrieval-based memory |
| Embeddings | Semantic vector representation |
| Vector Search | Similarity retrieval |
| Context Injection | Article-based QA |

---

# ⚙️ Technologies Used

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| AI Framework | LangChain |
| LLM Provider | Groq |
| Embeddings | Hugging Face |
| Vector Database | FAISS |
| Web Scraping | BeautifulSoup |
| Styling | Custom CSS |
| Animations | streamlit-lottie |

---

# 🧠 Why Hugging Face Was Used

Hugging Face was used for generating semantic embeddings.

Model used:

sentence-transformers/all-MiniLM-L6-v2

Purpose:
- Convert article text into vectors
- Enable semantic similarity search
- Retrieve relevant articles from FAISS

Example:
- “AI layoffs”
- “Tech companies reducing workforce”

Both become semantically similar vectors.

---

# 🧠 Why FAISS Was Used

FAISS is a vector database used for:
- storing embeddings
- semantic retrieval
- similarity search
- RAG memory system

FAISS enables the chatbot to retrieve relevant stored articles instead of relying only on current context.

---

# 🧠 Why LangChain Was Used

LangChain was used for:
- prompt chaining
- LLM orchestration
- RAG pipelines
- conversational AI
- structured prompt engineering

---

# 🧠 Why Groq Was Used

Groq provides ultra-fast LLM inference.

Used for:
- article summarization
- chatbot responses
- sentiment analysis
- bias detection
- reasoning tasks

---

# 🧠 Components Used in Project

## 1️⃣ Frontend UI Component
Handles:
- user interaction
- dashboard
- chatbot UI
- metrics
- animations

Technology:
- Streamlit

---

## 2️⃣ Web Scraping Component

Extracts article content from URLs.

Libraries:
- requests
- BeautifulSoup

Flow:

URL → HTML → Parse → Extract Text → Clean Content

---

## 3️⃣ LLM Processing Component

Performs:
- summarization
- insight extraction
- sentiment analysis
- bias detection
- chatbot reasoning

Technologies:
- LangChain
- Groq

---

## 4️⃣ Prompt Engineering Component

Custom prompts were designed to:
- generate structured JSON
- improve AI consistency
- reduce hallucinations

---

## 5️⃣ Conversational Chatbot Component

Allows users to chat with the article using context-aware prompting.

---

## 6️⃣ Session State Component

Used:
st.session_state

to persist:
- article text
- AI analysis
- chat history

---

## 7️⃣ RAG Component

Used for:
- long-term memory
- semantic retrieval
- intelligent article search

Technologies:
- Hugging Face embeddings
- FAISS
- LangChain

---

# 📂 Project Structure

ai-news-intelligence/

├── app.py  
├── llm.py  
├── rag.py  
├── article_extractor.py  
├── requirements.txt  
├── .env  

├── data/  
│   └── faiss_index/  

└── assets/  

---

# 📄 Main Files Explanation

| File | Purpose |
|---|---|
| app.py | Main frontend & app logic |
| llm.py | LLM chains & prompts |
| rag.py | RAG pipeline & vector retrieval |
| article_extractor.py | News extraction system |
| .env | API keys |
| requirements.txt | Dependencies |

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-news-intelligence.git

cd ai-news-intelligence
