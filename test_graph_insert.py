from app.ingestion.graph_builder import GraphBuilder

builder = GraphBuilder()

builder.add_entity("AWS")
builder.add_entity("Amazon Neptune")
builder.add_entity("Bedrock")

builder.add_relationship("Amazon Neptune", "integrates_with", "Bedrock")
builder.add_relationship("AWS", "provides", "Amazon Neptune")

print("Graph insert complete.")
