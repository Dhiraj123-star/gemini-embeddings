import os
import numpy as np
from fastapi import FastAPI,UploadFile,File,Query
from pypdf import PdfReader
import uuid
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import chromadb
from chromadb.config import Settings


# Load environment variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-embedding-2"

# FastAPI app
app = FastAPI(title="Gemini + Chroma Semantic Search API")

# ---------- Chroma Setup --------------
chroma_client = chromadb.Client(
    Settings(persist_directory="./chroma_db")
)

collection = chroma_client.get_or_create_collection(name="documents")


# ------------ Core Logic -----------------

def get_embedding(text: str):
    response = client.models.embed_content(
        model=MODEL,
        contents=text
    )
    return response.embeddings[0].values

# ------ Helper function -----------
def normalize_filename(filename:str) ->str:
    return filename.strip().lower()



def search(query:str,top_k:int=3,source:str =None):
    query_embedding = get_embedding(query)

    query_params= {
        "query_embeddings": [query_embedding],
        "n_results": top_k
    }

    if source:
        query_params["where"]= {"source":normalize_filename(source)}

    results = collection.query(
       **query_params
    )

    docs= results.get("documents",[[]])[0]
    
    if not docs:
        return {
            "query": query,
            "answer": "No relevant results found.",
            "context":[]
        }
    
    # Combine context
    context = "\n\n".join(docs)

    answer = generate_answer(query,context)

    return {
        "query": query,
        "answer": answer,
        "context" : docs
    }



# --------- Explanation ---------
def generate_answer(query:str,context:str ):
    prompt = f"""
    Answer the question based on the context below.
    Context:
    {context}
    Question:
    {query}

    Answer clearly and concisely. 

    """
    response = client.models.generate_content (
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )
    return response.text

# ------- PDF text extraction ---------
def extract_text_from_pdf(file: UploadFile):
    reader = PdfReader(file.file)
    text =""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def chunk_text(text:str, chunk_size: int = 500,overlap:int = 50):
    chunks = []
    start=0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    
    return chunks

# --------- Store PDF chunks in Chroma ---------
def store_pdf_chunks(chunks,filename:str):
    embeddings= [get_embedding(chunk) for chunk in chunks]

    ids= [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas= [{"source": filename} for _ in chunks]  # dynamic filename
    )



# --------------- API Schema ------------

class QueryRequest(BaseModel):
    query:str
    top_k:int =3 
    source: str| None = None # filter by filename
# ------------- Routes -----------

@app.get("/")
def root():
    return {"message": "Gemini + Chroma Semantic Search API running!!"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    normalized_name = normalize_filename(file.filename)

    text = extract_text_from_pdf(file)

    chunks = chunk_text(text)

    store_pdf_chunks(chunks,normalized_name) # pass filename

    return {
        "message": "PDF processed successfully",
        "file": normalized_name,
        "chunks_stored":len(chunks)
    }

@app.post("/ask")
def ask_question(request: QueryRequest):
    return search(request.query,request.top_k,request.source)

@app.get("/documents")
def list_documents():
    results = collection.get(include=["metadatas"])

    sources = set()

    for meta in results.get("metadatas",[]):
        if meta and "source" in meta:
            sources.add(meta["source"])

    return {
        "documents":list(sources)
    }

@app.delete("/documents")
def delete_document(source: str = Query(...)):
    normalized_source = normalize_filename(source)

    collection.delete(
        where= {"source":normalized_source}
    )

    return {
        "message": f"Document ' {normalized_source}' deleted succesfullly"
    }