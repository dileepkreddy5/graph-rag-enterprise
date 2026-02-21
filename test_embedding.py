from app.retrieval.embedding_service import EmbeddingService

embedder = EmbeddingService()

vector = embedder.embed("Amazon Neptune integrates with Bedrock")

print("Vector length:", len(vector))
