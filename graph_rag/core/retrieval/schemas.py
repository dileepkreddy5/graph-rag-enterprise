from dataclasses import dataclass
from typing import List


@dataclass
class GraphPath:
    nodes: List[str]
    score: float
    hop_count: int


@dataclass
class VectorResult:
    text: str
    similarity_score: float


@dataclass
class RetrievalResult:
    query: str
    extracted_entities: List[str]
    graph_paths: List[GraphPath]
    vector_results: List[VectorResult]
