from typing import List


class RetrievalMetrics:

    @staticmethod
    def precision_at_k(
        relevant_docs: List[str], retrieved_docs: List[str], k: int
    ) -> float:
        retrieved_k = retrieved_docs[:k]
        if not retrieved_k:
            return 0.0

        relevant_count = sum(1 for doc in retrieved_k if doc in relevant_docs)
        return relevant_count / k

    @staticmethod
    def recall_at_k(
        relevant_docs: List[str], retrieved_docs: List[str], k: int
    ) -> float:
        if not relevant_docs:
            return 0.0

        retrieved_k = retrieved_docs[:k]
        relevant_count = sum(1 for doc in retrieved_k if doc in relevant_docs)
        return relevant_count / len(relevant_docs)

    @staticmethod
    def mean_reciprocal_rank(
        relevant_docs: List[str], retrieved_docs: List[str]
    ) -> float:
        for i, doc in enumerate(retrieved_docs):
            if doc in relevant_docs:
                return 1.0 / (i + 1)
        return 0.0

    @staticmethod
    def graph_coverage_score(graph_paths) -> float:
        if not graph_paths:
            return 0.0

        unique_nodes = set()
        for path in graph_paths:
            for node in path.nodes:
                unique_nodes.add(node)

        return len(unique_nodes)
