from app.ingestion.document_loader import DocumentLoader
from app.ingestion.chunker import TextChunker

loader = DocumentLoader("data")
docs = loader.load_documents()

chunker = TextChunker(chunk_size=80, overlap=20)

for doc in docs:
    chunks = chunker.chunk(doc)
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:")
        print(chunk["content"])
