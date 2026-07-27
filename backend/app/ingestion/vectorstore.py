"""
Vector Store Service

Este módulo crea y administra la base vectorial utilizando ChromaDB.
"""

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import VECTORSTORE_PATH, TOP_K_RESULTS
from app.ingestion.embeddings import EmbeddingService


class VectorStoreService:
    """
    Servicio encargado de crear, cargar y consultar la base vectorial.
    """

    def __init__(self):

        self.embedding_function = EmbeddingService().get_embeddings()

        self.persist_directory = str(VECTORSTORE_PATH)

    def create_vectorstore(
        self,
        documents: list[Document],
    ) -> Chroma:
        """
        Crea una nueva base vectorial.

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

    def get_retriever(
        self,
        search_kwargs: dict | None = None,
    ):
        """
        Devuelve un retriever para realizar búsquedas semánticas.

        Parameters
        ----------
        search_kwargs : dict | None

        Returns
        -------
        VectorStoreRetriever
        """

        if search_kwargs is None:
            search_kwargs = {
                "k": TOP_K_RESULTS
            }

        vectorstore = self.load_vectorstore()

        return vectorstore.as_retriever(
            search_kwargs=search_kwargs
        )