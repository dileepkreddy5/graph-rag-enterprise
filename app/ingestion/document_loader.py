from pathlib import Path
from app.utils.logger import get_logger

logger = get_logger(__name__)


class DocumentLoader:
    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load_documents(self):
        documents = []

        for file_path in self.directory.glob("*.txt"):
            logger.info(f"Loading file: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append({"filename": file_path.name, "content": f.read()})

        return documents
