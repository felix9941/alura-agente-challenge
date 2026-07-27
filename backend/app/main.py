"""
FastAPI Application

Expone la API del agente RAG.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services.qa_service import QAService

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Alura Agent API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
qa = QAService()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():

    return {
        "message": "Alura Agent API funcionando correctamente."
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: QuestionRequest):

    try:

        response = qa.ask(request.question)

        return response

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )