from graph_rag.core.graph.neptune_client import NeptuneClient
from graph_rag.core.graph.reasoner import GraphReasoner
from graph_rag.core.vector.faiss_store import FAISSVectorStore
from graph_rag.core.retrieval.hybrid_engine import HybridRetrievalEngine
from graph_rag.core.ranking.hybrid_ranker import HybridRanker

from app.retrieval.embedding_service import EmbeddingService
from app.ingestion.entity_extractor import EntityExtractor

# Setup graph client
endpoint = "ws://localhost:8182/gremlin"
client = NeptuneClient(endpoint)
reasoner = GraphReasoner(client)

# Setup vector store
vector_store = FAISSVectorStore(dimension=384)
embedder = EmbeddingService()
ranker = HybridRanker(alpha=0.6, beta=0.4)

# Add sample document
sample_text = "Amazon Neptune integrates with Bedrock for AI applications."
vector_store.add(embedder.embed(sample_text), sample_text)

# Build engine
engine = HybridRetrievalEngine(
    reasoner=reasoner, vector_store=vector_store, embedder=embedder, ranker=ranker
)

# Extract entities from query
extractor = EntityExtractor()
query = "How does Amazon Neptune integrate with Bedrock?"
entities = extractor.extract(query)

# Retrieve
result = engine.retrieve(query, entities)

print("\nRanked Results:")
for r in result["ranked_results"]:
    print(r)

import json

print("\nFull Engine Output:\n")
print(json.dumps(result, indent=4))
