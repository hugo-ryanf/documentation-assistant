from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .rag_engine import RAGEngine
from .models import QueryRequest, QueryResponse, IndexResponse
from .config import settings
import shutil, os

app = FastAPI(title='Documentation Assistant API', version='1.0.0')
app.add_middleware(CORSMiddleware,
    allow_origins=['http://localhost:5173'],  # Vite dev server
    allow_methods=['*'], allow_headers=['*'],
)

rag = RAGEngine()

@app.get('/')
def health(): return {'status': 'online', 'docs': '/docs'}

@app.post('/api/query', response_model=QueryResponse)
async def query_documents(req: QueryRequest):
    sources = rag.query(req.question, req.top_k or settings.top_k_results)
    if not sources:
        raise HTTPException(404, 'Nenhum documento indexado ainda.')
    answer = await rag.generate_answer(req.question, sources)
    return QueryResponse(
        question=req.question,
        answer=answer,
        sources=sources,
        model_used=settings.ollama_model
    )

@app.post('/api/index', response_model=IndexResponse)
def reindex(): 
    docs, chunks = rag.index_documents()
    return IndexResponse(message='Indexacao concluida!',
        documents_indexed=docs, chunks_created=chunks)

@app.post('/api/upload')
async def upload_doc(file: UploadFile = File(...)):
    dest = os.path.join(settings.docs_path, file.filename)
    with open(dest, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    rag.index_documents()  # Re-indexa
    return {'message': f'{file.filename} enviado e indexado!'}

@app.get('/api/documents')
def list_documents():
    files = [f for f in os.listdir(settings.docs_path)
             if f.lower().endswith('.pdf')]
    return {'documents': files, 'count': len(files)}