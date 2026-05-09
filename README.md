# 🚀 Gemini RAG API (FastAPI + ChromaDB + PDF QA + Streaming UI + NGINX + HTTPS)

A minimal yet **production-style RAG (Retrieval-Augmented Generation) system** built using **Google Gemini Embeddings (`gemini-embedding-2`)**, **ChromaDB**, **FastAPI**, **NGINX**, and **HTTPS**.

This project allows users to:

* 📄 Upload PDF documents
* 🔍 Perform semantic search
* 🤖 Ask questions from uploaded documents
* ⚡ Receive real-time streaming AI responses
* 💬 Interact through a simple chat dashboard UI
* 🔐 Access the application securely over HTTPS
* 🐳 Run the complete stack using Docker Compose

---

# 📌 Features

* 📄 Upload PDF documents and extract text
* ✂️ Chunk documents for semantic retrieval
* 🧠 Generate embeddings using Gemini
* 🗄️ Store embeddings in ChromaDB
* 🔍 Top-K semantic similarity retrieval
* 🤖 RAG-based contextual answer generation
* ⚡ Real-time streaming responses
* 💬 HTML + JavaScript chat dashboard
* 📂 Multi-document support
* 🏷️ Metadata filtering by document source
* 📋 List uploaded documents
* ❌ Delete uploaded documents
* 🐳 Dockerized deployment
* 🌐 NGINX reverse proxy support
* 🔐 HTTPS with self-signed SSL certificates
* 🚀 Modular FastAPI architecture

---

# 🛠️ Tech Stack

* Python 3.12
* FastAPI
* Google Gemini API
* ChromaDB
* PyPDF
* HTML + JavaScript
* Docker & Docker Compose
* NGINX
* OpenSSL

---

# 📦 Installation

## Install dependencies

```bash
pip install -U google-genai fastapi uvicorn chromadb pypdf python-dotenv numpy
```

---

# 🔐 Environment Setup

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

# 🔐 Generate Local SSL Certificates

Create SSL folder:

```bash
mkdir ssl
```

Generate self-signed certificates:

```bash
openssl req -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout ssl/nginx.key \
-out ssl/nginx.crt
```

Generated files:

```text
ssl/
├── nginx.crt
└── nginx.key
```

---

# 🐳 Run with Docker + NGINX + HTTPS

## Build & Run

```bash
docker-compose up --build
```

Open:

```text
https://localhost
```

NGINX acts as the reverse proxy and forwards requests securely to the FastAPI application.

---

# 🌐 API Endpoints

---

## ✅ Health Check / Chat UI

```http
GET /
```

Serves the chat dashboard UI.

---

## 📤 Upload PDF

```http
POST /upload
```

### Example Response

```json
{
  "message": "PDF processed successfully",
  "file": "docker training.pdf",
  "chunks_stored": 6
}
```

---

## ❓ Ask Question

```http
POST /ask
```

### Request

```json
{
  "query": "What is Docker?",
  "top_k": 3,
  "source": "docker training.pdf"
}
```

### Response

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

## ⚡ Streaming Question Answering

```http
POST /ask-stream
```

Returns real-time streaming responses.

---

## 📂 List Uploaded Documents

```http
GET /documents
```

---

## ❌ Delete Document

```http
DELETE /documents?source=docker training.pdf
```

---

# 🧠 How It Works

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

# 💬 Chat UI Features

* Upload PDFs directly from browser
* Ask questions interactively
* Receive streaming AI responses
* Lightweight and responsive dashboard

---

# 🔥 Key Concepts

* **Embeddings** → Convert text into vectors
* **Vector Search** → Retrieve semantically similar chunks
* **RAG** → Retrieval + AI generation
* **Streaming** → Token-by-token AI response generation
* **Metadata Filtering** → Query specific documents
* **HTTPS** → Secure encrypted communication

---

# 📁 Project Structure

```text
.
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   └── main.py
│
├── nginx/
│   └── default.conf
│
├── ssl/
│   ├── nginx.crt
│   └── nginx.key
│
├── static/
│   └── index.html
│
├── chroma_db/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── .env
```

---

# 📜 License

MIT License

---
