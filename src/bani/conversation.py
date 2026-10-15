
"""Coordinate how BANI responds to a user message."""

from .commands import get_response, handle_command
from .input_validation import normalize_message, validate_message


def get_conversation_response(message: str) -> str:
    """Validate a message and choose the appropriate response."""
    normalized_message = normalize_message(message)

    validation_error = validate_message(normalized_message)
    if validation_error is not None:
        return validation_error

    command_response = handle_command(normalized_message)

    if command_response is not None:
        return command_response

    return get_response(normalized_message)
