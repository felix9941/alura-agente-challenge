"""
RAG Service

Este módulo implementa el flujo de Retrieval-Augmented Generation (RAG)
utilizando ChromaDB como base vectorial y Gemini como modelo de lenguaje.
"""

from app.ingestion.vectorstore import VectorStoreService
from app.models.llm import LLMService
from app.prompts import qa_prompt


class RAGService:
    """
    Servicio encargado de recuperar contexto y generar respuestas.
    """

    def __init__(self):

        self.llm = LLMService().get_llm()

        self.retriever = VectorStoreService().get_retriever()

    def answer_question(self, question: str) -> dict:
        """
        Procesa una pregunta utilizando el flujo RAG.

        Parameters
        ----------
        question : str

        Returns
        -------
        dict
        """

        # Buscar documentos relevantes
        documents = self.retriever.invoke(question)

        # Construir contexto
        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        # Construir prompt
        prompt = qa_prompt.invoke(
            {
                "context": context,
                "input": question,
            }
        )

        # Consultar Gemini
        response = self.llm.invoke(prompt)

        #Convertir la respuesta a texto plano
        if isinstance(response.content, str):
            answer = response.content
        elif isinstance(response.content, list):
            answer = "\n".join(
                block.get("text", "")
                for block in response.content
                if isinstance(block, dict)
            )
        else:
            answer = str(response.content)

        return {
            "question": question,
            "answer": answer,
            "sources": [
                doc.metadata
                for doc in documents
            ],
        }