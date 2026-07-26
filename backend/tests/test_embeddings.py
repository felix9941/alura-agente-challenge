"""
Prueba del servicio de Embeddings.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.ingestion.embeddings import EmbeddingService


def main():

    print("=" * 70)
    print("Inicializando servicio...")
    print("=" * 70)

    service = EmbeddingService()

    embeddings = service.get_embeddings()

    print()

    print("Servicio inicializado correctamente.")

    print()

    print("Modelo utilizado:")

    print(embeddings.model)


if __name__ == "__main__":
    main()