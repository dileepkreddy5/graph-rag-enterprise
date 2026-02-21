from app.ingestion.document_loader import DocumentLoader
from app.ingestion.chunker import TextChunker
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_store import VectorStore
from app.retrieval.hybrid_retriever import HybridRetriever

# Build vector store from chunks
loader = DocumentLoader("data")
docs = loader.load_documents()

chunker = TextChunker(chunk_size=200, overlap=0)
embedder = EmbeddingService()
store = VectorStore(dimension=384)

for doc in docs:
    chunks = chunker.chunk(doc)
    for chunk in chunks:
        vector = embedder.embed(chunk["content"])
        store.add(vector, {"text": chunk["content"]})

retriever = HybridRetriever(store)

query = "How does Amazon Neptune integrate with Bedrock?"

results = retriever.retrieve(query)

print("\nEntities:", results["entities"])
print("\nGraph Context:", results["graph_context"])
print("\nVector Context:")
for item in results["vector_context"]:
    print(item)
