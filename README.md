

## 💼 DocAssistant - O Sistema de busca inteligente em documentos da sua empresa
<p align="justify">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Node.js-18+-339933?logo=nodedotjs&logoColor=white" alt="Node.js 18+">
  <img src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB" alt="React">
  <img src="https://img.shields.io/badge/Vite-B73BFE?logo=vite&logoColor=FFD62E" alt="Vite">
  <img src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Ollama-000000?logo=ollama&logoColor=white" alt="Ollama">
</p>
**Sistema RAG para busca inteligente em documentação empresarial com IA 100% local.**

<img width="1882" height="909" alt="Captura de tela 2026-02-17 214919" src="https://github.com/user-attachments/assets/30c76cab-a60e-41e6-9b27-ce3c6902de99" />


---

## 📖 Sobre o Projeto

Empresas possuem centenas de documentos internos — manuais de RH, políticas de compliance, guias técnicos, procedimentos operacionais — espalhados em drives e sistemas. Funcionários perdem tempo valioso procurando informações básicas, sobrecarregando equipes de suporte com perguntas repetitivas.

O **Documentation Assistant** foi criado para resolver este problema. Utilizando uma arquitetura de **Geração Aumentada por Recuperação (RAG)**, este sistema transforma sua documentação em uma base de conhecimento interativa. Funcionários fazem perguntas em linguagem natural e recebem respostas precisas, com citação automática das fontes (documento + página), geradas por um modelo de linguagem local (Mistral 7B via Ollama) que garante total privacidade dos dados corporativos.

**Ideal para:** Onboarding de novos funcionários, suporte ao RH/TI, compliance interno, e qualquer cenário onde documentação precisa ser acessível e auditável.

---

## ✨ Funcionalidades Principais

- 💬 **Consultas em Linguagem Natural:** "Como solicitar férias?" ou "Qual a política de home office?" — pergunte como se estivesse conversando com um colega.
- 🎯 **Respostas Baseadas em Fontes:** Todas as respostas são construídas a partir de trechos relevantes extraídos dos seus documentos, evitando "alucinações" da IA.
- 🔍 **Visualização das Fontes:** Cada resposta mostra exatamente qual documento (e página) foi usado, permitindo auditoria completa.
- 📤 **Upload Simples de PDFs:** Interface para adicionar novos documentos que são automaticamente indexados.
- 🔒 **Arquitetura 100% Local:** LLM, embeddings e dados ficam no seu servidor. Nenhuma informação é enviada para APIs externas — perfeito para dados sensíveis e conformidade com LGPD.

---

## 🛠️ Tecnologias Utilizadas

**Backend:**
- **API Framework:** FastAPI
- **Orquestração RAG:** LangChain
- **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Vector Store:** FAISS (Facebook AI Similarity Search)
- **LLM Local:** Ollama + Mistral 7B
- **Processamento de PDFs:** PyPDF

**Frontend:**
- **Framework:** React + Vite
- **HTTP Client:** Axios
- **Estilização:** CSS moderno com design responsivo

