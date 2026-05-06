from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import StreamingResponse
from app.services.pdf_service import extract_text_from_pdf, chunk_text
from app.services.rag_service import store_pdf_chunks, search_stream, normalize_filename
from app.schemas.request import QueryRequest
from app.core.chroma import collection

router = APIRouter()



@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    filename = normalize_filename(file.filename)

    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)

    store_pdf_chunks(chunks, filename)

    return {"file": filename, "chunks": len(chunks)}


@router.post("/ask-stream")
def ask(request: QueryRequest):
    
    generator = search_stream(
        request.query,
        request.top_k,
        request.source
    )

    return StreamingResponse(generator, media_type="text/event-stream")

@router.get("/documents")
def list_docs():
    results = collection.get(include=["metadatas"])

    sources = {
        m["source"] for m in results.get("metadatas", []) if m
    }

    return {"documents": list(sources)}


@router.delete("/documents")
def delete_doc(source: str = Query(...)):
    source = normalize_filename(source)

    collection.delete(where={"source": source})

    return {"message": f"{source} deleted"}