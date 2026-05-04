import uuid
from google import genai
from app.core.config import GEMINI_API_KEY, LLM_MODEL
from app.core.chroma import collection
from app.services.embedding_service import get_embedding

client = genai.Client(api_key=GEMINI_API_KEY)


def normalize_filename(filename: str):
    return filename.strip().lower()


def store_pdf_chunks(chunks, filename):
    embeddings = [get_embedding(c) for c in chunks]
    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=[{"source": filename} for _ in chunks]
    )


def generate_answer(query, context):
    prompt = f"""
    Context:
    {context}

    Question:
    {query}

    Answer clearly and concisely.
    """

    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt
    )

    return response.text


def search(query, top_k=3, source=None):
    query_emb = get_embedding(query)

    params = {
        "query_embeddings": [query_emb],
        "n_results": top_k
    }

    if source:
        params["where"] = {"source": normalize_filename(source)}

    results = collection.query(**params)

    docs = results.get("documents", [[]])[0]

    if not docs:
        return {"query": query, "answer": "No results found", "context": []}

    context = "\n\n".join(docs)

    return {
        "query": query,
        "answer": generate_answer(query, context),
        "context": docs
    }