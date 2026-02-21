from itertools import combinations
from app.ingestion.graph_builder import GraphBuilder
from app.ingestion.entity_extractor import EntityExtractor
from app.utils.logger import get_logger

logger = get_logger(__name__)


class GraphIngestor:
    def __init__(self):
        self.builder = GraphBuilder()
        self.extractor = EntityExtractor()

    def ingest_chunk(self, chunk: dict):
        text = chunk["content"]

        entities = self.extractor.extract(text)

        # Add entities
        for entity in entities:
            self.builder.add_entity(entity)

        # Create co-occurrence relationships
        for e1, e2 in combinations(entities, 2):
            self.builder.add_relationship(e1, "co_occurs_with", e2)

        logger.info("Chunk ingestion complete.")
