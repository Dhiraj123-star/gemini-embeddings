from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3
    source: str | None = None