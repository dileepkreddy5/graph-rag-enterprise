from app.ingestion.document_loader import DocumentLoader

loader = DocumentLoader("data")
docs = loader.load_documents()

print(docs)
