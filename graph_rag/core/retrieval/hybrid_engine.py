import time
from typing import List, Dict

from graph_rag.core.graph.reasoner import GraphReasoner
from graph_rag.core.vector.faiss_store import FAISSVectorStore
from graph_rag.core.ranking.hybrid_ranker import HybridRanker
from graph_rag.core.retrieval.schemas import RetrievalResult, VectorResult


class HybridRetrievalEngine:
    def __init__(
        self,
        reasoner: GraphReasoner,
        vector_store: FAISSVectorStore,
        embedder,
        ranker: HybridRanker,
    ):
        self.reasoner = reasoner
        self.vector_store = vector_store
        self.embedder = embedder
        self.ranker = ranker

    def retrieve(self, query: str, entities: List[str]) -> Dict:

        total_start = time.time()

        # ----------------------------
        # Graph Expansion Phase
        # ----------------------------
        graph_start = time.time()

        graph_paths = []
        seen_paths = set()

        for entity in entities:
            expanded = self.reasoner.expand(entity)
            for path in expanded:
                key = tuple(path.nodes)
                if key not in seen_paths:
                    seen_paths.add(key)
                    graph_paths.append(path)

        MAX_GRAPH_PATHS = 20
        graph_paths = graph_paths[:MAX_GRAPH_PATHS]

        graph_end = time.time()

        # ----------------------------
        # Vector Retrieval Phase
        # ----------------------------
        vector_start = time.time()

        embedding = self.embedder.embed(query)
        vector_hits = self.vector_store.search(embedding)

        vector_results = [
            VectorResult(text=text, similarity_score=score)
            for text, score in vector_hits
        ]

        vector_end = time.time()

        # ----------------------------
        # Build Retrieval Object
        # ----------------------------
        retrieval_result = RetrievalResult(
            query=query,
            extracted_entities=entities,
            graph_paths=graph_paths,
            vector_results=vector_results,
        )

        # ----------------------------
        # Ranking Phase
        # ----------------------------
        ranking_start = time.time()

        ranked = self.ranker.rank(retrieval_result)

        ranking_end = time.time()

        # ----------------------------
        # Confidence Score
        # ----------------------------
        confidence = ranked[0]["final_score"] if ranked else 0.0

        total_end = time.time()

        # ----------------------------
        # Latency Breakdown (ms)
        # ----------------------------
        latency = {
            "total_ms": round((total_end - total_start) * 1000, 2),
            "graph_ms": round((graph_end - graph_start) * 1000, 2),
            "vector_ms": round((vector_end - vector_start) * 1000, 2),
            "ranking_ms": round((ranking_end - ranking_start) * 1000, 2),
        }

        return {
            "query": query,
            "entities": entities,
            "top_result": ranked[0] if ranked else None,
            "ranked_results": ranked,
            "confidence": round(confidence, 4),
            "latency": latency,
            "graph_paths": [
                {"nodes": path.nodes, "hop_count": path.hop_count, "score": path.score}
                for path in graph_paths
            ],
        }
