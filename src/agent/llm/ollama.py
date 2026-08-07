from __future__ import annotations
from ollama import Client
from agent.llm.client import LLMClient


class OllamaClient(LLMClient):
    """
    Concrete implementation of LLMClient backed by Ollama.
    """

    def __init__(self, model: str, host: str = "http://localhost:11434",) -> None:
        self._model = model
        self._client = Client(host=host)
    
    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the configured Ollama model and
        returns the generated response text.
        """
        response = self._client.chat(
            model=self._model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]