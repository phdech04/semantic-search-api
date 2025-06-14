from pydantic import BaseModel
from typing import List

class PaperModel(BaseModel):
    id: int
    title: str
    abstract: str
    authors: str

class SearchResponse(BaseModel):
    results: List[PaperModel]