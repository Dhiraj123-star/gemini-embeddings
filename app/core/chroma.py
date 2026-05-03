import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(
    Settings(persist_directory="./chroma_db")
)

collection = chroma_client.get_or_create_collection(name="documents")