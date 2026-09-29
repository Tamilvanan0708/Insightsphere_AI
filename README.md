# InsightSphere AI

AI-powered market research platform that discovers sources, extracts content, retrieves evidence, and generates cited research reports.

## Project Structure

```text
├── app/
│   ├── api/            # FastAPI routes and endpoints
│   ├── agents/         # Google ADK agent orchestration
│   ├── tools/          # Custom deterministic tools & schemas
│   ├── extraction/     # Web scraping, Playwright, PDF, Tables
│   ├── rag/            # Embeddings, Qdrant vector DB, BM25, Reranker
│   ├── db/             # PostgreSQL models and Alembic migrations
│   ├── worker/         # Background job processor
│   ├── observability/  # Tracing, latency and token metrics
│   └── security/       # URL guard, SSRF defense, sanitizers
├── eval/               # Evaluation datasets and retrieval benchmarks
└── tests/              # Unit and integration test suites
```

## Team Responsibilities

- **Data Extraction & Storage**: Tamilvanan (@tamilvanan)
- **AI Validation & Prompt Engineering**: Shahidha (@shahidha)
- **RAG & Vector Search**: James (@james)
- **API & Agent Orchestration**: Sivaprakash (@sivaprakash)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Tamilvanan0708/Insightsphere_AI.git
cd Insightsphere_AI

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (Story 2)
pip install -r requirements.txt
```
