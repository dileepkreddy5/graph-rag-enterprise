from typing import List, Dict
from app.utils.logger import get_logger
import re

logger = get_logger(__name__)


class TextChunker:
    def __init__(self, chunk_size: int = 300, overlap: int = 1):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_sentences(self, text: str) -> List[str]:
        sentences = re.split(r"(?<=[.!?])\s+", text.strip())
        return [s.strip() for s in sentences if s.strip()]

    def chunk(self, document: Dict) -> List[Dict]:
        sentences = self.split_sentences(document["content"])
        filename = document["filename"]

        chunks = []
        i = 0

        while i < len(sentences):
            current_chunk = []
            current_length = 0
            j = i

            while (
                j < len(sentences)
                and current_length + len(sentences[j]) <= self.chunk_size
            ):
                current_chunk.append(sentences[j])
                current_length += len(sentences[j])
                j += 1

            chunks.append({"filename": filename, "content": " ".join(current_chunk)})

            # move window forward
            i = j - self.overlap if self.overlap < j else j

        logger.info(f"Created {len(chunks)} sliding-window chunks from {filename}")
        return chunks
