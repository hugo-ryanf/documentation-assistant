from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    ollama_base_url: str = 'http://localhost:11434'
    ollama_model: str = 'llama3.2'
    embedding_model: str = 'all-MiniLM-L6-v2'
    chunk_size: int = 500
    chunk_overlap: int = 100
    top_k_results: int = 5
    docs_path: str = './data/documentos'
    faiss_index_path: str = './data/faiss_index'
    metadata_path: str = './data/metadata.json'
    class Config:
        env_file = '.env'
settings = Settings()