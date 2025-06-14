from fastapi import FastAPI, Query
from app.embedding import get_query_embedding
from app.db import get_top_k_semantic, get_top_k_bm25, Paper
from app.models import SearchResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Semantic Search API is running."}

@app.get("/search/semantic", response_model=SearchResponse)
def semantic_search(query: str = Query(...), top_k: int = 5):
    query_emb = get_query_embedding(query)
    results = get_top_k_semantic(query_emb, top_k)
    return SearchResponse(results=results)

@app.get("/search/bm25", response_model=SearchResponse)
def bm25_search(query: str = Query(...), top_k: int = 5):
    results = get_top_k_bm25(query, top_k)
    return SearchResponse(results=results)