**Infraestrutura:**
- **Linguagem:** Python 3.11+ | Node.js 18+
- **Containerização:** Docker (opcional)

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- [Ollama instalado](https://ollama.com/download)
- Git

### 1. Clone o Repositório
```bash
git clone https://github.com/hugo-ryanf/documentation-assistant.git
cd documentation-assistant
```

### 2. Configuração do Backend
```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configurar LLM Local (Ollama)
```bash
# Baixar modelo Mistral (a primeira vez exige download de ~4GB)
ollama pull mistral

# Verificar instalação
ollama list
```

### 4. Iniciar o Backend
```bash
# Na pasta backend/ com venv ativado:
uvicorn app.main:app --reload
```
- A API estará disponível em: `http://localhost:8000`
- Documentação interativa (Swagger): `http://localhost:8000/docs`

### 5. Configuração do Frontend
Em um **novo terminal**:
```bash
cd frontend

# Instalar dependências
npm install

# Iniciar aplicação
npm run dev
```
- A Interface web estará disponível em: `http://localhost:5173`

### 6. Upload de Documentos e Uso
1. Acesse `http://localhost:5173`
2. Faça upload de PDFs (manuais, políticas, guias internos).
3. Aguarde a indexação automática.
4. Digite sua pergunta: *"Como solicitar reembolso?"*
5. Receba a resposta com as fontes citadas!

---

## 📁 Estrutura do Projeto

```text
documentation-assistant/
├── backend/
│   ├── app/
│   │   ├── main.py              # Endpoints FastAPI
│   │   ├── rag_engine.py        # Motor RAG (indexação + busca)
│   │   ├── models.py            # Modelos Pydantic
│   │   └── config.py            # Configurações (paths, modelos)
│   ├── data/
│   │   ├── documentos/          # PDFs carregados (não versionado)
│   │   ├── faiss_index/         # Índice vetorial (não versionado)
│   │   └── metadata.json        # Metadados dos chunks
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # Componente principal
│   │   ├── components/
│   │   │   ├── ChatInterface.jsx
│   │   │   ├── SearchBar.jsx
│   │   │   └── SourceViewer.jsx
│   │   └── services/
│   │       └── api.js           # Client HTTP (Axios)
│   ├── package.json
│   └── vite.config.js
├── docs/
│   └── screenshot.png           # Print da aplicação
├── tests/                       # Testes automatizados
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🎯 Casos de Uso

**Recursos Humanos**
- "Qual o processo para solicitar férias?"
- "Como funciona o reembolso de despesas?"
- "Qual a política de home office?"

**TI e Suporte Técnico**
- "Como resetar a senha da VPN?"
- "Qual o procedimento para solicitar novo equipamento?"
- "Qual a política de backup de dados?"

**Compliance e Jurídico**
- "Quais são as diretrizes de LGPD da empresa?"
- "Quais são as normas de segurança da informação?"
- "Qual o procedimento para tratamento de dados pessoais?"

**Operações**
- "Manual de uso do sistema X"
- "Checklist de abertura de loja"
- "SOPs de atendimento ao cliente"

---

## 🔒 Privacidade e Segurança

**Por que 100% local é importante:**
- ✅ **Conformidade LGPD:** Dados sensíveis nunca saem do servidor da empresa.
- ✅ **Sem vazamentos:** Nenhuma pergunta ou documento é enviado para OpenAI, Anthropic ou qualquer API externa.
- ✅ **Auditabilidade completa:** Toda resposta cita a fonte exata, permitindo verificação.
- ✅ **Controle total:** Você escolhe quais documentos indexar e quando atualizá-los.
- ✅ **Sem custos recorrentes:** Sem cobrança por tokens ou chamadas de API.

**Arquitetura de privacidade:**
- LLM roda via Ollama (local).
- Embeddings gerados localmente (Sentence-Transformers).
- Vector store armazenado em disco (FAISS).
- PDFs permanecem no servidor.

---

## 📊 Performance

Benchmarks típicos *(hardware médio - Intel i5, 16GB RAM)*:

| Operação | Tempo Estimado |
| :--- | :--- |
| Indexação de 1 PDF (20 páginas) | ~15-30s |
| Busca vetorial (top 5 chunks) | ~200ms |
| Geração de resposta (LLM) | ~3-8s |
| **Total por pergunta** | **~4-10s** |

**Otimizações possíveis:**
- GPU acceleration (Ollama com CUDA).
- Cache de respostas frequentes.
- FAISS GPU para datasets grandes (10k+ documentos).

---

## 🗺️ Roadmap

**v1.0 (Atual)**
- [x] RAG básico funcionando
- [x] Upload de PDFs
- [x] Interface web React
- [x] Citação de fontes

**v1.1 (Próximo)**
- [ ] Upload via drag & drop na interface
- [ ] Autenticação de usuários
- [ ] Histórico de conversas
- [ ] Feedback (útil/não útil)

**v2.0 (Futuro)**
- [ ] Suporte a múltiplos formatos (DOCX, TXT, HTML)
- [ ] Categorização automática de documentos
- [ ] Dashboard de analytics (perguntas mais frequentes)
- [ ] Modo admin para gestão de documentos
- [ ] API de integração (Slack, Teams, WhatsApp)

---
## 👤 Autor

**Hugo Ryan**
- GitHub: [@hugo-ryanf](https://github.com/hugo-ryanf)
- LinkedIn: [@hugo-ryan](https://www.linkedin.com/in/hugo-ryan-9b5621201/)
- Email: [@hugoryanf](hugoryanf@gmail.com)
