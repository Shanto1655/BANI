
"""Normalize and validate incoming text messages."""

MAX_MESSAGE_LENGTH = 4000


def normalize_message(message: str) -> str:
    """Remove unnecessary whitespace around a message."""
    return message.strip()


def validate_message(message: str) -> str | None:
    """Return an error message if the input is invalid."""
    if not message:
        return "You haven't typed anything yet."

    if len(message) > MAX_MESSAGE_LENGTH:
        return (
            f"Your message is too long. "
            f"Please keep it under {MAX_MESSAGE_LENGTH + 1} characters."
        )

    return None
