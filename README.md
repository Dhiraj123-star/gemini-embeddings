# 🚀 Gemini RAG API (FastAPI + Chroma + PDF QA)

A minimal yet **production-style RAG (Retrieval-Augmented Generation) system** using **Google Gemini Embeddings (`gemini-embedding-2-preview`)**, **ChromaDB**, and **FastAPI**.

This project allows users to **upload PDF documents and ask questions**, with answers generated using relevant context retrieved from stored embeddings.

---

## 📌 Features

* 📄 Upload PDF documents and extract text
* ✂️ Chunk documents for better semantic retrieval
* 🧠 Generate embeddings using Gemini
* 🗄️ Store embeddings in Chroma (persistent vector DB)
* 🔍 Semantic search with **Top-K retrieval**
* 🤖 Generate contextual answers using Gemini (RAG)
* 📂 Multi-document support with metadata filtering
* 📋 List uploaded documents
* ❌ Delete specific documents
* ⚡ FastAPI-based REST API

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Google Gemini (Embeddings + LLM)
* ChromaDB (Vector Database)
* PyPDF (PDF parsing)
* python-dotenv

---

## 📦 Installation

```bash
pip install -U google-genai fastapi uvicorn chromadb pypdf python-dotenv
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

---

### ✅ Health Check

```http
GET /
```

---

### 📤 Upload PDF

```http
POST /upload
```

Upload a PDF file.

#### Response

```json
{
  "message": "PDF processed successfully",
  "file": "docker training.pdf",
  "chunks_stored": 6
}
```

---

### ❓ Ask Question (RAG)

```http
POST /ask
```

#### Request

```json
{
  "query": "What is Docker?",
  "top_k": 3,
  "source": "docker training.pdf"
}
```

#### Response

```json
{
  "query": "What is Docker?",
  "answer": "Docker is a containerization platform...",
  "context": [
    "Docker allows applications to run in containers...",
    "Containers are lightweight and portable..."
  ]
}
```

---

### 📂 List Documents

```http
GET /documents
```

#### Response

```json
{
  "documents": [
    "docker training.pdf",
    "kubernetes guide.pdf"
  ]
}
```

---

### ❌ Delete Document

```http
DELETE /documents?source=docker training.pdf
```

#### Response

```json
{
  "message": "docker training.pdf deleted"
}
```

---

## 🧠 How It Works

```text
PDF → Text Extraction → Chunking → Embeddings (Gemini)
   → Store in Chroma → Query Embedding → Similarity Search
   → Context Retrieval → Gemini → Final Answer
```

---

## 🔥 Key Concepts

* **Embeddings** → Convert text into vectors
* **Vector Search** → Find similar content
* **RAG** → Combine retrieval + LLM generation
* **Metadata Filtering** → Query specific documents

---

## 🔮 Future Improvements

* Add streaming responses (real-time answers)
* Add hybrid search (BM25 + embeddings)
* Add user authentication (multi-tenant system)
* Add document versioning
* Add Redis caching for embeddings
* Add UI (Streamlit / React)

---

## 📜 License

MIT License

---
