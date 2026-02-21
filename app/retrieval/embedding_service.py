from sentence_transformers import SentenceTransformer
from app.utils.logger import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str):
        logger.info("Generating embedding")
        return self.model.encode(text)
