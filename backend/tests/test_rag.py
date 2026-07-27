from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.rag import RAGService

def probar_agente():
    print("Inicializando RAG Service...")
    rag_service = RAGService()
    pregunta = "¿Cuáles son las características incluidas en el plan Enterprise?"
    
    print(f"\nPregunta: {pregunta}")
    print("Buscando en documentos y consultando a Gemini...\n")
    
    resultado = rag_service.answer_question(pregunta)
    
    print("=== RESPUESTA ===")
    print(resultado["answer"])
    
    print("\n=== FUENTES UTILIZADAS ===")
    for source in resultado["sources"]:
        print(f"- {source}")

if __name__ == "__main__":
    probar_agente()