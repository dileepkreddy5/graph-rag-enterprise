from typing import List
from graph_rag.core.retrieval.schemas import RetrievalResult, VectorResult, GraphPath


class HybridRanker:
    def __init__(self, alpha: float = 0.6, beta: float = 0.4):
        self.alpha = alpha
        self.beta = beta

    def normalize_vector_scores(
        self, results: List[VectorResult]
    ) -> List[VectorResult]:
        if not results:
            return results

        max_score = max(r.similarity_score for r in results)
        min_score = min(r.similarity_score for r in results)

        if max_score == min_score:
            # Avoid division by zero — assign uniform score
            for r in results:
                r.similarity_score = 1.0
            return results

        for r in results:
            r.similarity_score = (r.similarity_score - min_score) / (
                max_score - min_score
            )

        return results

    def aggregate_graph_score(self, graph_paths: List[GraphPath]) -> float:
        if not graph_paths:
            return 0.0

        weighted_scores = []

        for path in graph_paths:
            # Depth decay — shorter paths are stronger
            depth_decay = 1.0 / path.hop_count
            weighted_scores.append(path.score * depth_decay)

        return sum(weighted_scores) / len(weighted_scores)

    def rank(self, retrieval_result: RetrievalResult):

        normalized_vectors = self.normalize_vector_scores(
            retrieval_result.vector_results
        )

        graph_score = self.aggregate_graph_score(retrieval_result.graph_paths)

        unique_texts = set()
        ranked = []

        for vector in normalized_vectors:
            if vector.text in unique_texts:
                continue

            unique_texts.add(vector.text)

            final_score = self.alpha * vector.similarity_score + self.beta * graph_score

            ranked.append(
                {
                    "text": vector.text,
                    "vector_score": vector.similarity_score,
                    "graph_score": graph_score,
                    "final_score": final_score,
                }
            )

        ranked.sort(key=lambda x: x["final_score"], reverse=True)

        return ranked
