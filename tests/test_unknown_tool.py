import pytest
from agent.tools.registry import ToolRegistry
from agent.executor.tool_executor import ToolExecutor
from agent.protocol.message import ToolCall

def test_unknown_tool():

    registry = ToolRegistry()

    executor = ToolExecutor(registry)

    call = ToolCall(
        tool="weather",
        arguments={}
    )

    with pytest.raises(Exception):
        executor.execute(call)