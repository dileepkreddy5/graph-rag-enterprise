from gremlin_python.driver import client
from app.config.settings import settings

gremlin_client = client.Client(settings.NEPTUNE_ENDPOINT, "g")

result = gremlin_client.submit("g.V().count()").all().result()
print("Vertex Count:", result)
