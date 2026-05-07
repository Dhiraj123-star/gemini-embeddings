# 🚀 Gemini RAG API (FastAPI + Chroma + PDF QA + Streaming UI)

A minimal yet **production-style RAG (Retrieval-Augmented Generation) system** built using **Google Gemini Embeddings (`gemini-embedding-2`)**, **ChromaDB**, and **FastAPI**.

This project allows users to:

* 📄 Upload PDF documents
* 🔍 Perform semantic search
* 🤖 Ask questions from uploaded documents
* ⚡ Receive real-time streaming AI responses
* 💬 Interact through a simple chat dashboard UI

---

## 📌 Features

* 📄 Upload PDF documents and extract text
* ✂️ Chunk documents for semantic retrieval
* 🧠 Generate embeddings using Gemini
* 🗄️ Store embeddings in ChromaDB
* 🔍 Top-K semantic similarity search
* 🤖 RAG-based contextual answer generation
* ⚡ Real-time streaming responses
* 💬 HTML + JavaScript chat dashboard
* 📂 Multi-document support
* 🏷️ Metadata filtering by document source
* 📋 List uploaded documents
* ❌ Delete uploaded documents
* 🐳 Docker & Docker Compose support
* 🚀 FastAPI REST API architecture

---

## 🛠️ Tech Stack

* Python 3.12
* FastAPI
* Google Gemini API
* ChromaDB
* PyPDF
* HTML + JavaScript
* Docker & Docker Compose

---

## 📦 Installation

### Install dependencies

```bash
pip install -U google-genai fastapi uvicorn chromadb pypdf python-dotenv numpy
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000
```

---

# 🐳 Run with Docker

## Build & Run

```bash
docker-compose up --build
```

Open:

```text
http://localhost:8000
```

---

## 🌐 API Endpoints

---

### ✅ Health Check / Chat UI

```http
GET /
```

Serves the chat dashboard UI.

---

### 📤 Upload PDF

```http
POST /upload
```

#### Example Response

```json
{
  "message": "PDF processed successfully",
  "file": "docker training.pdf",
  "chunks_stored": 6
}
```

---

### ❓ Ask Question

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
    "Docker allows applications to run in containers..."
  ]
}
```

---

### ⚡ Streaming Question Answering

```http
POST /ask-stream
```

Returns real-time streaming responses.

---

### 📂 List Uploaded Documents

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
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Gemini Embeddings
   ↓
Store in ChromaDB
   ↓
Semantic Retrieval
   ↓
Gemini RAG Generation
   ↓
Streaming Answer
```

---

## 💬 Chat UI Features

* Upload PDFs directly from browser
* Ask questions interactively
* Receive streaming AI responses
* Lightweight and simple dashboard

---

## 🔥 Key Concepts

* **Embeddings** → Convert text into vectors
* **Vector Search** → Retrieve semantically similar chunks
* **RAG** → Retrieval + AI generation
* **Streaming** → Token-by-token AI response
* **Metadata Filtering** → Query specific documents

---

## 📁 Project Structure

```text
.
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   └── main.py
│
├── static/
│   └── index.html
│
├── chroma_db/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── .env
```

---

## 📜 License

MIT License

---
