"""
Prueba del Document Splitter.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter


def main():

    print("=" * 70)
    print("Cargando documentos...")
    print("=" * 70)

    loader = DocumentLoader()

    documents = loader.load_documents()

    print(f"Documentos originales: {len(documents)}")

    print()

    print("=" * 70)
    print("Dividiendo documentos...")
    print("=" * 70)

    splitter = DocumentSplitter()

    chunks = splitter.split_documents(documents)

    print(f"Chunks generados: {len(chunks)}")

    print()

    print("=" * 70)
    print("Primer chunk")
    print("=" * 70)

    print(chunks[0].page_content)

    print()

    print("=" * 70)
    print("Metadata")
    print("=" * 70)

    print(chunks[0].metadata)

    print()

    print("=" * 70)
    print("Último chunk")
    print("=" * 70)

    print(chunks[-1].page_content)

    print()

    print("=" * 70)
    print("Metadata")
    print("=" * 70)

    print(chunks[-1].metadata)


if __name__ == "__main__":
    main()