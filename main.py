import os
from typing import List
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-embedding-2-preview"

app = FastAPI(title="Gemini Semantic Search API")

# ------------ Core Logic -----------------

def get_embedding(text: str):
    response = client.models.embed_content(
        model=MODEL,
        contents=text
    )
    return response.embeddings[0].values


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


documents = [
    "FastAPI is great for APIs.",
    "Django is a full-stack framework",
    "Redis is used for caching.",
    "Kafka is used for streaming"
]

# Pre-computing embeddings at startup
doc_embeddings = [get_embedding(doc) for doc in documents]

def search(query:str):
    query_emb = get_embedding(query)

    scores = [
        cosine_similarity(query_emb,doc_emb)
        for doc_emb in doc_embeddings
    ]
    best_match_index= scores.index(max(scores))
    return {
        "query": query,
        "best_match": documents[best_match_index],
        "score": float(max(scores))
    }

# --------------- API Schema ------------

class QueryRequest(BaseModel):
    query:str

# ------------- Routes -----------

@app.get("/")
def root():
    return {"message": "Gemini Semantic Search API is running!!"}

@app.post("/search")
def semantic_search(request: QueryRequest):
    return search(request.query)