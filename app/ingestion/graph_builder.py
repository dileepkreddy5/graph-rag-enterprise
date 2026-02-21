from app.ingestion.graph_client import NeptuneClient
from app.utils.logger import get_logger

logger = get_logger(__name__)


class GraphBuilder:
    def __init__(self):
        self.client = NeptuneClient()

    def add_entity(self, name: str):
        query = f"""
        g.V().has('Entity','name','{name}')
        .fold()
        .coalesce(
            unfold(),
            addV('Entity').property('name','{name}')
        )
        """
        self.client.submit(query)
        logger.info(f"Entity ensured: {name}")

    def add_relationship(self, source: str, relation: str, target: str):
        query = f"""
        g.V().has('Entity','name','{source}').as('a')
        .V().has('Entity','name','{target}')
        .coalesce(
            inE('{relation}').where(outV().as('a')),
            addE('{relation}').from('a')
        )
        """
        self.client.submit(query)
        logger.info(f"Relationship ensured: {source} -[{relation}]-> {target}")
