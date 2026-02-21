from app.ingestion.document_loader import DocumentLoader
from app.ingestion.chunker import TextChunker
from app.ingestion.entity_extractor import EntityExtractor

loader = DocumentLoader("data")
docs = loader.load_documents()

chunker = TextChunker(chunk_size=200, overlap=0)
extractor = EntityExtractor()

for doc in docs:
    chunks = chunker.chunk(doc)
    for chunk in chunks:
        print("\nChunk:")
        print(chunk["content"])
        entities = extractor.extract(chunk["content"])
        print("Entities:", entities)
