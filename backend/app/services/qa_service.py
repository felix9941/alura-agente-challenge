"""
Question Answering Service

Este módulo expone una interfaz sencilla para consultar el agente RAG.
"""

from app.rag import RAGService


class QAService:
    """
    Servicio encargado de responder preguntas utilizando RAG.
    """

    def __init__(self):

        self.rag = RAGService()

    def ask(self, question: str) -> dict:
        """
        Ejecuta una consulta al agente.

        Parameters
        ----------
        question : str

        Returns
        -------
        dict
        """

        if not question.strip():

            return {
                "question": question,
                "answer": "Debe ingresar una pregunta.",
                "sources": [],
            }

        return self.rag.answer_question(question)