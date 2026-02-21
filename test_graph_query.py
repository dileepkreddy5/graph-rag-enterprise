from app.ingestion.graph_client import NeptuneClient

client = NeptuneClient()

print("\nVertices:")
vertices = client.submit("g.V().valueMap(true)").all().result()
print(vertices)

print("\nEdges:")
edges = client.submit("g.E().valueMap(true)").all().result()
print(edges)
