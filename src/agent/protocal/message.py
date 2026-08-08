from dataclasses import dataclass
from typing import Any

from agent.tools import tool

@dataclass
class ToolCall:
    tool: str
    arguments: dict[str, any]

@dataclass
class FinalAnswer:
    answer: str

@dataclass(frozen=True)
class Observation:
    tool: str
    content: str
