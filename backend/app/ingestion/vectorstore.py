"""
Vector Store Service

Este módulo crea y administra la base vectorial utilizando ChromaDB.
"""

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import VECTORSTORE_PATH
from app.ingestion.embeddings import EmbeddingService


class VectorStoreService:
    """
    Servicio encargado de crear y acceder a la base vectorial.
    """

    def __init__(self):

        self.embedding_function = (
            EmbeddingService().get_embeddings()
        )

        self.persist_directory = str(VECTORSTORE_PATH)

    def create_vectorstore(
        self,
        documents: list[Document],
    ) -> Chroma:
        """
        Crea una nueva base vectorial a partir de una lista de documentos.

        Parameters
        ----------
        documents : list[Document]

        Returns
        -------
        Chroma
        """

        if not documents:
            raise ValueError(
                "No hay documentos para indexar."
            )

        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_function,
            persist_directory=self.persist_directory,
        )

        return vectorstore

    def load_vectorstore(self) -> Chroma:
        """
        Carga una base vectorial existente.

        Returns
        -------
        Chroma
        """

        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_function,
        )