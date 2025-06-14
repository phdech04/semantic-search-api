import json
import os
from sqlalchemy import create_engine, text
from app.embedding import get_query_embedding

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/papers")
engine = create_engine(DATABASE_URL)

def create_table():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS papers (
                id SERIAL PRIMARY KEY,
                title TEXT,
                abstract TEXT,
                authors TEXT,
                embedding vector(384)
            );
        """))
        conn.commit()

def ingest():
    with open("data/sample_papers.json", "r") as f:
        papers = json.load(f)
    with engine.connect() as conn:
        for paper in papers:
            emb = get_query_embedding(paper["abstract"])
            conn.execute(
                text("INSERT INTO papers (title, abstract, authors, embedding) VALUES (:title, :abstract, :authors, :embedding)"),
                {
                    "title": paper["title"],
                    "abstract": paper["abstract"],
                    "authors": paper["authors"],
                    "embedding": emb.tolist()
                }
            )
        conn.commit()

if __name__ == "__main__":
    create_table()
    ingest()
    print("Ingestion complete.")