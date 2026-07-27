from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import RAGService

app = FastAPI(title="Alura Agent API")
rag_service = RAGService()

class Query(BaseModel):
    pregunta: str

@app.post("/chat")
async def chat_endpoint(query: Query):
    respuesta = rag_service.answer_question(query.pregunta)
    return {"respuesta": respuesta}