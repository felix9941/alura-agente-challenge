"""
Embedding Service

Genera embeddings utilizando Google Gemini.

Este servicio será utilizado posteriormente para construir
la base vectorial (ChromaDB).
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL,
)


class EmbeddingService:
    """
    Servicio encargado de generar embeddings.
    """

    def __init__(self):

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            google_api_key=GOOGLE_API_KEY,
        )

    def get_embeddings(self):
        """
        Devuelve la instancia de embeddings.

        Returns
        -------
        GoogleGenerativeAIEmbeddings
        """

        return self.embeddings