"""
Prompts

Este módulo contiene las plantillas de instrucciones para el LLM.
"""
from langchain_core.prompts import ChatPromptTemplate

# Definimos el comportamiento central del agente corporativo
system_prompt = (
    "Eres un asistente virtual corporativo útil, profesional y preciso. "
    "Utiliza EXCLUSIVAMENTE los siguientes fragmentos de contexto recuperados para responder a la pregunta. "
    "Si la respuesta no se encuentra en el contexto, indica claramente que no tienes esa información en los documentos. "
    "No intentes inventar datos ni usar conocimiento externo.\n\n"
    "Contexto recuperado:\n{context}"
)

# Creamos el template combinando el sistema y la entrada del usuario
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])