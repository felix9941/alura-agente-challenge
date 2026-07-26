"""
Prueba del Document Loader.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.ingestion.loader import DocumentLoader


def main():

    loader = DocumentLoader()

    documents = loader.load_documents()

    print("=" * 70)
    print(f"Documentos cargados: {len(documents)}")
    print("=" * 70)

    for i, doc in enumerate(documents[:5], start=1):

        print(f"\nDocumento {i}")

        print("-" * 70)

        print(doc.page_content[:300])

        print("\nMetadata:")

        print(doc.metadata)


if __name__ == "__main__":
    main()