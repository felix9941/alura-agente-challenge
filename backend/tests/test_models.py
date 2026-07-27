from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from google import genai

from app.config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

print("=" * 60)
print("MODELOS DISPONIBLES")
print("=" * 60)

for model in client.models.list():
    print(model.name)