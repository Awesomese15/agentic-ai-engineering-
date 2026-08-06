from dataclasses import dataclass
from typing import Any

@dataclass
class ToolCall:
    tool: str
    arguments: dict[str, any]

@dataclass
class FinalAnswer:
    answer: str