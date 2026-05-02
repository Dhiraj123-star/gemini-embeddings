import os
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import chromadb


# Load environment variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-embedding-2"

# FastAPI app
app = FastAPI(title="Gemini + Chroma Semantic Search API")

# ---------- Chroma Setup --------------
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="documents")


# ------------ Core Logic -----------------

def get_embedding(text: str):
    response = client.models.embed_content(
        model=MODEL,
        contents=text
    )
    return response.embeddings[0].values

documents = [
    "FastAPI is a backend framework for building APIs.",
    "Django is a backend web framework.",
    "Redis is a caching system used in backend architecture.",
    "Kafka is a streaming platform used in backend systems."
]


# Store documents in Chroma 

def store_documents():
    existing= collection.count()

    if existing==0:
        embeddings = [get_embedding(doc) for doc in documents]

        collection.add(
            documents=documents,
            embeddings = embeddings,
            ids= [str(i) for i in range(len(documents))]
        )

store_documents()

# Pre-computing embeddings at startup
doc_embeddings = [get_embedding(doc) for doc in documents]

def search(query:str,top_k:int=3):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = top_k
    )

    docs= results["documents"][0]
    scores = results["distances"][0]

    final_results=[]

    for doc, score in zip(docs,scores):
        explanation=explain_result(query,doc)
        final_results.append({
            "document":doc,
            "score":float(1-score), # convert into similarity
            "explanation":explanation
        })

    return {
        "query":query,
        "results":final_results
    }

# --------- Explanation ---------
def explain_result(query:str,best_result:str ):
    prompt = f"""
    User query:  "{query}"
    Retrieved result: "{best_result}"

    Explain clearly why this result is relevant to the query.
    Keep it simple and concise.

    """
    response = client.models.generate_content (
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )
    return response.text


# --------------- API Schema ------------

class QueryRequest(BaseModel):
    query:str
    top_k:int =3 
# ------------- Routes -----------

@app.get("/")
def root():
    return {"message": "Gemini + Chroma Semantic Search API running!!"}

@app.post("/search")
def semantic_search(request: QueryRequest):
    return search(request.query,request.top_k)