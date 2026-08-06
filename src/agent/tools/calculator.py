from tools.tool import Tool

class CalculatorTool(Tool):
    
    @property
    def name(self):
        return "calculator"
    
    def execute(self, arguments):
        expression = arguments["expression"]
        result = eval(expression)
        return str(result)