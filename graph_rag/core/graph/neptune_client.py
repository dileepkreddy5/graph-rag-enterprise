from gremlin_python.driver import client
from typing import List


class NeptuneClient:
    def __init__(self, endpoint: str):
        self.client = client.Client(endpoint, "g")

    def execute(self, query: str):
        return self.client.submit(query).all().result()

    def get_neighbors(self, entity: str) -> List[str]:
        query = f"""
        g.V().has('Entity','name','{entity}')
        .both()
        .values('name')
        """
        return self.execute(query)
