import os, json
import fitz  # PyMuPDF
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Tuple
from .config import settings
from .models import SourceChunk
import httpx

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer(settings.embedding_model)
        self.index = None
        self.chunks: List[dict] = []   # [{text, source, page}]
        self._load_or_build_index()

    def _extract_text(self, pdf_path: str) -> List[dict]:
        '''Extrai texto por pagina usando PyMuPDF.'''
        pages = []
        doc = fitz.open(pdf_path)
        for page_num, page in enumerate(doc):
            text = page.get_text('text').strip()
            if text:
                pages.append({'text': text, 'page': page_num + 1})
        doc.close()
        return pages
    
    def _chunk_text(self, text: str, source: str, page: int) -> List[dict]:
        '''Divide texto em chunks com overlap.'''
        chunks, size, overlap = [], settings.chunk_size, settings.chunk_overlap
        words = text.split()
        i = 0
        while i < len(words):
            chunk_words = words[i:i + size]
            chunks.append({'text': ' '.join(chunk_words),
                           'source': os.path.basename(source),
                           'page': page})
            i += size - overlap
        return chunks
    
    def index_documents(self) -> Tuple[int, int]:
        '''Indexa todos os PDFs em docs_path.'''
        all_chunks = []
        docs_count = 0
        for fname in os.listdir(settings.docs_path):
            if fname.lower().endswith('.pdf'):
                path = os.path.join(settings.docs_path, fname)
                pages = self._extract_text(path)
                for p in pages:
                    all_chunks.extend(self._chunk_text(p['text'], fname, p['page']))
                docs_count += 1
        if not all_chunks:
            return 0, 0
        texts = [c['text'] for c in all_chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        embeddings = np.array(embeddings).astype('float32')
        faiss.normalize_L2(embeddings)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)  # Inner Product = cosine apos normalize
        self.index.add(embeddings)
        self.chunks = all_chunks
        os.makedirs(settings.faiss_index_path, exist_ok=True)
        faiss.write_index(self.index,
            os.path.join(settings.faiss_index_path, 'index.faiss'))
        with open(settings.metadata_path, 'w', encoding='utf-8') as f:
            json.dump(all_chunks, f, ensure_ascii=False, indent=2)
        return docs_count, len(all_chunks)
    
    def _load_or_build_index(self):
        '''Carrega indice existente ou constroi do zero.'''
        idx_path = os.path.join(settings.faiss_index_path, 'index.faiss')
        if os.path.exists(idx_path) and os.path.exists(settings.metadata_path):
            self.index = faiss.read_index(idx_path)
            with open(settings.metadata_path, 'r', encoding='utf-8') as f:
                self.chunks = json.load(f)
        else:
            self.index_documents()

    def query(self, question: str, top_k: int = 5) -> List[SourceChunk]:
        '''Busca chunks mais relevantes para a pergunta.'''
        if self.index is None or len(self.chunks) == 0:
            return []
        q_emb = self.model.encode([question])
        q_emb = np.array(q_emb).astype('float32')
        faiss.normalize_L2(q_emb)
        scores, indices = self.index.search(q_emb, top_k)
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < 0: continue
            chunk = self.chunks[idx]
            results.append(SourceChunk(
                content=chunk['text'][:400],
                source=chunk['source'],
                page=chunk['page'],
                score=float(score)
            ))
        return results
    
    async def generate_answer(self, question: str, context_chunks: List[SourceChunk]) -> str:
        '''Chama Ollama local para gerar resposta com contexto.'''
        context = '\n\n'.join([
            f'[Fonte: {c.source}, p.{c.page}]\n{c.content}'
            for c in context_chunks
        ])
        
        prompt = fprompt = f"""Você é um assistente especializado em documentação empresarial e institucional.
Sua função é responder perguntas dos colaboradores com base exclusivamente nos documentos fornecidos.

## CONTEXTO DOS DOCUMENTOS
{context}

## PERGUNTA
{question}

## INSTRUÇÕES DE RESPOSTA
- Leia TODO o contexto antes de responder — a resposta pode estar distribuída em múltiplos trechos
- Responda em texto corrido, de forma clara e completa, sem tópicos ou marcadores
- Sempre cite a fonte (nome do arquivo e página) ao mencionar uma informação, por exemplo: "Conforme o Manual de Estágio (p. 27)..."
- Se diferentes documentos trouxerem informações complementares, integre-as em uma resposta coesa
- Se a informação não estiver no contexto, responda exatamente: "Informação não encontrada nos documentos."
- Nunca invente, suponha ou complemente com conhecimento externo
- Não repita a pergunta nem faça introduções desnecessárias — vá direto à resposta

## RESPOSTA
"""
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f'{settings.ollama_base_url}/api/generate',
                json={
                    'model': settings.ollama_model,
                    'prompt': prompt, 
                    'stream': False
                }
            )
            return resp.json().get('response', 'Erro ao gerar resposta.')