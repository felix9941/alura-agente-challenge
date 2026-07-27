"""
LLM Service

Este módulo crea y expone el modelo de lenguaje Gemini usado por la app.
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GOOGLE_API_KEY, LLM_MODEL


class LLMService:
    """Servicio encargado de inicializar el modelo Gemini."""

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=0.2,
            convert_system_message_to_human=True,
        )

    def get_llm(self) -> ChatGoogleGenerativeAI:

        return self.llm