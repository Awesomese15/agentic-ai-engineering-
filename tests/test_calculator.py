from agent.tools.calculator import CalculatorTool
def test_calculator():

    tool = CalculatorTool()

    result = tool.execute(
        {"expression":"3*7"}
    )

    assert result == "21"