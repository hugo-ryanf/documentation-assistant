from pydantic import BaseModel
from typing import List, Optional
class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 5
class SourceChunk(BaseModel):
    content: str
    source: str        # nome do arquivo
    page: int          # numero da pagina
    score: float       # similaridade cosine (0-1)
class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[SourceChunk]
    model_used: str
class IndexResponse(BaseModel):
    message: str
    documents_indexed: int
    chunks_created: int