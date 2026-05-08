from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

import os

DB_PATH = "data/faiss_index"

# 🔥 Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#  SAVE ARTICLES
def save_article(text, metadata):

    docs = [
        Document(
            page_content=text,
            metadata=metadata
        )
    ]

    # Existing DB
    if os.path.exists(DB_PATH):

        db = FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        db.add_documents(docs)

    # New DB
    else:

        db = FAISS.from_documents(
            docs,
            embeddings
        )

    db.save_local(DB_PATH)

# 🔎 SEARCH ARTICLES
def search_articles(query):

    # ❌ No DB yet
    if not os.path.exists(DB_PATH):
        return []

    db = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=3)

    return docs
