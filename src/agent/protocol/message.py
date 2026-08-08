from dataclasses import dataclass
from typing import Any

@dataclass
class ToolCall:
    tool: str
    arguments: dict[str, Any]

@dataclass
class FinalAnswer:
    answer: str

@dataclass(frozen=True)
class Observation:
    tool: str
    content: str
