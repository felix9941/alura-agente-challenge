"""
Ingestion Pipeline
Este script:
1. Elimina la base vectorial existente (si existe).
2. Carga todos los documentos.
3. Divide los documentos en chunks.
4. Genera embeddings.
5. Crea una nueva base vectorial en ChromaDB.
"""
from pathlib import Path
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import VECTORSTORE_PATH
from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter
from app.ingestion.vectorstore import VectorStoreService


def remove_old_vectorstore() -> None:
    """
    Elimina la base vectorial existente.
    """

    if VECTORSTORE_PATH.exists():

        print("🗑 Eliminando base vectorial anterior...")

        shutil.rmtree(VECTORSTORE_PATH)

        print("✓ Base eliminada.\n")


def main():

    print("=" * 70)
    print("ALURA AGENT - DOCUMENT INGESTION")
    print("=" * 70)
    print()

    # Eliminar base anterior

    remove_old_vectorstore()

    # Cargar documentos

    print("📄 Cargando documentos...")

    loader = DocumentLoader()

    documents = loader.load_documents()

    print(f"✓ {len(documents)} documentos cargados.\n")

    # Dividir documentos

    print("✂ Dividiendo documentos...")

    splitter = DocumentSplitter()

    chunks = splitter.split_documents(documents)

    print(f"✓ {len(chunks)} chunks generados.\n")

    # Crear ChromaDB

    print("🧠 Generando embeddings e indexando...")

    vectorstore = VectorStoreService()

    db = vectorstore.create_vectorstore(chunks)

    print("✓ Base vectorial creada correctamente.\n")

    print(f"📦 Total de chunks indexados: {db._collection.count()}")

    print()

    print("=" * 70)
    print("PROCESO FINALIZADO")
    print("=" * 70)


if __name__ == "__main__":
    main()