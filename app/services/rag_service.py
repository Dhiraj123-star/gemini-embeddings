import uuid
from google import genai
from app.core.config import GEMINI_API_KEY, LLM_MODEL
from app.core.chroma import collection
from app.services.embedding_service import get_embedding
from typing import Generator

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


def generate_answer_stream(query:str, context:str) -> Generator[str,None,None]:
    prompt = f"""
    Context:
    {context}

    Question:
    {query}

    Answer clearly and concisely.
    """

    stream = client.models.generate_content_stream(
        model=LLM_MODEL,
        contents=prompt
    )

    for chunk in stream:
        if chunk.text:
            yield chunk.text


def search_stream(query, top_k=3, source=None):
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
        def empty_stream():
            yield "No results found"
        return empty_stream()

    context = "\n\n".join(docs)

    return generate_answer_stream(query,context)