from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.models.llm import LLMService


def main():

    llm = LLMService().get_llm()

    print("Modelo:", llm.model)

    response = llm.invoke("Responde únicamente: Hola Mundo")

    print(response.content)


if __name__ == "__main__":
    main()