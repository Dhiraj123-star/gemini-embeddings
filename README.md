# 🚀 Gemini RAG API (FastAPI + Chroma + PDF QA + Streaming UI)

A minimal yet **production-style RAG (Retrieval-Augmented Generation) system** using **Google Gemini Embeddings (`gemini-embedding-2-preview`)**, **ChromaDB**, and **FastAPI**.

This project allows users to **upload PDF documents and ask questions via a chat UI**, with **real-time streaming responses** generated using relevant context retrieved from stored embeddings.

---

## 📌 Features

* 📄 Upload PDF documents and extract text
* ✂️ Chunk documents for better semantic retrieval
* 🧠 Generate embeddings using Gemini
* 🗄️ Store embeddings in Chroma (persistent vector DB)
* 🔍 Semantic search with **Top-K retrieval**
* 🤖 Generate contextual answers using Gemini (RAG)
* ⚡ **Streaming responses (real-time output like ChatGPT)**
* 💬 **Simple HTML chat UI**
* 📂 Multi-document support with metadata filtering
* 📋 List uploaded documents
* ❌ Delete specific documents
* 🚀 FastAPI-based REST API

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Google Gemini (Embeddings + LLM)
* ChromaDB (Vector Database)
* PyPDF (PDF parsing)
* HTML + JavaScript (Chat UI)
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

## 🌐 Access UI

Open in browser:

```text
http://localhost:8000
```

👉 Upload PDF → Ask questions → Get streaming answers

---

## 🌐 API Endpoints

---

### ✅ Health Check / UI

```http
GET /
```

Serves the **chat dashboard UI**

---

### 📤 Upload PDF

```http
POST /upload
```

#### Response

```json
{
  "message": "PDF processed successfully",
  "file": "docker training.pdf",
  "chunks_stored": 6
}
```

---

### ❓ Ask Question (Standard)

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

---

### ⚡ Ask Question (Streaming)

```http
POST /ask-stream
```

👉 Returns **streaming response (chunk-by-chunk)**

---

### 📂 List Documents

```http
GET /documents
```

---

### ❌ Delete Document

```http
DELETE /documents?source=docker training.pdf
```

---

## 🧠 How It Works

```text
PDF → Text Extraction → Chunking → Embeddings (Gemini)
   → Store in Chroma → Query Embedding → Similarity Search
   → Context Retrieval → Gemini (Streaming) → Answer
```

---

## 💬 Chat UI Features

* Upload PDF directly from browser
* Ask questions interactively
* Real-time streaming answers
* Simple and lightweight interface

---

## 🔥 Key Concepts

* **Embeddings** → Convert text into vectors
* **Vector Search** → Find similar content
* **RAG** → Combine retrieval + LLM generation
* **Streaming** → Token-by-token response generation
* **Metadata Filtering** → Query specific documents

---


---

## 📜 License

MIT License

---

