from __future__ import annotations
from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Defines the contract that every Large Language Model provider
    must implement.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str :
        """
        Sends a prompt to the language model and returns
        the generated response.

        Args:
            prompt: The prompt sent to the language model.

        Returns:
            The model's generated response as plain text.
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
        raise NotImplementedError