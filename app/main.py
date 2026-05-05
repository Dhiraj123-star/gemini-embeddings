from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.routes import router

app = FastAPI(title="Gemini RAG API")

# Include API routes
app.include_router(router)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve UI at root
@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")