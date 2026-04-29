
# 🚀 Gemini Embeddings Semantic Search (Python)

A minimal project demonstrating how to use **Google Gemini Embeddings (`gemini-embedding-2-preview`)** to build a simple **semantic search system**.

---

## 📌 Features

- Convert text into vector embeddings using Gemini
- Perform semantic similarity using cosine similarity
- Retrieve the most relevant document based on meaning (not keywords)
- Lightweight and easy to understand implementation

---

## 🛠️ Tech Stack

- Python
- google-genai (Gemini SDK)
- NumPy
- python-dotenv

---

## 📦 Installation

### Install dependencies

```bash
pip install -U google-genai numpy python-dotenv
````

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 Example

```bash
Enter your query:
fastapi good for?

Best Match: FastAPI is great for APIs.
```

---

## 🧠 How It Works

* Documents are converted into embeddings
* Query is converted into an embedding
* Cosine similarity is calculated between query and documents
* The most similar document is returned

---

## 🔮 Future Improvements

* Add FastAPI API layer
* Store embeddings in vector databases (Qdrant, pgvector)
* Support dynamic document input
* Return top-k results instead of a single match

---

## 📜 License

MIT License


