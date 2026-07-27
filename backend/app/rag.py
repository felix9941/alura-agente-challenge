"""
RAG Service

Este módulo orquesta el flujo de Retrieval-Augmented Generation conectando
la base vectorial ChromaDB con el modelo Gemini.
"""

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from app.ingestion.vectorstore import VectorStoreService
from app.models.llm import LLMService
from app.prompts import qa_prompt


class RAGService:
    """Servicio encargado de orquestar la consulta y generación de respuesta."""

    def __init__(self):
        # 1. Obtenemos el modelo Gemini
        self.llm = LLMService().get_llm()

        # 2. Obtenemos el retriever desde nuestro servicio de ChromaDB
        self.retriever = VectorStoreService().get_retriever(search_kwargs={"k": 4})

        # 3. Encadenamos las instrucciones (prompt) y el modelo (LLM)
        self.document_chain = create_stuff_documents_chain(self.llm, qa_prompt)

        # 4. Unimos la búsqueda en la base vectorial con la cadena de documentos
        self.rag_chain = create_retrieval_chain(self.retriever, self.document_chain)

    def answer_question(self, question: str) -> dict:
        """
        Procesa la consulta ingresada por el usuario.

        Parameters
        ----------
        question : str

        Returns
        -------
        dict
            Diccionario que contiene la respuesta y opcionalmente las fuentes.
        """
        try:
            response = self.rag_chain.invoke({"input": question})
            return {
                "answer": response["answer"],
                # 'context' contiene la lista de documentos recuperados de ChromaDB por si deseas auditoría/fuentes
                "sources": [doc.metadata for doc in response.get("context", [])]
            }
        except Exception as e:
            return {
                "answer": f"Error al procesar la consulta en el flujo RAG: {str(e)}",
                "sources": []
            }