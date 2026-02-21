from app.ingestion.entity_extractor import EntityExtractor
from app.ingestion.graph_client import NeptuneClient
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_store import VectorStore


class HybridRetriever:
    def __init__(self, vector_store: VectorStore):
        self.extractor = EntityExtractor()
        self.graph = NeptuneClient()
        self.embedder = EmbeddingService()
        self.vector_store = vector_store

    def graph_expand(self, entity: str):
        query = f"""
        g.V().has('Entity','name','{entity}')
        .both()
        .values('name')
        """
        result = self.graph.submit(query).all().result()
        return result

    def retrieve(self, query: str, k=3):
        # 1. Entity extraction from query
        entities = self.extractor.extract(query)

        graph_context = []
        for entity in entities:
            expanded = self.graph_expand(entity)
            graph_context.extend(expanded)

        # 2. Vector similarity
        query_vector = self.embedder.embed(query)
        vector_results = self.vector_store.search(query_vector, k=k)

        return {
            "entities": entities,
            "graph_context": list(set(graph_context)),
            "vector_context": vector_results,
        }
