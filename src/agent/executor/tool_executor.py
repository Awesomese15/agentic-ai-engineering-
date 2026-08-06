class ToolExecutor:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_call):
        tool = self.registry.get(tool_call.tool)

        if tool is None:
            raise Exception(
                f"Unknown tool {tool_call.tool}"
            )

        return tool.execute(tool_call.arguments)