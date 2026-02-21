from typing import List
from graph_rag.core.graph.neptune_client import NeptuneClient
from graph_rag.core.retrieval.schemas import GraphPath


class GraphReasoner:
    def __init__(self, client: NeptuneClient, max_hops: int = 2):
        self.client = client
        self.max_hops = max_hops

    def expand(self, entity: str) -> List[GraphPath]:
        neighbors = self.client.get_neighbors(entity)

        paths = []
        for neighbor in neighbors:
            path = GraphPath(
                nodes=[entity, neighbor],
                score=1.0 / 1,  # simple scoring for now
                hop_count=1,
            )
            paths.append(path)

        return paths
