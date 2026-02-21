from app.ingestion.document_loader import DocumentLoader
from app.ingestion.chunker import TextChunker
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_store import VectorStore
from app.retrieval.hybrid_retriever import HybridRetriever
from app.llm.prompt_builder import build_prompt
from app.llm.local_llm import LocalLLM

# Build vector store
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

prompt = build_prompt(query, results["graph_context"], results["vector_context"])

llm = LocalLLM()
answer = llm.generate(prompt)

print("\nFINAL ANSWER:\n")
print(answer)
