import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector
from app.embedding import get_query_embedding
from app.bm25 import bm25_search
from app.models import PaperModel

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/papers")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Paper:
    def __init__(self, id, title, abstract, authors):
        self.id = id
        self.title = title
        self.abstract = abstract
        self.authors = authors

def get_top_k_semantic(query_emb, top_k=5):
    with engine.connect() as conn:
        sql = text(
            "SELECT id, title, abstract, authors FROM papers ORDER BY embedding <-> (:query_emb::vector) LIMIT :top_k"
        )
        result = conn.execute(sql, {"query_emb": query_emb.astype(float).tolist(), "top_k": top_k})
        papers = [PaperModel(id=row[0], title=row[1], abstract=row[2], authors=row[3]) for row in result]
    return papers

def get_top_k_bm25(query, top_k=5):
    return bm25_search(query, top_k)