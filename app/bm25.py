from rank_bm25 import BM25Okapi
import json

# Load papers into memory (for demo)
with open("data/sample_papers.json", "r") as f:
    papers = json.load(f)

corpus = [paper["abstract"] for paper in papers]
bm25 = BM25Okapi([doc.split() for doc in corpus])

def bm25_search(query, top_k=5):
    scores = bm25.get_scores(query.split())
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    results = []
    for idx in top_indices:
        paper = papers[idx]
        results.append({
            "id": paper["id"],
            "title": paper["title"],
            "abstract": paper["abstract"],
            "authors": paper["authors"]
        })
    return results