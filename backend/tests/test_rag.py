"""
Prueba del flujo completo RAG.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.qa_service import QAService


def main():

    qa = QAService()

    question = "¿Qué incluye el plan Enterprise?"

    print("=" * 70)
    print("Pregunta")
    print("=" * 70)

    print(question)

    print()

    response = qa.ask(question)

    print("=" * 70)
    print("Respuesta")
    print("=" * 70)

    print(response["answer"])

    print()

    print("=" * 70)
    print("Fuentes")
    print("=" * 70)

    for source in response["sources"]:

        print(source)


if __name__ == "__main__":
    main()