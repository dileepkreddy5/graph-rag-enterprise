import re
from typing import List
from app.utils.logger import get_logger

logger = get_logger(__name__)


class EntityExtractor:
    def __init__(self):
        self.pattern = r"\b([A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*)\b"
        self.stop_words = {"How", "What", "Why", "When", "Where", "Who"}

    def extract(self, text: str) -> List[str]:
        matches = re.findall(self.pattern, text)

        seen = set()
        entities = []

        for m in matches:
            if m not in seen and m not in self.stop_words and len(m) > 2:
                seen.add(m)
                entities.append(m)

        logger.info(f"Extracted entities: {entities}")
        return entities
