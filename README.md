\# 💼 Documentation Assistant



Sistema RAG para busca inteligente em documentação empresarial com IA 100% local.



\## 🎯 Funcionalidades



\- ✅ Consultas em linguagem natural

\- ✅ Respostas baseadas em fontes confiáveis

\- ✅ Citação automática de documentos e páginas

\- ✅ 100% Local - privacidade total dos dados

\- ✅ Interface web moderna e responsiva



\## 🛠️ Tecnologias



\*\*Backend:\*\*

\- Python + FastAPI

\- LangChain

\- Sentence-Transformers (embeddings)

\- FAISS (vector database)

\- Ollama + Mistral (LLM local)



\*\*Frontend:\*\*

\- React + Vite

\- Axios



\## 📦 Instalação



\### Pré-requisitos

\- Python 3.11+

\- Node.js 18+

\- Ollama instalado



\### Backend

```bash

cd backend

python -m venv venv



\# Windows

venv\\Scripts\\Activate



\# Mac/Linux

source venv/bin/activate



pip install -r requirements.txt

```



\### LLM Local

```bash

\# Instalar Ollama: https://ollama.com/download

ollama pull mistral

```



\### Frontend

```bash

cd frontend

npm install

```



\## 🚀 Como Usar



\### 1. Iniciar Backend

```bash

cd backend

uvicorn app.main:app --reload

```



API disponível em: http://localhost:8000



\### 2. Iniciar Frontend

```bash

cd frontend

npm run dev

```



Interface em: http://localhost:5173



\### 3. Upload de Documentos



\- Acesse a interface web

\- Faça upload de PDFs (manuais, políticas, guias)

\- Sistema indexa automaticamente



\### 4. Fazer Perguntas



\- Digite sua pergunta em linguagem natural

\- Receba resposta clara com citação das fontes

\- Clique nas fontes para ver documento original



\## 📸 Casos de Uso



\- \*\*RH:\*\* Políticas de férias, home office, benefícios

\- \*\*TI:\*\* Procedimentos técnicos, troubleshooting

\- \*\*Compliance:\*\* Regulamentos internos, normas

\- \*\*Operações:\*\* Manuais de processo, SOPs



\## 🔒 Privacidade e Segurança



\- ✅ Todos os dados processados localmente

\- ✅ Nenhuma informação enviada para APIs externas

\- ✅ LLM roda no próprio servidor (Ollama)

\- ✅ Embeddings gerados localmente

\- ✅ Ideal para dados sensíveis/confidenciais



\## 📁 Estrutura do Projeto

```

documentation-assistant/

├── backend/

│   ├── app/

│   │   ├── main.py          # FastAPI endpoints

│   │   ├── rag\_engine.py    # Sistema RAG

│   │   ├── models.py        # Pydantic models

│   │   └── config.py        # Configurações

│   └── data/

│       ├── documentos/      # PDFs indexados

│       └── faiss\_index/     # Vector database

└── frontend/

&nbsp;   └── src/

&nbsp;       ├── App.jsx          # Componente principal

&nbsp;       └── services/        # API client

```



\## 🎓 Projeto Educacional



Este projeto foi desenvolvido como estudo de:

\- RAG (Retrieval-Augmented Generation)

\- Sistemas de IA corporativos

\- Processamento de linguagem natural

\- Arquitetura de aplicações full-stack



\## 📝 Licença



MIT



\## 👤 Autor



Hugo Ryan - \[GitHub](https://github.com/hugo-ryanf)



