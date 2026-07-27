"""
Configuration module.

Loads environment variables and exposes project configuration
constants that are used throughout the application.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Base directory

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / ".env")

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY was not found. "
        "Please create a .env file inside backend/"
    )

DATA_PATH = BASE_DIR / "data"
VECTORSTORE_PATH = BASE_DIR / "vectorstore"

# LLM
LLM_MODEL = "gemini-flash-latest"
# Embeddings
EMBEDDING_MODEL = "models/gemini-embedding-001"
# Text Splitter
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RESULTS = 3