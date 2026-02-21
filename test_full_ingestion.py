from app.ingestion.document_loader import DocumentLoader
from app.ingestion.chunker import TextChunker
from app.ingestion.graph_ingestor import GraphIngestor

loader = DocumentLoader("data")
docs = loader.load_documents()

chunker = TextChunker(chunk_size=200, overlap=0)
ingestor = GraphIngestor()

for doc in docs:
    chunks = chunker.chunk(doc)
    for chunk in chunks:
        ingestor.ingest_chunk(chunk)

print("Full ingestion completed.")
