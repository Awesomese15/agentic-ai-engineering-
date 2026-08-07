from agent.executor.tool_executor import ToolExecutor
from agent.llm.client import LLMClient
from agent.protocal.parser import parse_response


class Agent:

    """
    Coordinates the complete lifecycle of an AI agent.

    The Agent itself contains no business logic.
    It orchestrates interactions between the language model,
    parser, and tool executor.
    """

    """
    Coordinates the complete lifecycle of an AI agent.

    The Agent itself contains no business logic.
    It orchestrates interactions between the language model,
    parser, and tool executor.
    """

    def __init__(
        self,
        llm: LLMClient,
        executor: ToolExecutor,
    ) -> None:
        self._llm = llm
        self._executor = executor

    
    def run(self, prompt: str):
        response = self._llm.generate(prompt)
        parsed = parse_response(response)