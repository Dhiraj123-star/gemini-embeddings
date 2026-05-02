
# 🚀 Gemini Embeddings Semantic Search API (FastAPI)

A minimal project demonstrating how to use **Google Gemini Embeddings (`gemini-embedding-2-preview`)** to build a **semantic search system**, enhanced with **AI-generated explanations using Gemini** and **Top-K result retrieval**.

---

## 📌 Features

- Convert text into vector embeddings using Gemini
- Perform semantic similarity using cosine similarity
- Retrieve **Top-K most relevant documents**
- Generate AI-powered explanations for each result
- Expose functionality via FastAPI REST API
- Lightweight and easy to understand implementation

---

## 🛠️ Tech Stack

- Python
- FastAPI
- google-genai (Gemini SDK)
- NumPy
- python-dotenv

---

## 📦 Installation

### Install dependencies

```bash
pip install -U google-genai numpy python-dotenv fastapi uvicorn
````

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### Health Check

```bash
GET /
```

### Semantic Search (Top-K)

```bash
POST /search
```

#### Request Body

```json
{
  "query": "best backend framework",
  "top_k": 3
}
```

#### Example Response

```json
{
  "query": "best backend framework",
  "results": [
    {
      "document": "FastAPI is a backend framework for building APIs.",
      "score": 0.78,
      "explanation": "FastAPI is designed specifically for building APIs, making it highly relevant."
    },
    {
      "document": "Django is a backend web framework.",
      "score": 0.75,
      "explanation": "Django is a full-featured backend framework suitable for web applications."
    },
    {
      "document": "Redis is a caching system used in backend architecture.",
      "score": 0.55,
      "explanation": "Redis supports backend systems by improving performance through caching."
    }
  ]
}
```

---

## 🧠 How It Works

* Documents are converted into embeddings using Gemini
* User query is converted into an embedding
* Cosine similarity is calculated between query and documents
* Top-K relevant documents are selected based on similarity
* Gemini generates explanations for each result

---

## 🔮 Future Improvements

* Add hybrid search (keyword + semantic)
* Store embeddings in vector databases (Qdrant, pgvector)
* Add caching (Redis) for embeddings
* Build full RAG pipeline (context + answer generation)
* Add authentication & rate limiting

---

## 📜 License

MIT License

````
