"""
Document Splitter

Este módulo divide los documentos cargados en fragmentos
(chunks) para optimizar el proceso de embeddings y recuperación.

Utiliza RecursiveCharacterTextSplitter de LangChain.
"""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_SIZE, CHUNK_OVERLAP


class DocumentSplitter:
    """
    Divide una lista de documentos en chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Divide los documentos recibidos.

        Parameters
        ----------
        documents : list[Document]

        Returns
        -------
        list[Document]
        """

        if not documents:
            raise ValueError(
                "La lista de documentos está vacía."
            )

        chunks = self.splitter.split_documents(documents)

        return chunks