from email import message
from io import UnsupportedOperation
from agent import llm
from agent.executor.tool_executor import ToolExecutor
from agent.llm.client import LLMClient
from agent.protocol.message import FinalAnswer, ToolCall
from agent.protocol.parser import parse_response


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

    
    def run(self, user_input: str) -> str:
        """
        Execute a single agent interaction.

        The current implementation performs one LLM call,
        optionally executes one tool, and returns the result.

        A future version will evolve into the complete
        Think → Act → Observe loop.
        """
        raw_response = self._llm.generate(user_input)
        message = parse_response(raw_response)

        if(isinstance(message, FinalAnswer)):
            return message.answer
        
        if(isinstance(message, ToolCall)):
            return self._executor.execute(message)

        raise TypeError(
            f"Unsupported response type: {type(message).__name__} "
        )