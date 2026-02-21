from graph_rag.core.retrieval.hybrid_engine import HybridRetrievalEngine
from graph_rag.core.vector.faiss_store import FAISSVectorStore
from graph_rag.core.ranking.hybrid_ranker import HybridRanker
from app.retrieval.embedding_service import EmbeddingService
from app.ingestion.entity_extractor import EntityExtractor


def build_engine():

    # Setup vector store
    vector_store = FAISSVectorStore(dimension=384)
    embedder = EmbeddingService()
    ranker = HybridRanker(alpha=0.6, beta=0.4)

    # Add sample document
    sample_text = "Amazon Neptune integrates with Bedrock for AI applications."
    vector_store.add(embedder.embed(sample_text), sample_text)

    # Create dummy reasoner (no graph dependency for benchmark)
    class DummyReasoner:
        def expand(self, entity):
            return []

    reasoner = DummyReasoner()

    engine = HybridRetrievalEngine(
        reasoner=reasoner,
        vector_store=vector_store,
        embedder=embedder,
        ranker=ranker
    )

    extractor = EntityExtractor()
    query = "How does Amazon Neptune integrate with Bedrock?"
    entities = extractor.extract(query)

    return engine, query, entities
