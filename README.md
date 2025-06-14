# Semantic Search API for Research Papers

## Overview

This project is an end-to-end semantic search engine for research papers. It allows users to query a collection of papers in natural language and retrieves the most relevant documents using deep learning embeddings, not just keyword matching.

## Features

- Semantic search using transformer-based embeddings (HuggingFace, PyTorch, pgvector)
- BM25 keyword search baseline
- REST API with FastAPI
- Data ingestion and embedding pipeline
- Dockerized for easy deployment

## Project Structure
semantic-search-api/
├── app/                  # API core
│   ├── api/              # FastAPI route handlers
│   ├── models/           # Pydantic models
│   ├── services/         # Search services (semantic/bm25)
│   └── utils/            # Database & embedding utilities
├── ingest/               # Data pipeline
│   ├── data_loader.py    # Custom ingestion script
│   └── sample_papers.json # Demo dataset
├── infrastructure/       # Deployment configs
│   ├── Dockerfile        # API service
│   ├── docker-compose.yml# Full stack (API + DB)
│   └── init.sql          # DB schema bootstrap
└── tests/                # Test suite
    ├── unit/             # Component tests
    └── integration/      # API endpoint tests


---

## How It Works

1. **Ingestion**: The pipeline loads research papers, generates semantic embeddings using a transformer model, and stores both metadata and embeddings in PostgreSQL with the pgvector extension.
2. **Semantic Search**: Users query the API in natural language. The query is embedded and compared to stored vectors using efficient similarity search.
3. **Keyword Search**: As a baseline, BM25 keyword search is implemented for comparison.
4. **API**: FastAPI exposes endpoints for both semantic and keyword search.
5. **Deployment**: The entire stack can be run locally or in containers using Docker and Docker Compose.

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/phdech04/semantic-search-api.git
cd semantic-search-api
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL and pgvector

- Install PostgreSQL and the pgvector extension.
- Create a database named `papers` and enable the extension:
  ```sh
  createdb papers
  psql -d papers -c "CREATE EXTENSION IF NOT EXISTS vector;"
  ```

### 4. Ingest Data

```sh
python3 -m ingest.ingest
```

### 5. Run the API

```sh
uvicorn app.main:app --reload
```

- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API documentation.

---

## Example API Endpoints

- `GET /search/semantic?query=deep learning&top_k=5`  
  Returns the top 5 most semantically similar papers to the query.
- `GET /search/bm25?query=deep learning&top_k=5`  
  Returns the top 5 papers using BM25 keyword search.

---

## Why This Project?

This project demonstrates the integration of state-of-the-art NLP, scalable databases, and modern deployment techniques. It showcases both machine learning modeling and production engineering skills, making it a strong portfolio piece for roles in data science, machine learning engineering, and backend development.
---

## License

MIT

---