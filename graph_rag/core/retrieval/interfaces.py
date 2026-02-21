from typing import Protocol, List, Dict


class Retriever(Protocol):
    def retrieve(self, query: str, k: int = 5) -> Dict: ...


class Ranker(Protocol):
    def rank(self, query: str, candidates: List[Dict]) -> List[Dict]: ...
