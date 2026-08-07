import json
from protocal.message import ToolCall, FinalAnswer

class InvalidResponse(Exception):
    pass

def parse_response(response: str):
    try:
        data = json.loads(response)
    except Exception:
        raise InvalidResponse("Response was not a valid JSON object")
    response_type = data.get("type")


    if response_type == "tool_call":
        return ToolCall(
            tool=data.get("tool"),
            arguments=data.get("arguments"),
        )

    if response_type == "final_answer":
        return FinalAnswer(
            answer=data.get("answer"),
        )

    raise InvalidResponse("Unknown response type")