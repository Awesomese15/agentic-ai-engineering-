from __future__ import annotations
from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Defines the contract that every Large Language Model provider
    must implement.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str :
        raise NotImplementedError