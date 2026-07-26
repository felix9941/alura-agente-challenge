"""
Document Loader

Este módulo se encarga de cargar todos los documentos
almacenados en la carpeta data.

Actualmente soporta:
- PDF
- CSV

Devuelve una lista de objetos Document de LangChain.
"""

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
)

from app.config import DATA_PATH

# Registro de loaders soportados
LOADERS = {
    ".pdf": PyPDFLoader,
    ".csv": CSVLoader,
}


class DocumentLoader:
    """Carga todos los documentos de la carpeta data."""

    def __init__(self):
        self.data_path = DATA_PATH

    def load_documents(self) -> list[Document]:
        """
        Carga todos los documentos soportados.

        Returns
        -------
        list[Document]
            Lista de documentos de LangChain.
        """

        documents = []

        files = sorted(self.data_path.iterdir())

        if not files:
            raise FileNotFoundError(
                f"No se encontraron archivos en {self.data_path}"
            )

        for file in files:

            extension = file.suffix.lower()

            if extension not in LOADERS:
                continue

            loader_class = LOADERS[extension]

            if extension == ".csv":
                loader = loader_class(file_path=str(file))
            else:
                loader = loader_class(str(file))

            documents.extend(loader.load())

        return documents