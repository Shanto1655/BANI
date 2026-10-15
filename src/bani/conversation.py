
"""Coordinate how BANI responds to a user message."""

from .commands import get_response, handle_command


def get_conversation_response(message: str) -> str:
    """Choose the appropriate response for a user message."""
    command_response = handle_command(message)

    if command_response is not None:
        return command_response

    return get_response(message)
