import faiss
import numpy as np
from app.utils.logger import get_logger

logger = get_logger(__name__)


class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embedding, metadata):
        vector = np.array([embedding]).astype("float32")
        self.index.add(vector)
        self.documents.append(metadata)
        logger.info("Added embedding to vector store")

    def search(self, embedding, k=3):
        vector = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(vector, k)

        results = []
        seen = set()

        for idx in indices[0]:
            if idx < len(self.documents):
                doc = self.documents[idx]
                text = doc["text"]

                if text not in seen:
                    seen.add(text)
                    results.append(doc)

        return results
