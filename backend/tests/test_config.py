from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import GOOGLE_API_KEY, DATA_PATH

print("API Key:", GOOGLE_API_KEY)
print("Data Path:", DATA_PATH)