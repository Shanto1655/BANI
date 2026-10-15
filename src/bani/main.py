
"""Initial application entry point."""

from . import __version__


def get_startup_message() -> str:
    """Return BANI's initial startup message."""
    return "Hello, buddy! I'm BANI. How can I help you?"


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
    """Return a basic response to a user's message."""
    cleaned_message = message.strip()

    if not cleaned_message:
        return "You haven't typed anything yet."

    return f"I heard you say: {cleaned_message}"


def main() -> None:
    """Run BANI's basic text conversation."""
    print(f"BANI: {get_startup_message()}")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBANI: Conversation ended.")
            break

        if message.strip().lower() in {"exit", "quit"}:
            print("BANI: Goodbye, buddy!")
            break

        response = handle_command(message)

        if response is None:
            response = get_response(message)

        print(f"BANI: {response}")


if __name__ == "__main__":
    main()
