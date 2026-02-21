from gremlin_python.driver import client
from app.config.settings import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


class NeptuneClient:
    def __init__(self):
        self.client = client.Client(settings.NEPTUNE_ENDPOINT, "g")

    def submit(self, query: str):
        logger.info(f"Executing Gremlin Query: {query}")
        return self.client.submit(query)

    def close(self):
        self.client.close()
