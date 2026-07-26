"""
Prueba del Vector Store.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter
from app.ingestion.vectorstore import VectorStoreService


def main():

    print("=" * 70)
    print("Cargando documentos...")
    print("=" * 70)

    loader = DocumentLoader()

    documents = loader.load_documents()

    print(f"Documentos: {len(documents)}")

    print()

    print("=" * 70)
    print("Dividiendo documentos...")
    print("=" * 70)

    splitter = DocumentSplitter()

    chunks = splitter.split_documents(documents)

    print(f"Chunks: {len(chunks)}")

    print()

    print("=" * 70)
    print("Creando ChromaDB...")
    print("=" * 70)

    vectorstore = VectorStoreService()

    db = vectorstore.create_vectorstore(chunks)

    print()

    print("Base vectorial creada correctamente.")

    print()

    print(f"Total de documentos indexados: {db._collection.count()}")

    print()

    print("=" * 70)
    print("Prueba de búsqueda")
    print("=" * 70)

    results = db.similarity_search(
        "¿Qué incluye el plan Enterprise?",
        k=3,
    )

    for i, doc in enumerate(results, start=1):

        print()

        print(f"Resultado {i}")

        print("-" * 70)

        print(doc.page_content[:300])

        print()

        print(doc.metadata)


if __name__ == "__main__":
    main()