from agent.protocal.parser import parse_response

def test_parser_call():
    response = f'''
    {
        "type": "tool_call",
        "tool": "calculator",
        "arguments": {
            "expression": "1 + 1"
        }
    }
    '''
    result = parse_response(response)
    assert result.tool == "calculator"