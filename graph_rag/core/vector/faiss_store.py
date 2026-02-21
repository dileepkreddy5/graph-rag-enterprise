import faiss
import numpy as np
from typing import List, Tuple


class FAISSVectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embedding, text: str):
        vector = np.array([embedding]).astype("float32")
        self.index.add(vector)
        self.documents.append(text)

    def search(self, embedding, k=5) -> List[Tuple[str, float]]:
        vector = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(vector, k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.documents):
                results.append((self.documents[idx], float(dist)))

        return results
