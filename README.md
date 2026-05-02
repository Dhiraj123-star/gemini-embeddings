# 🚀 Gemini Embeddings Semantic Search API (FastAPI)

A minimal project demonstrating how to use **Google Gemini Embeddings (`gemini-embedding-2-preview`)** to build a simple **semantic search system**, enhanced with **AI-generated explanations using Gemini**.

---

## 📌 Features

- Convert text into vector embeddings using Gemini
- Perform semantic similarity using cosine similarity
- Retrieve the most relevant document based on meaning (not keywords)
- Generate AI-powered explanation for the retrieved result
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

### Semantic Search

```bash
POST /search
```

#### Request Body

```json
{
  "query": "which framework is best for APIs?"
}
```

#### Example Response

```json
{
  "query": "which framework is best for APIs?",
  "best_match": "FastAPI is great for APIs.",
  "score": 0.72,
  "explanation": "FastAPI is specifically designed for building APIs efficiently, making it highly relevant to the user's query."
}
```

---

## 🧠 How It Works

* Documents are converted into embeddings using Gemini
* User query is converted into an embedding
* Cosine similarity is calculated between query and documents
* Best matching document is selected
* Gemini generates a natural language explanation for the result

---

## 🔮 Future Improvements

* Add top-k semantic search results
* Store embeddings in vector databases (Qdrant, pgvector)
* Add caching (Redis) for embeddings
* Build full RAG pipeline (context + answer generation)
* Add authentication & rate limiting

---

## 📜 License

MIT License


