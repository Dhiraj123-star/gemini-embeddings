# 🚀 Gemini RAG API (FastAPI + ChromaDB + PDF QA + Streaming UI + NGINX + HTTPS + CI/CD)

A minimal yet **production-style RAG (Retrieval-Augmented Generation) system** built using **Google Gemini Embeddings (`gemini-embedding-2`)**, **ChromaDB**, **FastAPI**, **NGINX**, **Docker**, and **GitHub Actions CI/CD**.

This project allows users to:

* 📄 Upload PDF documents
* 🔍 Perform semantic search
* 🤖 Ask questions from uploaded documents
* ⚡ Receive real-time streaming AI responses
* 💬 Interact through a simple chat dashboard UI
* 🔐 Access the application securely over HTTPS
* 🐳 Run the complete stack using Docker Compose
* 🚀 Automatically build & push Docker images using GitHub Actions

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
* ⚙️ GitHub Actions CI/CD pipeline
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
* GitHub Actions

---

# 📦 Installation

## Install dependencies

```bash id="b1osux"
pip install -U google-genai fastapi uvicorn chromadb pypdf python-dotenv numpy
```

---

# 🔐 Environment Setup

Create a `.env` file:

```env id="s4ec1l"
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run Locally

```bash id="5v96qv"
uvicorn app.main:app --reload
```

Open:

```text id="u7kkdw"
http://localhost:8000
```

---

# 🔐 Generate Local SSL Certificates

Create SSL folder:

```bash id="c8h8qj"
mkdir ssl
```

Generate self-signed certificates:

```bash id="jv8zci"
openssl req -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout ssl/nginx.key \
-out ssl/nginx.crt
```

Generated files:

```text id="w8fd71"
ssl/
├── nginx.crt
└── nginx.key
```

---

# 🐳 Run with Docker + NGINX + HTTPS

## Build & Run

```bash id="8ysx5d"
docker-compose up --build
```

Open:

```text id="y36rj0"
https://localhost
```

NGINX acts as the reverse proxy and forwards requests securely to the FastAPI application.

---

# ⚙️ GitHub Actions CI/CD

This project includes a simple GitHub Actions workflow that:

* Builds the Docker image
* Pushes the image to DockerHub automatically on every push to `main`

---

## GitHub Secrets

Add the following repository secrets:

```text id="jlwm9w"
DOCKER_USERNAME
DOCKER_PASSWORD
```

---

## DockerHub Image

```text id="mq5l9u"
dhiraj918106/gemini-rag-api:latest
```

---

# 🌐 API Endpoints

---

## ✅ Health Check / Chat UI

```http id="j66tfy"
GET /
```

Serves the chat dashboard UI.

---

## 📤 Upload PDF

```http id="4r21fr"
POST /upload
```

### Example Response

```json id="3cb6u4"
{
  "message": "PDF processed successfully",
  "file": "docker training.pdf",
  "chunks_stored": 6
}
```

---

## ❓ Ask Question

```http id="0yowk7"
POST /ask
```

### Request

```json id="d6y2ti"
{
  "query": "What is Docker?",
  "top_k": 3,
  "source": "docker training.pdf"
}
```

### Response

```json id="0b6m9j"
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

```http id="bt8r7g"
POST /ask-stream
```

Returns real-time streaming responses.

---

## 📂 List Uploaded Documents

```http id="x0e9k5"
GET /documents
```

---

## ❌ Delete Document

```http id="duv9vz"
DELETE /documents?source=docker training.pdf
```

---

# 🧠 How It Works

```text id="fkwwch"
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
* **CI/CD** → Automated Docker image deployment

---

# 📁 Project Structure

```text id="w9q7vs"
.
├── .github/
│   └── workflows/
│       └── docker.yml
│
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
