
"""Deterministic commands and basic fallback responses."""

from . import __version__


def handle_command(message: str) -> str | None:
    """Handle recognized built-in commands."""
    command = message.strip().lower()

    if command in {"hello", "hi", "hey"}:
        return "Hello, buddy! How can I help you?"

    if command == "help":
        return "Available commands: hello, help, version, exit, quit."

    if command == "version":
        return f"BANI version {__version__}"

    return None


def get_response(message: str) -> str:
    """Return a basic response when no command is recognized."""
    cleaned_message = message.strip()

    if not cleaned_message:
        return "You haven't typed anything yet."

    return f"I heard you say: {cleaned_message}"
