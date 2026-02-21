from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_store import VectorStore

embedder = EmbeddingService()
store = VectorStore(dimension=384)

texts = [
    "Amazon Neptune is a graph database",
    "Amazon Bedrock provides foundation models",
    "Neptune integrates with Bedrock",
]

# Add documents
for text in texts:
    vector = embedder.embed(text)
    store.add(vector, {"text": text})

# Query
query = "How does Neptune work with Bedrock?"
query_vector = embedder.embed(query)

results = store.search(query_vector, k=2)

print("\nTop Results:")
for r in results:
    print(r)
